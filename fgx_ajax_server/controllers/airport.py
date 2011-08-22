
import logging
import datetime
import re

from pylons import request, response #, session # , tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from fgx_ajax_server.lib.base import BaseController, render
from fgx_ajax_server.lib import helpers as h

from fgx_ajax_server.model.meta import MC
from fgx_ajax_server.model.meta import Session

from fgx_ajax_server.model import Apt, RunwayThreshold, Ils

#log = logging.getLogger(__name__)



class AirportController(BaseController):


	##================================================================
	@jsonify
	def search(self):

		payload = {'success': True}
		
		if 'search' in request.params:
			search = request.params['search'].strip()
			like = "%" + search.upper() + "%"
			airports = Session.query(Apt).filter( Apt.apt_icao.like(like) ).all()
			payload['airports'] = [a.dic() for a in airports]
			
		return payload
	
	
	
	##=========================================================
	@jsonify
	def airport(self, code):
		
		payload = {	'success': True}
		airport = Session.query(Apt).filter_by(apt_icao=code).first()
		
		if airport == None:
			payload['airport'] = None
			payload['app_error'] = "Airport '%s' not found" % code
			
		else:
			airport_dic = {'airport': [airport.dic()]}
			runwayObs = Session.query(RunwayThreshold).filter_by(apt_icao=code).order_by(RunwayThreshold.rwy_num).all()
			ilsObs = Session.query(Ils).filter_by(apt_icao=code).order_by(Ils.rwy_num).all()
			
			## walk thru runways and stick in a dic, along with ils
			runways_dic = {}
			runway_ends = []
			for runway in runwayObs:
				
				rwy_num = str(runway.rwy_num.strip())
				if not rwy_num in runways_dic: ## WTF dupes ??
					runways_dic[rwy_num] = runway.dic()
					runways_dic[rwy_num]['ils'] = None
					for ils in ilsObs:
						if rwy_num == ils.rwy_num:
							runways_dic[rwy_num] = ils.dic()
					rev_rwy = self.reverse_rwy(runway.rwy_num)
					
					if not runways_dic.has_key(rev_rwy):
						runway_ends.append( [rwy_num, rev_rwy] )
	

			
			airport_dic['runways'] = []
			for ends in runway_ends:
				dic = {}
				dic['runway'] = "%s-%s" % (ends[0], ends[1])
				dic['thresholds'] =  [ runways_dic[ends[0]], runways_dic[ends[1]] ]
				airport_dic['runways'].append( dic )
		
			payload['airport'] = airport_dic
		return payload
		
		
		
	def reverse_rwy(self, rwy_num):
		parts = re.compile("(\d+)(.*)").split(rwy_num, maxsplit=0)
		#print rwy_str, len(rwy_str), parts
		num = int(parts[1])
		lr = parts[2].upper() 

		#if num:
		#	return rwy_str	
		
		if num > 18:
			rnum = num - 18
		else:
			rnum = num + 18
			
		if lr != "":
			if lr == "L":
				lr = "R"
			elif lr == "R":
				lr = "L"

		return str("%02d%s" % (rnum, lr)).strip()


"""
gral queries..
landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50000);
[23:06] * peteffs brb cofee and smoke,,,
[23:06] <gral> or ...
[23:06] <gral> landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50*1000*1.85201);

"""


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
			data = {'airport': [airport.dic()]}
			runwayObs = Session.query(RunwayThreshold).filter_by(apt_icao=code).order_by(RunwayThreshold.rwy_num).all()
			ilsObs = Session.query(Ils).filter_by(apt_icao=code).order_by(Ils.rwy_num).all()
			
			## walk thru runways and stick in a dit, along with ils
			runways_dic = {}
			runway_ends = []
			for runway in runwayObs:
				rwy_num = runway.rwy_num.strip()
				runways_dic[rwy_num] = runway.dic()
				runways_dic[rwy_num]['ils'] = None
				for ils in ilsObs:
					if rwy_num == ils.rwy_num:
						runways_dic[rwy_num] = ils.dic()
				rev_rwy = self.reverse_rwy(runway.rwy_num)
				print rwy_num, rev_rwy
				if not rev_rwy in runways_dic:
					runway_ends.append( (rwy_num, rev_rwy) )
			print runway_ends
				
				
			if len(runwayObs) > 0:
				runways = []
				for runway in runwayObs:
					dic = runway.dic()
					print runway.rwy_num, self.reverse_rwy(runway.rwy_num)
					dic['ils'] = None
					for ils in ilsObs:
						if ils.rwy_num == ils.rwy_num:
							dic['ils'] = ils.dic()
					runways.append(dic)
				data['runways'] = runways
			else:
				data['runways'] = []
		
			payload['airport'] = data
		return payload
		
		
		
	def reverse_rwy(self, rwy_num):
		rwy_str = rwy_num
		parts = re.compile("(\d+)(.*)").split(rwy_str, maxsplit=0)
		print rwy_str, len(rwy_str), parts
		num = int(parts[1])
		lr = parts[2]
		
		#if(!$num)
		#{
		#	return ${rwy_num};
		#}
		
		if num > 18:
			num = num - 18
		else:
			num += num + 18

		if lr != "":		
			if lr.upper() == "L":
				lr = "R"
			else:
				lr = "L"
		
		return "%s%s" % (num, lr)


"""
gral queries..
landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50000);
[23:06] * peteffs brb cofee and smoke,,,
[23:06] <gral> or ...
[23:06] <gral> landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50*1000*1.85201);

"""

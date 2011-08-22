
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

log = logging.getLogger(__name__)


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
			runwayObs = Session.query(RunwayThreshold).filter_by(apt_icao=code).all()
			ilsObs = Session.query(Ils).filter_by(apt_icao=code).all()
			if len(runwayObs) > 0:
				runways = []
				for runway in runwayObs:
					dic = runway.dic()
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
		pass
		"""
		my($num, $lr) = ($rwy_num =~ /(\d+)(.*)/);

		if(!$num)
		{
			return ${rwy_num};
		}

		if($num > 18)
		{
			$num -= 18;
		}
		else
		{
			$num += 18;
		}

		if($lr ne "")
		{
			if(uc($lr) eq "L")
			{
				$lr = "R";
			}
			else
			{
				$lr = "L";
			}
		}

		return "${num}${lr}";
		}

		"""

"""
gral queries..
landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50000);
[23:06] * peteffs brb cofee and smoke,,,
[23:06] <gral> or ...
[23:06] <gral> landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50*1000*1.85201);

"""

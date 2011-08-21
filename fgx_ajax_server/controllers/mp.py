
import logging
import datetime

from pylons import request, response #, session # , tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from fgx_ajax_server.lib.base import BaseController, render

from fgx_ajax_server.model.meta import MC

log = logging.getLogger(__name__)


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class MainController(BaseController):


	##================================================================
	
	@jsonify
	def index(self):

		c = MC.get("hit_counter")
		if c == None:
			c = 1
		c += 1
		MC.set("hit_counter", c)
		
		MC.set("TEST", {'this': 'foo', 'x': True})

		payload = {'success': True, 'c': c,  'T': MC.get("TEST")}

		return payload
		
	@jsonify
	def mp(self, end_point=None):
		
		c = MC.get("hit_counter")
		if c == None:
			c = 1
		c += 1
		MC.set("hit_counter", c)
		
		payload = {	'success': True, 
					'utc' : datetime.datetime.now().strftime(DATE_FORMAT),
					'hit_counter': MC.get("hit_counter")
				}
		
		if end_point == None:
			"""No end point so send list of end points """
			payload['end_points'] = ['/info', '/servers']
			
		else:
			
			mp_info = MC.get("mp_info")
			if end_point == "info":
				payload['mp_info']  = mp_info
					
			elif end_point == "servers":
				payload['servers']  = mp_info['servers']

		return payload
		



"""
gral queries..
landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50000);
[23:06] * peteffs brb cofee and smoke,,,
[23:06] <gral> or ...
[23:06] <gral> landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50*1000*1.85201);

"""

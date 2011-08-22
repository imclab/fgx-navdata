
import logging
import datetime
try:
	import django.utils.simplejson as json
except:
	import json

from pylons import request, response #, session # , tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from fgx_ajax_server.lib.base import BaseController, render

from fgx_ajax_server.model.meta import MC

log = logging.getLogger(__name__)

from fgx_ajax_server.config import xconf


class MpController(BaseController):


	##================================================================
	
	@jsonify
	def index(self):

		payload = {'success': True, 'endpoints': ['servers','flights']}

		return payload
		
	@jsonify
	def flights(self, end_point=None):
		
		payload = {	'success': True, 'utc' : datetime.datetime.now().strftime(xconf.DATE_FORMAT)}
		
		flights = MC.get("mp_flights")
		if flights:
			payload['flights']  = json.loads(flights)
		else:
			payload['flights'] = []
		return payload
		
	@jsonify
	def servers(self, end_point=None):
		
		payload = {	'success': True, 'utc' : datetime.datetime.now().strftime(xconf.DATE_FORMAT)}
		
		servers = MC.get("mp_servers")
		if servers:
			payload['servers']  = json.loads(servers)
		else:
			payload['servers'] = []
		return payload


"""
gral queries..
landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50000);
[23:06] * peteffs brb cofee and smoke,,,
[23:06] <gral> or ...
[23:06] <gral> landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50*1000*1.85201);

"""

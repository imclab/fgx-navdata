
import logging
import datetime

from pylons import request, response #, session # , tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from fgx_ajax_server.lib.base import BaseController, render
from fgx_ajax_server.lib import helpers as h

from fgx_ajax_server.model.meta import MC
from fgx_ajax_server.model.meta import Session

from fgx_ajax_server.model import Apt

log = logging.getLogger(__name__)



class AirportController(BaseController):


	##================================================================
	
	@jsonify
	def index(self):

		
		payload = {'success': True}

		return payload
		
	@jsonify
	def airport(self, code):
		
		payload = {	'success': True}
		airport = Session.query(Apt).filter_by(apt_icao=code).first()
		if airport == None:
			payload['airport'] = None
			payload['app_error'] = "Airport '%s' not found" % code
		else:
			payload['airport'] = [airport.dic()]	
		
		return payload
		
		
		
		
		
		return payload
		



"""
gral queries..
landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50000);
[23:06] * peteffs brb cofee and smoke,,,
[23:06] <gral> or ...
[23:06] <gral> landcover=> SELECT icao FROM apt_airfield WHERE ST_DWithin((SELECT ST_Transform(wkb_geometry, 900913) FROM apt_airfield WHERE icao LIKE 'LSZH'), ST_Transform(wkb_geometry, 900913), 50*1000*1.85201);

"""

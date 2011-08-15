
import logging


from pylons import request, response #, session # , tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from fgx_ajax_server.lib.base import BaseController, render

from fgx_ajax_server.model.meta import MC

log = logging.getLogger(__name__)




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
	def mp_servers(self):
		
		payload = {	'success': True, 
					'mp_servers': MC.get("mp_servers")
				}

		return payload

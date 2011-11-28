#!/usr/bin/env python

import os
import sys
try:
	import django.utils.simplejson as json
except:
	import json
	
from paste.deploy import appconfig
from pylons import config

parent_path = os.path.abspath( os.path.join(os.path.dirname(__file__), "../") )
sys.path.append(parent_path)  


if os.path.isfile(parent_path + "/LOCAL"):
	ini = parent_path + '/development.ini'
else:
	ini = parent_path + 'production.ini'

from fgx_ajax_server.config.environment import load_environment
conf = appconfig('config:' + ini)
load_environment( conf.global_conf, conf.local_conf)


## Aiports
from fgx_ajax_server.model.meta import Session
from fgx_ajax_server.model import Apt, RunwayThreshold


def write_objects(file_name, objects):
	c= 0
	f = open(file_name, "w")
	for ob in objects:
		c += 1
		print c, 
		f.write( json.dumps(ob.dic()) + "\n" )
	f.close()
	
airports = Session.query(Apt).all()
write_objects("./apt.txt", airports)

runways = Session.query(RunwayThreshold).all()
write_objects("./runwaythreshold.txt", runways)



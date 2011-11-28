#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: <Peter Morgan> pete at freeflightsim dot org

# Processes airports.csv from ourairports.com
# 

#!/usr/bin/env python

import os
import sys
import json
	
from paste.deploy import appconfig
from pylons import config

parent_path = os.path.abspath( os.path.join(os.path.dirname(__file__), "../../../") )
print parent_path
sys.path.append(parent_path)  


if os.path.isfile(parent_path + "/LOCAL"):
	ini = parent_path + '/development.ini'
else:
	ini = parent_path + 'production.ini'

print ini
from fgx_ajax_server.config.environment import load_environment
conf = appconfig('config:' + ini)
load_environment( conf.global_conf, conf.local_conf)


## Aiports
from fgx_ajax_server.model.meta import Session
from fgx_ajax_server.model import Apt, RunwayThreshold


sys.exit(0)

import sys
import os
import csv

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))  
from libs import conf

from libs import airport


#config = conf.init()

source_file = conf.Conf.temp_file("airports.csv")
#print import_file


c = 0
try:
    reader = csv.reader(source_file)
    for row in reader:
		c += 1
		if c == 1:
			#skip
			print row
		else:
			#print row
			airport.update_from_row("ourairports/airports.csv", row)
			print c, row[1]
		if c == 300:
			print "stopped"
			#sys.exit(0)	
		
finally:
    source_file.close()
    
"""    
c = 0
for line in import_file:
	c += 1
	if c == 1:
		# skip first line
		pass 
	else:
		print line
		
	if c == 30:
		print "stopped"
		sys.exit(0)
"""
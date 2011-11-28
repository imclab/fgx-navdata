#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: <Peter Morgan> pete at freeflightsim dot org

# Processes airports.csv from ourairports.com
# 
import csv

import shell_conf
from fgx_ajax_server.model import meta, Airport
from utils import helpers as h

source_file = conf.Conf.temp_file("airports.csv")

def run():
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
				#airport.update_from_row("ourairports/airports.csv", row)
				meta.Session.query(Airport).filter_by(source=source, ident=apt_code).first()
				
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
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: <Peter Morgan> pete at freeflightsim dot org

# Processes airports.csv from ourairports.com
# 
import csv

import shell_conf
from fgx_ajax_server.model import meta, Airport
from utils import helpers as h

source_file = h.temp_file("airports.csv")
source = "ourairports"

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
				print c, row
				apt_code = row[1]
				
				do_import = False
				if shell_conf.icao_only == True:
					do_import = h.is_icao(apt_code)
				else:
					do_import = True
				
				if do_import:
					#airport.update_from_row("ourairports/airports.csv", row)
					apt = meta.Session.query(Airport).filter_by(source=source, airport_code=apt_code).first()
					if apt == None:
						apt = Airport()
						apt.source = source
						apt.airport_code = apt_code
						meta.Session.add(apt)
					apt.airport = row[3]
					apt.type = row[2]
					apt.iata_code = row[13]
					
					meta.Session.commit()
					
				
				
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
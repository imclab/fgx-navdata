#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: <Peter Morgan> pete at freeflightsim dot org

# Processes airports.csv from ourairports.com
# 

import sys
import os
import csv

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))  

#from libs import conf
import shell_conf

source_file = shell_conf.temp_file("runways.csv")

"""
from libs import airport


"""
#from libs import runways

c = 0
try:
    reader = csv.reader(source_file)
    for row in reader:
		c += 1
		if c == 1:
			#skip
			print row
			#sys.exit(0)
		else:
			#print row
			#sA = airport.update_from_row("ourairports/airports.csv", row)
			#print row[1]
			apt_code = row[2]
			runway = row[8] + "-" + row[14]
			print apt_code, runway
			
			r = runways.Runway(apt_code, runway)
			r.length_ft = row[3]
			r.width_ft = row[4]
			
			t = Threshold(apt_code, row[8])
			
			
			
		if c == 300:
			print "stopped"
			sys.exit(0)	
		
finally:
    source_file.close()
"""    
0'id', 
1'airport_ref',
2'airport_ident', 
3'length_ft',
4'width_ft',
5'surface', 
6'lighted',
7'closed',

8'le_ident', 9'le_latitude_deg', 10'le_longitude_deg', 11'le_elevation_ft', 12'le_heading_degT', 13'le_displaced_threshold_ft',
14'he_ident', 15'he_latitude_deg', 16'he_longitude_deg', 17'he_elevation_ft', 18'he_heading_degT', 19'he_displaced_threshold_ft', 
"""
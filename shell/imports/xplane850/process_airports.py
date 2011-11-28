#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: <Peter Morgan> pete at freeflightsim dot org

# Processes xplane 850

import os
import sys

import shell_conf

from fgx_ajax_server.model import meta, Runway, Threshold
from utils import helpers as h


apt_dat_file = "/home/ffs/ffs-app-engine/nav_data_processing/Resources/default scenery/default apt dat/Earth nav data/apt.dat"
source = "xplane850/apt.dat"

class ROW_CODES:
	airport = 1
	seaport = 16
	heliport = 17
	
	runway = 100 
	water = 101 
	helipad = 102 


class APT_COLS:
	key = 0
	elevation = 1
	atc = 2 
	_DOO = 3
	airport_code = 4
	name = 5




def run():
	
	c = 0
	fileObj = open(apt_dat_file, "r")
	
	print fileObj.readline()
	
	while 1:
		line =  fileObj.readline()

		line = line.strip()
		if line:
			cols = line.split()
			## aiport, seaplane, heliport
			akey = cols[0]
			
			#heliports = []
			#seaports = []
			
			
			
			
			if akey != '99':
				
				if akey in ['1', '16', '17']:
					seaport = True if akey == '16' else False
					heliport = True if akey == '17' else False
					#                            icoa,    name,    seaport, heliport, elev,    atc
					#print cols
					airport_raw = " ".join(cols[5:])
					apt_code = str(cols[4])
					
					do_import = False
					if shell_conf.icao_only:
						do_import = h.is_icao(apt_code)
					else:
						do_import = True
					#is_valid = self.is_icao(icao)
					if do_import:
						#self.airports_csv.writerow( [cols[4], airport, seaport, heliport, cols[1], cols[2]] )
						print "===", apt_code, cols
						
						#bits = str(airport_raw)
						#airport = ''
						#print "...........", airport
						#for b in bits:
						#	try:
						#		json.dumps({'foo': b})
						#		airport += b
						#	except:
						#		pass

						"""
						self.airports[icao] = { 
								'name': airport, 
								'seaport': seaport, 
								'heliport': heliport,
								'elevation': int(cols[1]),
								'atc': bool(cols[2])
						}
						"""
						#self.airports[icao] = airport.replace("'", "")
								
						#print self.airports[icao]
						#json.dumps(self.airports[icao])
					#else:
						#print 'skip', icao
					#yaml.dump(yam, self.airports_yaml, width=500, indent=4)
					if c % 500 == 0:
						print c, cols[4] #, airport
			
					if c == 50:
						print "break"
						#self.process_items()
						sys.exit(0)
					c += 1
	"""					
	for line in f.readlines():
		c += 1
		print line
		
		
		if c == 10:
			sys.exit(0)
	"""
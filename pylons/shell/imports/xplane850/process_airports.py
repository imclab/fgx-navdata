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

class ROW_CODE:
	airport = "1"
	seaport = "16"
	heliport = "17"
	
	runway = "100" 
	water = "101" 
	helipad = "102" 


class APT_COL:
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
	do_import = False
	while 1:
		line =  fileObj.readline()

		line = line.strip()
		if line:
			cols = line.split()
			## aiport, seaplane, heliport
			row_code = cols[0]
			
			#heliports = []
			#seaports = []
			#print cols
			if row_code == ROW_CODE.airport:
				apt_code = str(cols[4])
				do_import = False
				if shell_conf.icao_only:
					do_import = h.is_icao(apt_code)
				else:
					do_import = True
			
			
			if do_import and row_code == ROW_CODE.runway:	
				#print cols
				
				runway = cols[8] + "-" + cols[17]
				print "=", apt_code, runway
				rwyOb = meta.Session.query(Runway).filter_by(source=source, airport_code=apt_code, runway=runway).first()
				if rwyOb == None:
					rwyOb = Runway()
					rwyOb.source = source
					rwyOb.airport_code = apt_code
					rwyOb.runway = runway
					meta.Session.add(rwyOb)
				rwyOb.width_m = cols[1]
				rwyOb.width_ft = h.metres_to_feet(cols[1])
				meta.Session.commit()
				
				thr1Ob = meta.Session.query(Threshold).filter_by(source=source, airport_code=apt_code, threshold=cols[8]).first()
				if thr1Ob == None:
					thr1Ob = Threshold()
					thr1Ob.source = source
					thr1Ob.airport_code = apt_code
					thr1Ob.threshold = cols[8]
					meta.Session.add(thr1Ob)
				thr1Ob.lat = cols[9]
				thr1Ob.lon = cols[10]
				thr1Ob.displaced_m = cols[11]
				thr1Ob.displaced_ft = h.metres_to_feet(cols[11])
				meta.Session.commit()
				
				
			
			if 1 == 0: #row_code != '99':
				
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
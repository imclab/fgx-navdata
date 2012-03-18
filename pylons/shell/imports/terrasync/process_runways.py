#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: <Peter Morgan> pete at freeflightsim dot org

# Processes thresholds from terrasync root

import os
import sys
from lxml import objectify

import shell_conf

from fgx_ajax_server.model import meta, Runway, Threshold
from utils import helpers as h


terra_path = "/home/flight-sim/terra_sink/Airports/"
source = "terrasync"

def run():
	
	c = 0
	for dirname, dirnames, filenames in os.walk(terra_path):
		#for subdirname in dirnames:
		#	print os.path.join(dirname, subdirname)

		for filename in filenames:
			#print "\n", filename
			if len(filename) > 12:
				#print filename.endswith(".threshold.xml")	, filename
				c += 1
				
				
				if filename.endswith(".threshold.xml"):
					apt_code = filename.split(".")[0]
					
					do_import = False
					if shell_conf.icao_only == True:
						do_import = h.is_icao(apt_code)
						
					else:
						do_import = True
							
					#fileObj = open(os.path.join(dirname, filename))
					#print xml_string
					if do_import:
						
						xml_string =   open(os.path.join(dirname, filename)).read()
						tree = objectify.fromstring(xml_string)
						
						
						#print "==", tree.runway[0].tag
						for rwy in tree.runway:
							
							runway = rwy.threshold[0].rwy.text + "-" + rwy.threshold[1].rwy.text
							#print "rwy", apt_code, runway #rwy.threshold[0].lat.text
							
							rwyOb = meta.Session.query(Runway).filter_by(source=source, airport_code=apt_code, runway=runway).first()
							if rwyOb == None:
								rwyOb = Runway()
								rwyOb.source = source
								rwyOb.airport_code = apt_code
								rwyOb.runway = runway
								meta.Session.add(rwyOb)
							meta.Session.commit()
					else:
						print "skip=", apt_code, filename
						
					#xml_string = open(os.path.join(dirname, filename)).read()
					#print xml_string
					#root = objectify.fromstring( xml_string )
					#p#rint root['runway'] #runway
					
				else:
					
					#print dirname, filename
					#print os.path.join(dirname, filename)
					#print "\n"
					#print filename
					pass
				if c == 2000:
					sys.exit(0)
			else:
				#print "SKIP=", filename
				pass
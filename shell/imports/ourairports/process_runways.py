#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: <Peter Morgan> pete at freeflightsim dot org

# Processes runways.csv from ourairports.com
# 
import sys
import csv

import shell_conf
from fgx_ajax_server.model import meta, Runway, Threshold, RunwaySurfaces
from utils import helpers as h

source_file = shell_conf.temp_file("runways.csv")
source="ourairports"

def run():
	print "============================="
	print "== Our Airports - RUNWAYS =="
	print "============================="
	c = 0
	try:
		
		runway_surfaces = RunwaySurfaces.reverse_lookup()
		print runway_surfaces
		reader = csv.reader(source_file)
		for row in reader:
			c += 1
			if c == 1:
				#skip first row
				pass
			else:
				#print row
				#sA = airport.update_from_row("ourairports/airports.csv", row)
				#print row[1]
				apt_code = row[2]
				runway = row[8] + "-" + row[14]
				if c % 50 == 0:
					print c, apt_code, runway
				
				#print "------------------"
				rwyOb = None # meta.Session.query(Runway).filter_by(source=source, airport_code=apt_code, runway=runway).first()
				if rwyOb == None:
					rwyOb = Runway()
					rwyOb.airport_code = apt_code
					rwyOb.runway = runway
					rwyOb.source = source 
					meta.Session.add(rwyOb)
					#print "add"
					pre = None
				else:
					pre = rwyOb.dic().copy()
					#print "update"
				rwyOb.length_ft = int(row[3]) if row[3] else None
				rwyOb.width_ft = row[4] if row[4] else None
				
				#print row
				rwyOb.length_m = h.feet_to_metres(row[3]) if rwyOb.length_ft else None
				rwyOb.width_m = h.feet_to_metres(row[4]) if rwyOb.width_ft else None
				
				
				surf =  str(row[5]).upper().replace("'","")
				#print surf
				rwyOb.surface_id = None
				
				# Grass
				if  surf.startswith("GRASS") or \
					surf.startswith("TURF") or \
					surf in ["TURF", "GRASS",  "TURF-GRVL", "GRS",
														"TURF-DIRT", "TURF-GRVL-F", "TURF-DIRT-F", "TURF-GRVL-P",
														"SOD", "TURF-E", "TURF-DIRT-P"]:
					rwyOb.surface_id = runway_surfaces["Grass/Turf"]
					
				# Asphalt
				elif surf.startswith("ASPH") or \
					 surf.startswith("ASPHALT") or \
					 surf in ["ASP", "BIT", "ASP/TURF", "OLD ASP", "ASFALT", "TAR", "ASPHALT", "PER", "ASB",
								"BITUMINOUS", "ALPHALT", "ASP/CONC", "ASP/CON"]:
					rwyOb.surface_id = runway_surfaces["Asphalt"]

				# Concrete
				elif  surf.startswith("CONC") or \
					  surf in ["CON", "PAVED", "CONCRETE", "COM", "PEM", "COR", "CON/ASP", "CON/PAD"]:
					rwyOb.surface_id = runway_surfaces["Concrete"]

				# Dirt
				elif surf.startswith("DIRT") or \
					 surf.startswith("CLAY") or \
					 surf in ["CALICHE", "TRTD-DIRT", "TRTD", "TRTD-DIRT-P", "EARTH", "OILED DIRT", "SOFT SAND",
								"STONE", "STONE DUST",  "EARTH/TURF", "SAND/CLAY/GRAV", "EARTH/SNOW", "MAC",
								"NATURAL SOIL, GRASS / SOD", "PACKED DIRT", "NATURAL SOIL", "CLA", "TRTD-DIRT-F"
								]:
					
					rwyOb.surface_id = runway_surfaces["Dirt"]
					
				# Gravel	
				elif surf.startswith("GRVL") or \
					surf.startswith("GRAVEL") or \
					surf in [ "GRE", "GVL","GRV",  "LOOSE GRAVEL", "SAN", "SAND/GRVL", "TRTD GRVL", "SND", "GRAV",
								 "SAND", "GRVL-DIRT-P", "SAND/GRAVEL/AS", "SAND/GRAVEL",  "LAT", "GROUND", "CORAL",
								 "OILED GRAVEL/T", "OILED GRAVEL", "PACKED GRAVEL", "CRUSHED ROCK", "BITUMEN/GRAVEL",
								 "SAND-F"
								]:
					rwyOb.surface_id = runway_surfaces["Gravel"]

				# Mats
				elif surf.startswith("MATS") or \
					surf in ["C", "PSP", "ROOF-TOP", "ROOFTOP", "DECK", "NSTD", "MET", "STEEL-CONC",
								"ALUM-DECK", "ALUMINUM", "METAL", "STEEL", "PFC", "ALUM", "BRI",
								"PIERCED STEEL PLANKING / LANDING MATS / MEMBRANES"]:
					rwyOb.surface_id = runway_surfaces["Mats"]

				# Water
				elif surf.startswith("WATER"):
					rwyOb.surface_id = runway_surfaces["Water"]

				# Water
				elif surf in ["ICE", "ICE - FROZEN LAKE", "SNO"]:
					rwyOb.surface_id = runway_surfaces["Snow/Ice"]
					
				# Other
				elif surf.startswith("TREATED") or \
					surf in ["WOOD",  "BRICK", "OIL&CHIP-T-G", "UNK", "COP", "OILED", "U", "UNKNOWN", 
							"UNPAVED", "CLOSED", "NEOPRENE"]:
					rwyOb.surface_id = runway_surfaces["Other"]
					
				elif surf == "":
					rwyOb.surface_id = runway_surfaces["Other"]
					
				if rwyOb.surface_id == None:
					print "no surface=", surf,row
					sys.exit(0)
					
				#meta.Session.commit()
				#print rwyOb.dic()
				if pre != None:
					diff = h.diff(pre, rwyOb.dic())
					#print "diff=", diff 
				#print row
				if 1 == 0:
					thlOb = meta.Session.query(Threshold).filter_by(airport_code=apt_code, threshold=row[8]).first()
					if thlOb == None:
						thlOb = Threshold()
						thlOb.source = source
						thlOb.airport_code = apt_code
						thlOb.threshold = row[8]
						meta.Session.add(thlOb)
					
					#if row[9] and row[10]:
					thlOb.lat = row[9] if row[9] else None
					thlOb.lon = row[10] if row[10] else None
						
					
					thlOb.elevation_ft = row[11] if row[11] else None
					thlOb.elevation_m = h.feet_to_metres( row[11] ) if thlOb.elevation_ft else None
					
					thlOb.true_heading = row[12] if row[12] else None
					meta.Session.commit()
					
				#print "rwy=", rwyOb
				
				#t = Threshold(apt_code, row[8])
				
				
				
				
			if c == 20:
				print "stopped"
				#sys.exit(0)	
			
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
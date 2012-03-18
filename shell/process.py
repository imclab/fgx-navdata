#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

#import argparse
from optparse import OptionParser

import shell_conf


"""
parser = argparse.ArgumentParser(description='Process files.')
parser.add_argument('--icao-only', action='store',  nargs="?", type=int, default=1, help='Wherther to import only ICAO codes')
parser.add_argument('--all', action='store', nargs="?",  help='Process All')
parser.add_argument('--xplane850', action='store', nargs="?",  help='Process AptDat')
parser.add_argument('--ourairports', action='store', nargs="?",  help='Process OurAirports ')
parser.add_argument('--ourairports-runways', action='store',  nargs="?", help='Process OurAirports Runways only')


args = parser.parse_args()

shell_conf.icao_only = bool(args.icao_only)
print args, args.icao_only, shell_conf.icao_only
"""

##==================================================
parser = OptionParser()
parser.add_option( "--icao-only", dest="icao_only", action="store_true",
                  help="Import only ICAO codes (", default=True)

parser.add_option("--ourairports-airports",
                  action="store_true", dest="ourairports_airports", default=False,
                  help="Import OurAiports airports")
                  
parser.add_option("--ourairports-runways",
                  action="store_true", dest="ourairports_runways", default=False,
                  help="Import OurAiports runways")

parser.add_option("--xplane-850",
                  action="store_true", dest="xplane850", default=False,
                  help="Import AptDat 850")
                  
(options, args) = parser.parse_args()

print options, args

shell_conf.icao_only = options.icao_only


if options.ourairports_airports == False and \
	options.ourairports_runways == False and \
	options.xplane850 == False :
		print "Nothing to do "
		parser.print_usage()
		sys.exit(0)


##==================================================

## Our Airports
if options.ourairports_airports:
	import imports.ourairports.process_airports
	imports.ourairports.process_airports.run()
	
if options.ourairports_runways:
	import imports.ourairports.process_runways
	imports.ourairports.process_runways.run()



## Terrasync
if 1 == 0:
	import imports.terrasync.process_runways
	imports.terrasync.process_runways.run()



## Xlane
if options.xplane850:
	import imports.xplane850.process_airports
	imports.xplane850.process_airports.run()


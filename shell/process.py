#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import datetime, calendar
import argparse

import shell_conf


"""
parser = argparse.ArgumentParser(description='Process files.')
parser.add_argument('--year', action='store', nargs="?", help='year to process or --year= for current')
parser.add_argument('--month', action='store', nargs="?", help='month to process or --month= for current')
parser.add_argument('--day', action='store', nargs="?", help='day to process or --day= for current')

args = parser.parse_args()

"""

if 1 == 0:
	import imports.ourairports.process_runways
	imports.ourairports.process_runways.run()

if 1 == 0:
	import imports.terrasync.process_runways
	imports.terrasync.process_runways.run()

if 1 == 1:
	import imports.xplane850.process_airports
	imports.xplane850.process_airports.run()


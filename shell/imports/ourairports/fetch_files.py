#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: <Peter Morgan> pete at freeflightsim dot org

# Fetches data files from ourairports.com
# The list of files is at http://www.ourairports.com/data/

# url fetches the files
# saves to temp/ourairports/*

import sys
import os

from email.utils import parsedate_tz
from urllib2 import Request, urlopen, URLError

## Init Config
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))  
from config import conf
config = conf.load()
#print config


base_url = "http://www.ourairports.com/data/"
files= ["airports.csv"]

print "---------------------------------"
print "OurAirports.com - Fetching Files"
print ""
for f in files:
	
	url = base_url + f
	print ">> Fetching: " + url
	req = Request(url)
	try:
		response = urlopen(req)
	except URLError, e:
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
		elif hasattr(e, 'code'):
			print 'The server couldn\'t fulfill the request.'
			print 'Error code: ', e.code
	else:
		# everything is fine
		print response.info()

		print parsedate_tz(response.info()['Last-Modified'])

		print "#" + response.info()['Last-Modified']
		target_file = config.temp_dir + f
		if 1 == 0:
			f = open(target_file, "w")
			f.write(response.read())
			f.close()
		print "<< Saved to: '%s'" % target_file
		print ""

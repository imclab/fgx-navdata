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


import shell_conf
import utils.helpers as h

base_url = "http://www.ourairports.com/data/"
#files= ["airports.csv"]
files = ["countries.csv", "regions.csv"]

print "---------------------------------"
print "OurAirports.com - Fetching Files"
print "---------------------------------"


for file_name in files:
	
	url = base_url + file_name
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
		target_file = h.temp_file("ourairports", file_name)
		if 1 == 0:
			f = open(target_file, "w")
			f.write(response.read())
			f.close()
		print "<< Saved to: '%s'" % target_file
		print ""

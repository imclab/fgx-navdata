

import os
import sys

from decimal import *

import re
icao_pattern = re.compile("[A-Z]{4}")

import shell_conf


##==================================================
def feet_to_metres(val, precision=2):
	# 1 foot = 0.3048 metres
	if val == None or str(val).strip() == "":
		return None
		
	#getcontext().prec = precision
	#getcontext().rounding=ROUND_05UP
	m = float(val) * 0.3048
	return Decimal("%0.2f" % m)
	return "%0.2f" % m
	
	
def metres_to_feet(val, precision=2):
	# 1 metre = 3.2808399 feet
	if val == None or str(val).stripdd() == "":
		return None
	return float(val) * 3.2808399
	
##==================================================	
def is_icao(code):
	if len(code) == 4:
		if icao_pattern.match(code):
			return True
		
	return Falses
	
##==================================================	
def diff(pre, post):
	dic = {}
	for k in pre.keys():
		if pre[k] != post[k]:
			dic[k] = "%s > %s" % (pre[k], post[k])
	if len(dic.keys()) == 0:
		return None
	return dic
	
	
##==================================================
def temp_file(directory, file_name):
	print shell_conf.temp_dir()
	if not os.path.exists(shell_conf.temp_dir()):
		print "TEMP path '%s' not exist" % shell_conf.temp_dir()
		sys.exit(0)
		
		
	
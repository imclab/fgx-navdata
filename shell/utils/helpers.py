
import re

icao_pattern = re.compile("[A-Z]{4}")


def feet_to_metres(val):
	# 1 foot = 0.3048 metres
	#print "feet_to-metres=", val
	if val == None or str(val).strip() == "":
		#print "NON"
		return None
	return  float(val) * 0.3048
	
	
def is_icao(code):
	if len(code) == 4:
		if icao_pattern.match(code):
			return True
		
	return False
"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password


def to_dic(obj):
	
	dic = obj.__dict__
	
	ret = {}
	for ki in dic:
		v = dic[ki]
		
		
		if isinstance(v, unicode) or isinstance(v, str):
			## String types need to be stripped as CHAR has trialing spaces
			ret[ki] = v.strip()
			
		elif isinstance(v, int):
			ret[ki] = v
		else:
			print  type(v)
	
	
	return ret
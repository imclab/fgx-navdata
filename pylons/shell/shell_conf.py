
"""
This file is imported on all the shell scripts
Declares and load the environment

utils.helpers
typically used as
import utils.helpers as h

accomodates a lot of the "functions".. atmo

"""

import os
import sys

from paste.deploy import appconfig
from pylons import config

## We need to append the parent_path to load the fgx_pylons stuff
parent_path = os.path.abspath( os.path.join(os.path.dirname(__file__), "../") )
sys.path.append(parent_path + "/")  

##=====================================================
## Load the ini file, 
## got dev create a file "LOCAL" 
# eg touch ../LOCAL
if os.path.isfile(parent_path + "/LOCAL"):
	ini = parent_path + '/development.ini'
else:
	ini = parent_path + '/production.ini'

## Load and unut the pylons enviroment
from fgx_ajax_server.config.environment import load_environment
conf = appconfig('config:' + ini)
load_environment( conf.global_conf, conf.local_conf)

##===============================================================================
# Global Vars

icao_only = True

##=============================================================================

def temp_dir():
	"""Returns the TEMP_DIR from the .ini file"""
	return  conf['TEMP_DIR']
	

"""
def temp_file( file_name):
	return open( temp_dir() + file_name, "r")
	
def data_file(file_name):
	
	file_path = DATA_ROOT + file_name
	if os.path.exists(file_path):
		return None
	
	return open(file_path, "r")
"""
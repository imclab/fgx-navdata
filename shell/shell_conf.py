
import os
import sys

from paste.deploy import appconfig
from pylons import config


parent_path = os.path.abspath( os.path.join(os.path.dirname(__file__), "../") )
sys.path.append(parent_path + "/")  


if os.path.isfile(parent_path + "/LOCAL"):
	ini = parent_path + '/development.ini'
else:
	ini = parent_path + '/production.ini'


from fgx_ajax_server.config.environment import load_environment
conf = appconfig('config:' + ini)
load_environment( conf.global_conf, conf.local_conf)




#from pylons import config



def temp_dir():
	return conf['TEMP_DIR']
	
#TEMP_DIR = config['TEMP_DIR']
#print conf.keys()
#print config['pylons.environ_config']


def temp_file( file_name):
	return open( temp_dir() + file_name, "r")
	
def data_file(file_name):
	
	file_path = DATA_ROOT + file_name
	if os.path.exists(file_path):
		return None
	
	return open(file_path, "r")

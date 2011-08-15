#!/usr/bin/env python

import time
import datetime
import sys


import threading

import socket
import telnetlib
import memcache

MC = memcache.Client(['127.0.0.1:11211'])

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

## Thread to make it timeout after a few seconds instead of 30 secs ++
## http://stackoverflow.com/questions/492519/timeout-on-a-python-function-call
def timeout(func, args=(), kwargs={}, timeout_duration=10, default=None):
	"""This function will spawn a thread and run the given function
	using the args, kwargs and return the given default value if the
	timeout_duration is exceeded.
	""" 
	class InterruptableThread(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)
			self.result = default
		def run(self):
			self.result = func(*args, **kwargs)
	it = InterruptableThread()
	it.start()
	it.join(timeout_duration)
	if it.isAlive():
		return it.result
	else:
		return it.result
		

def lookup_server(server_domain):
	try:
		addr = socket.gethostbyname(server_domain) #, PORT)
		return addr

	except socket.gaierror as err:
		#print "  ERR=\t" , err # eg Host No Found
		return None
	

# Max number of servers to look
MAX_MPSERVER_ADDRESS = 20

## Payload to store in memcached
mp_info = {}
mp_info['last_start'] = datetime.datetime.now().strftime(DATE_FORMAT)
mp_info['servers'] = {}

for no in range(1, MAX_MPSERVER_ADDRESS + 1):
	server_name = "mpserver%02d.flightgear.org" % no
	#print server_name
	address = timeout(lookup_server, (server_name,), timeout_duration=5)
	print "--------------------------------\n", server_name, address
	
	if address != None:
		mp_info['servers'][server_name] = {'ip': address, 'last': None}
		
		try:
			conn = telnetlib.Telnet(server_name, 5001, 5)
			data = conn.read_all()
			lines = data.split("\n")
			#print lines[0]
			#print lines[1]
			#print lines[2]
			#print lines[3]
			#print lines[4]
			mp_info['servers'][server_name]['info'] = {	'info': lines[0],
												'version': lines[1],
												'tracked': lines[2],
												'pilots': lines[3],
												}
			mp_info['servers'][server_name]['last'] = time.mktime( datetime.datetime.utcnow().timetuple() )
			
		except 	socket.error as err:
			#print "err=", err
			pass
			
		

mp_info['last_end'] = datetime.datetime.now().strftime(DATE_FORMAT)
#print datetime.datetime.now()	
MC.set("mp_info", mp_info)


print "DONE"

sys.exit(0)

		
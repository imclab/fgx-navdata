#!/usr/bin/env python

import time
import datetime
import sys

import socket
import telnetlib

import shell_vars 


## Does a DNS loopkup of a server eg mpserver07
def lookup_server(server_name):

	server_domain = "%s.flightgear.org" % server_name
	try:
		addr = socket.gethostbyname(server_domain) #, PORT)		
		return addr

	except socket.gaierror as err:
		print "  DNS =\t" , server_name, err		
		return None
	


## Telnet connections
def get_telnet(address):
	try:
		conn = telnetlib.Telnet(address, 5001, 5)
		data = conn.read_all()
		lines = data.split("\n")
		conn.close()
		#print lines[0]
		#print lines[1]
		#print lines[2]
		#print lines[3]
		#print lines[4]
		return {'info': lines[0],
				'version': lines[1],
				'tracked': lines[2],
				'pilots': lines[3],
				'last': datetime.datetime.now().strftime(shell_vars.DATE_FORMAT)
				}
		
	except 	socket.error as err:
		print " telnet=", address, err
		#conn.close()
		return None
		


## Payload to store in memcached
mp_info = {}
mp_info['last_dns_start'] = datetime.datetime.now().strftime(shell_vars.DATE_FORMAT)
mp_info['servers'] = {}

## Loop range and lookup servers
for no in range(1, shell_vars.MAX_MPSERVER_ADDRESS + 1):
	
	server_name = "mpserver%02d" % no
	address = lookup_server(server_name)
	print "--------------------------------\n", server_name, address
	
	if address != None:
		mp_info['servers'][server_name] = {'ip': address, 'last': None}
		
		info = get_telnet(address) # server_name + ".flightgear.org")
		if info != None:
			mp_info['servers'][server_name]['info'] = info

		

mp_info['last_dns_end'] = datetime.datetime.now().strftime(shell_vars.DATE_FORMAT)

## Update Memcached
shell_vars.MC.set("mp_info", mp_info)

print "DONE", mp_info

sys.exit(0)

		
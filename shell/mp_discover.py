#!/usr/bin/env python

"""
pete@freeflightsim.org composed and knocked this up script for fgx update of mp

Purpose:
To be on a cron every minute and to update the memcache tree with the mpserver status.
why? 
> so one can update the server status into from here memcache 
> then other apps can query memcache.. and nothing to so with this script

How:
This script walks thought the domain 1 > shell_vars.MAX_MPSERVER_ADDRESS
it then chacks if the dns entry exists and its address or Null
it then connect to each server in telnet to gain latest data or null
Finally updates the memcache with the "mp_info"
job done :-)
"""

import time
import datetime
import sys

import socket
import telnetlib

import shell_vars 


from pprint import pprint


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
		tracked = "@ Not Tracked"
		if lines[2].find("tracked") != -1:
			tracked = lines[2]
			
		if lines[3].find("tracked") != -1:
			tracked = lines[3]
			
			
		pilots = "@ No Pilots"
		if lines[2].find("pilots") != -1:
			pilots = lines[2]
			
		if lines[3].find("pilots") != -1:
			pilots = lines[3]
		
		return {'info': lines[0],
				'version': lines[1],
				'tracked': tracked,
				'pilots': pilots
				}
		
	except 	socket.error as err:
		print " telnet=", address, err
		#conn.close()gr
		return None
		

def current_date_utc():
	return datetime.datetime.utcnow().strftime(shell_vars.DATE_FORMAT)

## Payload to store in memcached
#shell_vars.MC.set("mp_info", None)
mp_info = shell_vars.MC.get("mp_info")

#print mp_info
if mp_info == None:
	mp_info = {}
	mp_info['servers'] = {}	
	
mp_info['last_dns_start'] = current_date_utc()

## Loop range and lookup servers
for no in range(1, shell_vars.MAX_MPSERVER_ADDRESS + 1):
	
	server_name = "mpserver%02d" % no
	address = lookup_server(server_name)
	print "--------------------------------\n", server_name, address
	
	if address != None:
		if not mp_info['servers'].has_key(server_name):
			mp_info['servers'][server_name] = {'ip': address, 'last': None, 'info': None, 'fail': None}
		
		info = get_telnet(address) # server_name + ".flightgear.org")
		if info != None:
			mp_info['servers'][server_name]['info'] = info
			mp_info['servers'][server_name]['last'] = current_date_utc()
			mp_info['servers'][server_name]['fail'] = None # cancel a fail message
		else:
			if mp_info['servers'][server_name]['fail'] == None:
				## we only want the first fail
				mp_info['servers'][server_name]['fail'] = current_date_utc()
		

mp_info['last_dns_end'] = current_date_utc()

## Update Memcached
shell_vars.MC.set("mp_info", mp_info)

#print "DONE", mp_info
pprint(mp_info)

sys.exit(0)




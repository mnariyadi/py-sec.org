  1 #!/usr/bin/python
  2 
  3 #written for py-sec.org
  4 #cracking poverty with python
  5 
  6 import socket, sys
  7 
  8 
  9 
 10 def scanning_port(target_server):
 11 
 12         for port in range(20, 30):
 13                 try:
 14                         print "[+] Connecting to " + target_server + " port: " + str(port)
 15                         port_scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 16                         port_scanner.connect((target_server, port))
 17                         port_scanner.send("Hello world \n")
 18                         banner = port_scanner.recv(4096)
 19                         print "[+] Port %s open"%port
 20                         print "[+] Port banner: " + banner
 21                 except:pass
 22 
 23 def main():
 24 
 25         target_server = sys.argv[1]
 26         print "\n" + "Port scanning on progress .." + "\n"
 27         scanning_port(target_server)
 28         print "\n" + "Port scanning finished .." + "\n"
 29 
 30 if __name__ == main():
 31         main()
 32 

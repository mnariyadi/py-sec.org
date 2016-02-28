  1 #!/usr/bin/python
  2 # written for py-sec.org
  3 # ASIA Education Summit, February 23 - 26 2016, Bangkok
  4 # OUT OF SCHOOL CHILDREN
  5 
  6 import socket
  7 import sys
  8 
  9 
 10 def client(targetHost):
 11         tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 12         port = 80
 13         tcpClient.connect((targetHost, port))
 14         tcpClient.send("GET / HTTP/1.1\r\nHost:%s"%targetHost+"\r\n\r\n")
 15         response = tcpClient.recv(4096)
 16         print "=============================================================    ="
 17         print "Header %s adalah: "%targetHost
 18         print "=============================================================    ="
 19         print "\n" + response
 20 
 21 def main():
 22         targetServer = open("webserver","r")
 23         for server in targetServer.readlines():
 24                 targetHost = server.strip("\n")
 25                 client(targetHost)
 26 
 27 if __name__ == main():
 28         main()

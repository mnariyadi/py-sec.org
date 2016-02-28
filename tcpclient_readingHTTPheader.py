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
 11         targetPort = 80
 12         tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 13         tcpClient.connect((targetHost, targetPort))
 14         tcpClient.send("GET / HTTP/1.1\r\nHost:%s"%targetHost+"\r\n\r\n")
 15         response = tcpClient.recv(4096)
 16         print "=============================================================="
 17         print "Header Web Server %s adalah: "%(targetHost)
 18         print "=============================================================="
 19         print "\n" + response
 20 
 21 def main():
 22 
 23         if len(sys.argv) != 2:
 24                 print "\n" + "<script> <Hostname web server>"
 25                 print "Harap masukkan target web server" + "\n"
 26                 sys.exit(1)
 27         targetHost = sys.argv[1]
 28         client(targetHost)
 29 
 30 if __name__ == main():
 31         main()
                         
                                                                                                                                                              
  1 #!/usr/bin/python
  2 # written for py-sec.org
  3 # cracking poverty with python 
  4 
  5 import socket
  6 
  7 def udpclient(udpserver, port):
  8 
  9         client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 10         message = "Hello world"
 11         print "Mengirim data: Hello world" + " ke port: " + str(port)dapun s    cript secara singkat adalah sebagaimana gambar berikut:
 12         client.sendto(message, (udpserver, port))
 13 
 14 
 15 def main():
 16         udpserver = "127.0.0.1"
 17         port = 10000
 18         udpclient(udpserver, port)
 19 
 20 
 21 
 22 if __name__ == main():
 23         main()

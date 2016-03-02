  1 #!/usr/bin/python
  2 # written for py-sec.org
  3 # cracking poverty with python
  4 
  5 import socket
  6 
  7 def udpserver(server, port):
  8         while True:
  9                 udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 10                 udpserver.bind((server, port))
 11                 print "\n" + "Mendengar pada port: " + str(port) + "\n"
 12                 data, address = udpserver.recvfrom(4096)
 13                 print "Menerima koneksi dari " + str(address[0]) + " port: " + str(    address[1])
 14                 print "Data: " + str(data)
 15 
 16 
 17 def main():
 18         server = "127.0.0.1"
 19         port = 10000
 20         udpserver(server, port)
 21 
 22 if __name__ == main():
 23         main() 

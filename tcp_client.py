  1 #!/usr/bin/python
  2 #written for py-sec.org
  3 #cracking poverty with python
  4 
  5 import socket
  6 
  7 def main():
  8         target_server = "127.0.0.1"
  9         target_port = 9999
 10 
 11         # Membuat socket object
 12         tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 13 
 14         # Menghubungi mesin server
 15         tcp_client.connect((target_server, target_port))
 16 
 17         # Mengirimkan data
 18         #tcp_client.send("GET / HTTP/1.1\r\nHost:localhost\r\n\r\n")
 19         tcp_client.send("Hello world ... ")
 20         # Menerima data dari server
 21         server_response = tcp_client.recv(4096)
 22 
 23         # Mencetak server response ke layar
 24         print server_response
 25 
 26 if __name__ == main():
 27         main()
~                                           
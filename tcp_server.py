  1 #!/usr/bin/python
  2 #written for py-sec.org
  3 #cracking poverty with python
  4 
  5 import socket
  6 import threading
  7 
  8 # Membuat thread untuk beberapa koneksi dengan client
  9 def client_thread(client_request):
 10 
 11         # 05.a.Menampilkan data dari client
 12         request = client_request.recv(1024)
 13         print "[+] Menerima: %s"%request
 14 
 15         # 05.b.Mengirim konfirmasi ke client
 16         client_request.send("ACK!")
 17 
 18         # 05.c.Menutup komunikasi setelah data diterima
 19         client_request.close()
 20 
 21 def main():
 22 
 23         ip_server = "127.0.0.1"
 24         ip_port = 9999
 25 
 26         # 01. Membuat socket object
 27         tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 28 
 29         # 02.Menghubungkan socket address dengan socket object
 30         tcp_server.bind((ip_server, ip_port))
 31 
 32         # 03. Mendengarkan permintaan client
 33         tcp_server.listen(5)
 34         print "[+] Mendengarkan client request pada %s:%d"%(ip_server,ip_port)
 35 
 36         while True:
 37 
 38                 # 04. Menerima client request
 39                 client_request, address =  tcp_server.accept()
 40                 print "[+] menerima client request dari: %s:%d"%(address[0], address[1])
 41 
 42                 # 05. Mengolah client request dengan thread
 43                 request_handler = threading.Thread(target=client_thread, args=(client_request,))
 44                 request_handler.start()
 45 
 46 if __name__ == main():
 47         main()
 48 
 49 
                                                                                                                                                                  24,15-22      All

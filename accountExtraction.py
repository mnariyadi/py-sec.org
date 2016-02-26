#!/usr/bin/python

def main():

	userAccount = open("shadow","r")                      # Membaca file pada /etc/shadow     

	counter = 1

	print "\n" + "Account yang akan di crack adalah :"

	for line in userAccount.readlines():                  # Memilah setiap account pada /etc/shadow

		line = line.replace("\n","").split(":")       # Membuat sembilan kolom 

		if not line[1] in ['*', '!','x']:             # Hanya memilih account tanpa karakter *, ! dan x
			user = line[0]			      # Memilih user account atau field pertama
			cryptPass = line[1]                   # Memilih hash dari user account atau field keduas
			print "\n" + "Account ke - %s"%counter
			print "[+] user : " + user
			print "[+] hash : " + cryptPass

		counter += 1

	print "\n"
	

if __name__ == main():
	main()

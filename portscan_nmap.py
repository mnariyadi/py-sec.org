  3 # cracking poverty with python
  4 
  5 import nmap, sys
  6 
  7 def nmapScanning (targetServer, targetPort):
  8 
  9         nmapScanner = nmap.PortScanner()
 10         nmapScanner.scan(targetServer, targetPort, '-sS')
 11         portState = nmapScanner[targetServer]['tcp'][int(targetPort)]['state    ']
 12         print " [+] " + targetServer + " , port %s status: "%targetPort + po    rtState
 13         print " [+] " + "Service: " + nmapScanner.csv()
 14 
 15 
 16 
 17 
 18 def main():
 19 
 20         targetServer = sys.argv[1]
 21         print "\n" + "[*] Port scanning on progress .." + "\n"
 22         for targetPort in range(21, 26):
 23                 nmapScanning(targetServer, str(targetPort))
 24         print "\n" + "[*] Port scanning finished .." + "\n"
 25 
 26 
 27 if __name__ == main():
 28         main()
 29 

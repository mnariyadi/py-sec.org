  3 # cracking poverty with python
  4 
  5 import nmap
  6 import optparse
  7 
  8 def targetSelection(subNet):
  9 
 10         nmapScanner = nmap.PortScanner()
 11         nmapScanner.scan(subNet, '445')
 12         targetHost = []
 13         for host in nmapScanner.all_hosts():
 14                 if nmapScanner[host].has_tcp(445):
 15                         state = nmapScanner[host]['tcp'][445]['state']
 16                         if state == 'open':
 17                                 print '[+] Found Target Host: ' + host
 18                                 targetHost.append(host)
 19 
 20 def main():
 21 
 22         parser = optparse.OptionParser('[*] Usage: script' + ' -H <Range of     Targets> ' )
 23         parser.add_option('-H', dest='targetHost', type='string', help='spec    ify range of target')
 24         (options, args) = parser.parse_args()
 25         if options.targetHost == None:
 26                 print parser.usage
 27                 exit(0)
 28 
 29 
 30         print "\n" + "Conficker target selection is in progress ... " + "\n"
 31         targetHost = targetSelection(options.targetHost)
 32         print "\n" + "Conficker target selection is finished .." + "\n"
 33 
 34 
 35 if __name__ == main():
 36         main()

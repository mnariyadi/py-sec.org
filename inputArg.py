  1 #!/usr/bin/python
  2 # written for py-sec.org
  3 # ASIA Education Summit, February 23 - 26, 2016
  4 # OUT OF SCHOOL CHILDREN
  5 
  6 
  7 import sys
  8 
  9 if len(sys.argv) != 4:
 10         print "\n" + "Need argument: " + sys.argv[0] + " <host> " + "<IP Addr> " + "<port> " + "\n"
 11         sys.exit(1)
 12 
 13 print "\n" + "Relative path of script: ", sys.argv[0]
 14 print "Jumlah argument: ", len(sys.argv)
 15 print "Argument-nya: ", str(sys.argv), "\n"
 16 
 17 serverName = sys.argv[1]
 18 serverIP = sys.argv[2]
 19 serverPort = sys.argv[3]
 20 
 21 print "Server Name: ", serverName
 22 print "Server IP  : ", sys.argv[2]
 23 print "Server Port:", sys.argv[3] + "\n"
 24 
~                                                                                                                                                                                                                                                                                                 
                                                                                                                          
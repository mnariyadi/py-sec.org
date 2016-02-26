#!/usr/bin/python


import ftplib
import threading
import Queue

class ftpscan(threading.Thread):

	def __init__(self,queue,lock):
		threading.Thread.__init__(self)
		self.queue = queue
		self.lock = lock

	def run(self):
		while True:
			self.lock.acquire()
			self.queue.get()
			#ftpclient = ftplib.FTP(ftpserver.strip())
			self.queue.task_done()
			self.lock.release()



def main():

	queue = Queue.Queue()
	lock = threading.Lock()
	ftplist = open("ftpsites","r")
	counter = 1

	for tid in range(5):
		print "Creating FTPSCAN Thread: %d"%tid
		ftpscan_Thread = ftpscan(queue,lock)
		ftpscan_Thread.setDaemon(True)
		ftpscan_Thread.start()
		print "FTPSCAN Thread %d created"%tid
	
	
	for ftpserver in ftplist.readlines():
		ftp = ftplib.FTP(ftpserver.strip())
		queue.put(ftpserver.strip())
		print "------------------------------------------------------------------------------"
		print "<%d> FTP Server: "%counter + ftpserver.strip()
		print "------------------------------------------------------------------------------"
		ftp.login()
		ftp.retrlines('LIST')
		ftp.quit()
		queue.join()
		print "------------------------------------------------------------------------------"
		print "Listing directory at FTP Server: " + ftpserver.strip() + " finished"
		print "------------------------------------------------------------------------------" + "\n"
		counter += 1

if __name__ == main():
	main()



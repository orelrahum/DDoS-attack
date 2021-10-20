import subprocess
import numpy as np
import sys

arr = []
ipaddress = '10.0.0.18'  # guess who
with open("pings-python.txt", 'w+')as f:
    f.write("pings:")
f.close()
while (True):
	proc = subprocess.Popen(['ping', '-c1', ipaddress],
                        stdout=subprocess.PIPE)
	stdout, stderr = proc.communicate()

	if proc.returncode == 0:
    		s = (stdout)
	for line in s.split(" "):
    		if "time=" in line:
			d=float(line.split("=")[1])
			with open("pings-python.txt", 'a+')as f:
    				f.write(`d`+",")
			f.close()


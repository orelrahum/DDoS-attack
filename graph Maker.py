from matplotlib import pyplot
import numpy as np
def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

bins=list(frange(0,500,50))
ping=[]
with open("c-results.txt") as p:
	a=p.readline()
b=a.split(",")

for line in b:
	ping.append(float(str(line)))

print(np.mean(ping))
ping.sort()
size=len(ping)
print(size)
pyplot.figure(figsize=(10,10),facecolor='white',dpi = (80))

pyplot.hist(ping, bins, alpha=1, histtype='bar',edgecolor='black', stacked=True)#query host
pyplot.legend(loc='upper right',prop={'size': 24})
pyplot.yscale('log')
pyplot.title("Ping of C",fontsize=20)
#pyplot.yticks(fontsize=20)
#pyplot.xticks(tick,rotation=90,fontsize=20)
pyplot.ylabel("Number of hits", fontsize=20)
pyplot.xlabel("Milliseconds", fontsize=20)
pyplot.show()


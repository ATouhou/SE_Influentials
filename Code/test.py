import heapq
import csv

h = []
heapq.heappush(h,(10, 1200131))
heapq.heappush(h,(20, 31))
heapq.heappush(h,(5, 111111111111111111))


#print heapq.nlargest(1,h)

#print heapq.heappushpop(h,(1,231))
#print p[1]

fr = open('list.csv','r')
csv1 = csv.reader(fr,delimiter='\t')

for row in csv1:
	print row[0]

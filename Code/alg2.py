import heapq
import csv
import operator

h = []

fr = open('list.csv','r')
csv1 = csv.reader(fr,delimiter='\t')
f = open('following/top19.csv', "wb")
for row in csv1:
	fname = row[0]
	sample = open(fname,'r')
	csv11 = csv.reader(sample,delimiter='\t')
	for row in csv11:
		heapq.heappush(h,(-(int(row[3])),row[1]))
	sample.close()


for x in range(0,55):
	p = heapq.heappop(h)
	params = (p[1],-p[0])
	f.write('%s\t%s\n' % params)



f.close()



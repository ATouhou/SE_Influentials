import csv

excl = {}
exclude = open('top200.csv','r')
csvex = csv.reader(exclude,delimiter='\t')
for row in csvex:
	excl[row[0]] = 1

excl1 = {}
exclude1 = open('ans.csv','r')
csvex1 = csv.reader(exclude1,delimiter='\t')
for row in csvex1:
	if not excl.has_key(row[0]):
		print row[0]


"""
import sys, csv ,operator
sam = open('pvn251.csv','r')
data = csv.reader(sam,delimiter='\t')
sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort
      #now write the sorte result into new CSV file
with open("pvn251.csv", "wb") as f:
   fileWriter = csv.writer(f, delimiter='\t')
for row in sortedlist:
	fileWriter.writerow(row)
"""






import csv
import operator

sample = open('icse2015.csv','r')
csv1 = csv.reader(sample,delimiter='\t')
for row in csv1:
	print row[1]
#sort = sorted(csv1,key = operator.itemgetter(3))

#sort = sorted(csv1,key = lambda row: float(row[3]),reverse = True)

#f = open("pvn251.csv", "wb")
#fileWriter = csv.writer(f, delimiter='\t')
#for row in sort:
#	fileWriter.writerow(row)

sample.close()


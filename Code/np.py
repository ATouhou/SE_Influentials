import csv
import os

'''
for file in os.listdir("following"):
	if file.endswith(".csv"):
		print(file)

lat = open('following/anildaash.csv','r')
csvlat = csv.reader(lat,delimiter='\t')


for row in csvlat:
	fname = os.path.join('users', row[0] + '.csv')
	f = open(fname,"wb")
	#print row[2]
	params = (row[1],row[3])
        f.write('%s\t%s\n' % params)

'''

f = open('record.csv',"a")
lat = open('following/vps5495.csv','r')
f.write(lat.read())

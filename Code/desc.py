import tweepy
import csv
'''
import io
f = io.open('Description.csv',"w",encoding='utf8')
'''

CONSUMER_KEY =         'dKFZqHB8FyNi2ebbFjQGFPmkr'
CONSUMER_SECRET =      'wfj09vfMfAVFdYS6iy3rVYY546GUXn4KhLgE5EbCjGkfTzF7kC'
ACCESS_TOKEN   =       '3220731312-SlujZpUvkJ4Q0ltlVAD82WBPeTSQUOlJwPN5VR3'
ACCESS_TOKEN_SECRET =   'YJKquEf4SwuZHyspdkie3Vt87H5VwkTK6uVmby5logt1A'

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

lat = open('Results/top10p11.csv','r')
csvlat = csv.reader(lat,delimiter='\t')


f = open('Description.csv',"wb")
for row in csvlat:
	user = api.get_user(row[0])	
	print row[0]
	params = (user.name,user.description,user.url)
	f.write('%s\t%s\t%s\n' % params)

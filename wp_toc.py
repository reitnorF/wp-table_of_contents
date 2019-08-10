import urllib2
from bs4 import BeautifulSoup
import pickle
import requests
from requests.exceptions import HTTPError

#Change this to suits your needs
uri = "https://targetsite.wordpress.com/"
start_year = 2012
end_year = 2019

listofAll = list()
stop = False
anchor = 0
listofURL = list()
listofTitle = list()

for year in range(start_year,end_year+1):
	num = 1
	stop = False
	while not stop:
		print str(year) + str(num)
		now_uri = uri + str(year) +"/page/" + str(num)	
		try:
			pagereq = urllib2.Request(now_uri)
			page = urllib2.urlopen(now_uri)
		except urllib2.HTTPError, e:
			if e.code == 404:
				print "Done"
				stop = True
		if not stop:
			soup = BeautifulSoup(page,'html.parser')
			name = soup.find_all('h1', attrs={'class':'entry-title'})
			for i in name:
				judul = i.text.strip()
				link = i.find_all('a')
				for tag in link:
					postlink = tag.get('href')
					print judul + "   |||   " + postlink
			num += 1

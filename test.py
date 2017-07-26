import requests
import json
from bs4 import BeautifulSoup

# set url to be scraped
sb_url="https://www.yellowpages.com/search?search_terms=star+bucks&geo_location_terms=miami" 

#get the html for the url by sending a request into sb_get.content 
sb_get = requests.get(sb_url)

#soupify using BS4
sb_soup = BeautifulSoup(sb_get.content)

#find all a tags in sb_soup
#sb_link = sb_soup.find_all("a")

#for all link aka a in sb_link list
#for link in sb_link: 
#	     print "<a href='%s'>%s</a>" %(link.text, link.get("href"))

#find all div class info
sb_info = sb_soup.find_all("div", {"class": "info"})	   

for item in sb_info:
	print item.contents[0].find_all("a", {"class": "business-name"})[0].text
	try:
		print item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
	except:
	    pass	
	try:
		print item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replace(',','').replace('\n','').replace('\r','').replace('\r\n','')
	except:
	    pass	
	try:
		print item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text
	except:
	    pass	
	try:
		print item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
	except:
	    pass	
	try:
		print item.contents[1].find_all("div", {"class": "phones"})[0].text
	except:
		pass




print "hello,world"
print "test again"


import requests
from bs4 import BeautifulSoup

#set url to be scraped
scrape_url="https://www.youtube.com"
search_url="/results?search_query="
search_hardcode = "game+of+thrones"
mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}



def bstheurl():
        sb_url = scrape_url + search_url + search_hardcode
        sb_get = requests.get(sb_url, headers = mozhdr)
        soupeddata = BeautifulSoup(sb_get.content, "html.parser")
        yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
        for x in yt_links:
            yt_href =  x.get("href")
            yt_title = x.get("title")
            yt_final = scrape_url + yt_href
            print yt_final
            print yt_title
            

bstheurl()

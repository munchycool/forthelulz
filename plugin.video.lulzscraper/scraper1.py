import requests
from bs4 import BeautifulSoup
import json
import sys,urllib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin


# Get the plugin url in plugin:// notation.
addon_url = sys.argv[0]
# Get the plugin handle as an integer number.
addon_handle = int(sys.argv[1])

addon = xbmcaddon.Addon('plugin.video.lulzscraper')
addon_name   = addon.getAddonInfo('name') #get addon name
addon_icon   = addon.getAddonInfo('icon') #get addon icon
addon_id     = addon.getAddonInfo('id') # Grab our add-on id
home_folder  = xbmc.translatePath('special://home/')# Convert the special path of Kodi home folder to the physical path


#set url to be scraped
#sb_url="https://einthusan.tv/movie/results/?lang=hindi&query=rock%20on" 
base_url="https://einthusan.tv"
search_url="/movie/results/?lang=hindi&query="
search_string = "rock%20on"


def bstheurl():
	sb_url = base_url + search_url + search_string
	sb_get = requests.get(sb_url)
	soupeddata = BeautifulSoup(sb_get.content, "html.parser")
	return soupeddata

#find all div class block2
#	print "top-con"
#	print "<a href='%s'>%s</a>" %(item.text, item.get("href"))
#	print "top-con-end"
#find all links in sb_info
#sb_links = sb_soup.find_all("a", {"class": "title"})
#loop for link
#for link in sb_links:
#	print link.get('href')"""

vid_list = []
def findtheshit(sb_soup):
	sb_info = sb_soup.find_all("div", {"class": "block2"})	 
#	vid_list = []
	for item in sb_info:
		vid_details = gettheshit(item)
		vid_list.append(vid_details)
	return vid_list

def gettheshit(vidstuff):	
	video_details = []
	try:	
		vid_url       =  json.dumps(vidstuff.contents[0].get("href").replace('\n', '').replace('\t', '').lstrip())
		video_details.append(vid_url)
		vid_name      =  json.dumps(vidstuff.contents[0].find("h3").contents[0].replace('\t', '').lstrip())
		video_details.append(vid_name)
	except:
		pass
	try:		
		vid_language  =  json.dumps(vidstuff.contents[1].find("p").contents[0].replace('\t', '').lstrip())
		video_details.append(vid_language)
		vid_year      =  json.dumps(vidstuff.contents[1].find("span").contents[0].replace('\t', '').lstrip())
		video_details.append(vid_year)
		vid_quality   =  json.dumps(vidstuff.contents[1].find("i").get("class")).replace('\n','')
	except:
		pass
#	video_details.append(vid_url).append(vid_name).append(vid_language).append(vid_year)
#	video_details = vid_url + "," + vid_name + "," + vid_language + "," + vid_year
#	print video_details
	return (video_details)

def buildMenu():
    addMenuItem(params['title'], link, 'icon.png', params['image'], False)
    endListing()



def dequote(s):
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

def makeLink(params):
	return base_url + params

def addMenuItem(caption, link, icon=None, thumbnail=None, folder=False):
    """
    Add a menu item to the xbmc GUI
    
    Parameters:
    caption: the caption for the menu item
    icon: the icon for the menu item, displayed if the thumbnail is not accessible
    thumbail: the thumbnail for the menu item
    link: the link for the menu item
    folder: True if the menu item is a folder, false if it is a terminal menu item
    
    Returns True if the item is successfully added, False otherwise
    """
    listItem = xbmcgui.ListItem(unicode(caption), iconImage=icon, thumbnailImage=thumbnail)
    listItem.setInfo(type="Video", infoLabels={ "Title": caption })
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link, listitem=listItem, isFolder=folder)

def endListing():
    """
    Signals the end of the menu listing
    """
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

def playMedia(title, thumbnail, link, mediaType='Video') :
    """Plays a video

    Arguments:
    title: the title to be displayed
    thumbnail: the thumnail to be used as an icon and thumbnail
    link: the link to the media to be played
    mediaType: the type of media to play, defaults to Video. Known values are Video, Pictures, Music and Programs
    """
    li = xbmcgui.ListItem(label=title, iconImage=thumbnail, thumbnailImage=thumbnail, path=link)
    li.setInfo(type=mediaType, infoLabels={ "Title": title })
    xbmc.Player().play(item=link, listitem=li)


def traversevislist(videolist):
#	print videolist
	for x in videolist:
#		print x
		movie_url = makeLink(dequote(x[0]))
#		print movie_url
		movie_name = dequote(x[1])
#		print movie_name
#		for y in x:
#			print y
	return movie_url

einthusian_html = bstheurl()
list_of_videos = findtheshit(einthusian_html)
final_url=traversevislist(list_of_videos)

playMedia("Rock",addon_icon,final_url)


#print "hello,world"
#print "test again"

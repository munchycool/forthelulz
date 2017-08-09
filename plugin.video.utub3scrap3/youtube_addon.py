import sys
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import urllib
import urlparse
import urlresolver
import requests
from bs4 import BeautifulSoup


base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

# set url to be scraped
scrape_url = "https://www.youtube.com"
search_url = "/results?search_query="
mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}


def build_url(query):
    return base_url + '?' + urllib.urlencode(query)


def getusersearch(website):
    kb = xbmc.Keyboard('default', 'heading')
    kb.setDefault('Enter Search Word')
    kb.setHeading(website + 'Search')
    kb.setHiddenInput(False)
    kb.doModal()
    if (kb.isConfirmed()):
        search_term = kb.getText()
        return(search_term)
    else:
        return


def addMenuitem(url, li, folder):
    return xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=folder)


def endMenu():
    xbmcplugin.endOfDirectory(addon_handle)


def bstheurl(url):
    sb_get = requests.get(url, headers=mozhdr)
    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
    yt_links = soupeddata.find_all("a", class_="yt-uix-tile-link")
    for x in yt_links:
        yt_href = x.get("href")
        yt_title = x.get("title")
        yt_final = scrape_url + yt_href        
        url = build_url({'mode': 'play', 'playlink': yt_final})
        li = xbmcgui.ListItem(yt_title, iconImage='DefaultVideo.png')
        li.setProperty('IsPlayable', 'true')
        addMenuitem(url, li, False)
    endMenu()


def resolve_url(url):
    duration = 7500  # in milliseconds
    message = "Cannot Play URL"
    stream_url = urlresolver.HostedMediaFile(url=url).resolve()
    # If urlresolver returns false then the video url was not resolved.
    if not stream_url:
        dialog = xbmcgui.Dialog()
        dialog.notification("URL Resolver Error", message,
                            xbmcgui.NOTIFICATION_INFO, duration)
        return False
    else:
        return stream_url


def play_video(path):
    """
    Play a video by the provided path.
    :param path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    vid_url = play_item.getfilename()
    stream_url = resolve_url(vid_url)
    if stream_url:
        play_item.setPath(stream_url)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)


mode = args.get('mode', None)

if mode is None:
    url = build_url({'mode': 'search', 'site': 'youtube'})
    li = xbmcgui.ListItem('Youtube Search', iconImage='DefaultFolder.png')
    addMenuitem(url, li, True)
    endMenu()

elif mode[0] == 'search':
    website = args['site'][0]
    search_string = getusersearch(website)
    yotube_search_url = scrape_url + search_url + \
        search_string.replace(" ", "+")
    xbmcplugin.setContent(addon_handle, 'movies')
    bstheurl(yotube_search_url)

elif mode[0] == 'play':
    final_link = args['playlink'][0]
    play_video(final_link)

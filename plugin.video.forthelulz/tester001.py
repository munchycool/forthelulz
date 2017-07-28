import urlparse
import requests
from bs4 import BeautifulSoup
import json
import sys,urllib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urlresolver



base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
_addon = xbmcaddon.Addon()
_addonname = _addon.getAddonInfo('name')
_icon = _addon.getAddonInfo('icon')


def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def resolve_url(url):
    duration=7500   
    try:
        stream_url = urlresolver.HostedMediaFile(url=url).resolve()
        # If urlresolver returns false then the video url was not resolved.
        if not stream_url or not isinstance(stream_url, basestring):
            try: msg = stream_url.msg
            except: msg = url
            xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('URL Resolver',msg, duration, _icon))
            return False
    except Exception as e:
        try: msg = str(e)
        except: msg = url
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('URL Resolver',msg, duration, _icon))
        return False
        
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
    print "in play video"
    print play_item
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

# addon kicks in

mode = args.get('mode', None)


if mode is None:
    # video_play_url = "http://justmoviesonline.com/playh.php?id=5969a9bc048e740290fa7866"
    video_play_url = "https://drive.google.com/file/d/0BzZ_8k1jNVGILUktQjdEQ0lkS00/preview"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Play Video', iconImage='DefaultVideo.png')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'play':
    final_link = args['playlink'][0]
    print "in mode play"
    print final_link
    play_video(final_link)






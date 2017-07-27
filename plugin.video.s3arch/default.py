import sys
import xbmcgui
import xbmcplugin
import xbmc
import urllib
import urlparse

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
# xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def getusersearch(language):
    kb = xbmc.Keyboard('default', 'heading')
    kb.setDefault('Enter Search Word')
    kb.setHeading(language + 'Search')
    kb.setHiddenInput(False)
    kb.doModal()
    if (kb.isConfirmed()):
        search_term  = kb.getText()
        return(search_term)
    else:
        return

mode = args.get('mode', None)


if mode is None:
    url = build_url({'mode': 'search', 'language': 'Hindi'})
    li = xbmcgui.ListItem('Hindi Search', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    url = build_url({'mode': 'search', 'language': 'English'})
    li = xbmcgui.ListItem('English Search', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'search':
    language = args['language'][0]
    search_string = getusersearch(language)
    xbmcplugin.setContent(addon_handle, 'movies')
    if language == 'Hindi':
        url = 'http://www.vidsplay.com/wp-content/uploads/2017/04/alligator.mp4'
        li = xbmcgui.ListItem(search_string + ' Video', iconImage='DefaultVideo.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)
    elif language == 'English':
        url = 'http://www.vidsplay.com/wp-content/uploads/2017/04/alligator.mp4'
        li = xbmcgui.ListItem(search_string + ' Video', iconImage='DefaultVideo.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)


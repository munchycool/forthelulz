import urlparse
import sys,urllib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin



base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])


def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def play_video(path):
    """
    Play a video by the provided path.
    :param path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    vid_url = play_item.getfilename()
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

# addon kicks in

mode = args.get('mode', None)


if mode is None:
    video_play_url = "http://www.vidsplay.com/wp-content/uploads/2017/04/alligator.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Play Video 1', iconImage='DefaultVideo.png')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

    video_play_url = "https://www.youtube.com/watch?v=J9d9UrK0Jsw"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Play Video 2', iconImage='DefaultVideo.png')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

    xbmcplugin.endOfDirectory(addon_handle)


elif mode[0] == 'play':
    final_link = args['playlink'][0]
    play_video(final_link)






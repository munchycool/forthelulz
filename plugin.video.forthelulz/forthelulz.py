# -*- coding: utf-8 -*-
# Module: forthelulz
# Author: munchycool.
# Created on: 20.12.2020
# License: forthelulz

import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import forthelulzfunctions
import urlresolver


# Get the plugin url in plugin:// notation.
addon_url = sys.argv[0]
# Get the plugin handle as an integer number.
addon_handle = int(sys.argv[1])

addon = xbmcaddon.Addon('plugin.video.forthelulz')
addon_name   = addon.getAddonInfo('name') #get addon name
addon_icon   = addon.getAddonInfo('icon') #get addon icon
addon_id     = addon.getAddonInfo('id') # Grab our add-on id
home_folder  = xbmc.translatePath('special://home/')# Convert the special path of Kodi home folder to the physical path



# 001 - code in file forthelulzfunctions.py now as a function
#li = xbmcgui.ListItem(label=addon_title, iconImage=addon_icon, thumbnailImage=addon_icon, path=link)
#li.setInfo(type='Video', infoLabels={ "Title": addon_title})
#li.setProperty('IsPlayable','true')
#xbmc.Player().play(item=link, listitem=li)
# end 001

def resolve_url(url):
    duration=7500   
    try:
        stream_url = urlresolver.HostedMediaFile(url=url).resolve()
        # If urlresolver returns false then the video url was not resolved.
        if not stream_url or not isinstance(stream_url, basestring):
            try: msg = stream_url.msg
            except: msg = url
            xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('URL Resolver',msg, duration, addon_icon))
            return False
    except Exception as e:
        try: msg = str(e)
        except: msg = url
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('URL Resolver',msg, duration, addon_icon))
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


# 002 start
#link = "http://www.vidsplay.com/wp-content/uploads/2017/04/alligator.mp4"
link = "https://drive.google.com/file/d/0BzZ_8k1jNVGILUktQjdEQ0lkS00/preview"
# link = "http://justmoviesonline.com/playh.php?id=5969a9bc048e740290fa7866"
play_video(link)
# forthelulzfunctions.playMedia(addon_name,addon_icon,link)
# 002 end

#003 test dialog
#xbmcgui.Dialog().ok(addon_name, addon_id,home_folder)
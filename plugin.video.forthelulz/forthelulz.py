# -*- coding: utf-8 -*-
# Module: forthelulz
# Author: munchycool.
# Created on: 20.12.2020
# License: forthelulz

import xbmc
import xbmcgui
import xbmcaddon
import forthelulzfunctions

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


# 002 start
link = "http://www.vidsplay.com/wp-content/uploads/2017/04/alligator.mp4"
forthelulzfunctions.playMedia(addon_name,addon_icon,link)
# 002 end

#003 test dialog
#xbmcgui.Dialog().ok(addon_name, addon_id,home_folder)
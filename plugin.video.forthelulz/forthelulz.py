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
addon_title = addon.getAddonInfo('name')
addon_icon = addon.getAddonInfo('icon')

link = "http://www.vidsplay.com/wp-content/uploads/2017/04/alligator.mp4"

#li = xbmcgui.ListItem(label=addon_title, iconImage=addon_icon, thumbnailImage=addon_icon, path=link)
#li.setInfo(type='Video', infoLabels={ "Title": addon_title})
#li.setProperty('IsPlayable','true')

#xbmc.Player().play(item=link, listitem=li)

forthelulzfunctions.playMedia(addon_title,addon_icon,link)

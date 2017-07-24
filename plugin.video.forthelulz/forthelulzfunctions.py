# -*- coding: utf-8 -*-
# Module: forthelulz
# Author: munchycool.
# Created on: 20.12.2020
# License: forthelulz

# file for functions, forthelulzfunctions.py

import xbmcgui
import xbmc

#function to play a media. 4 parameters with mediaType hardcoded as video
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
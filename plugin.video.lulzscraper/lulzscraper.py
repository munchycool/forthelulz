# -*- coding: utf-8 -*-
# Module: lulzscraper
# Author: munchycool.
# Created on: 20.12.2020
# License: lulzscraper

import xbmc
import xbmcgui
import xbmcaddon
import lulzscraperfunctions
import urllib2


# Get the plugin url in plugin:// notation.
addon_url = sys.argv[0]
# Get the plugin handle as an integer number.
addon_handle = int(sys.argv[1])

addon = xbmcaddon.Addon('plugin.video.lulzscraper')
addon_name   = addon.getAddonInfo('name') #get addon name
addon_icon   = addon.getAddonInfo('icon') #get addon icon
addon_id     = addon.getAddonInfo('id') # Grab our add-on id
home_folder  = xbmc.translatePath('special://home/')# Convert the special path of Kodi home folder to the physical path
scrape_url = 'http://www.entv.dz/tvfr/video/'


def playVideo(params):
    response = urllib2.urlopen(params['video'])
    if response and response.getcode() == 200:
        content = response.read()
        videoLink = lulzscraperfunctions.extract(content, 'flashvars.File = "', '"')
        lulzscraperfunctions.playMedia(params['title'], params['image'], videoLink, 'Video')
    else:
        lulzscraperfunctions.showError(addon_id, 'Could not open URL %s to get video information' % (params['video']))
    
def buildMenu():
    url = scrape_url + 'index.php'
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        videos = lulzscraperfunctions.extractAll(content, '<td align="left">', '/td>')
        for video in videos:
            params = {'play':1}
            params['video'] = scrape_url + lulzscraperfunctions.extract(video, 'a href="', '\"')
            params['image'] = scrape_url + lulzscraperfunctions.extract(video, 'img src="', '\"')
            params['title'] = lulzscraperfunctions.extract(video, '</a>', '<') + ' (%s)' % (u'Fran\u00e7ais' if '19H' in params['video'] else 'Arabe')
            link = lulzscraperfunctions.makeLink(params)
            lulzscraperfunctions.addMenuItem(params['title'], link, 'DefaultVideo.png', params['image'], False)
        lulzscraperfunctions.endListing()
    else:
        lulzscraperfunctions.showError(addon_id, 'Could not open URL %s to create menu' % (url))


parameters = lulzscraperfunctions.parseParameters()
if 'play' in parameters:
    playVideo(parameters)
else:
    buildMenu()

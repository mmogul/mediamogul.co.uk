#Youtube channels
#
#
#
#
#
#Husham with Ryan reggae n dancehall music Addon
import re
import os
import sys
import urllib2
import buggalo
import xbmcgui
import xbmcaddon
import xbmcplugin

BASE_URL = 'http://www.gametest.dk/'
PLAY_VIDEO_PATH = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'
PLAYLIST_PATH = 'plugin://plugin.video.youtube/user/AkamEntertainments/'
PLAYLIST_PATH2 = 'plugin://plugin.video.youtube/user/TheReggaeselecta/'
PLAYLIST_PATH3 = 'plugin://plugin.video.youtube/channel/UC7_aGyrvwh5TBZvyleQ97pw/'

if __name__ == '__main__':
    ADDON = xbmcaddon.Addon()
    HANDLE = int(sys.argv[1])

    try:
        u = urllib2.urlopen(BASE_URL)
        html = u.read()
        u.close()


        m = re.search('//www.youtube.com/embed/([^"]+)"', html, re.DOTALL)
        if m:
            item = xbmcgui.ListItem('Reggae n Dancehall music',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-wQ8woE0PkAM/AAAAAAAAAAI/AAAAAAAAAAA/V5jh5XF6NBQ/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH, item, True)
            item = xbmcgui.ListItem('The Reggae Selecta',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-EvhOxI8WdWg/AAAAAAAAAAI/AAAAAAAAAAA/e8X3nNDSpvY/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH2, item, True)  
            item = xbmcgui.ListItem('Lloyd Williams',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-pYpEOEE_IS4/AAAAAAAAAAI/AAAAAAAAAAA/t70MqZ9IxSQ/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH3, item, True) 			
        xbmcplugin.endOfDirectory(HANDLE)
    except:
        buggalo.onExceptionRaised()

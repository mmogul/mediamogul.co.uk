import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse
from t0mm0.common.addon import Addon
from metahandler import metahandlers

addon_id = 'plugin.video.onlinemovies'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
ADDON2=xbmcaddon.Addon(id='plugin.video.onlinemovies')
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
metaset = selfAddon.getSetting('enable_meta')

def CATEGORIES():
        addDir2('Latest Cinema Releases','http://onlinemovies.pro/category/most-popular-new-movies/?filtre=date',1,icon,'',fanart)
        addDir2('Recently Added','http://onlinemovies.pro/category/genre/?filtre=date',1,icon,'',fanart)
        addDir2('Most Viewed','http://onlinemovies.pro/category/genre/?filtre=views',1,icon,'',fanart)
        addDir2('Highest Rated','http://onlinemovies.pro/category/genre/?filtre=rate',1,icon,'',fanart)
        addDir2('HD Movies','http://onlinemovies.pro/category/hd-movies/?filtre=random',1,icon,'',fanart) 
        addDir2('Christmas Movies','http://onlinemovies.pro/category/christmas-movies/',1,icon,'',fanart)
        addDir2('Disney','http://onlinemovies.pro/category/disneys/',1,icon,'',fanart)
        addDir2('Latest TV Episodes','http://onlinemovies.pro/category/serials/?filtre=date',1,icon,'',fanart) 
        addDir2('Search','url',3,icon,'',fanart)
        xbmc.executebuiltin('Container.SetViewMode(50)')
               
def GETMOVIES(url,name):
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        if 'category/serials/' in url: metaset='false'
        match=re.compile('<a href="(.+?)" title="(.+?)">').findall(link)[:-12]
        for url,name in match:
                name=cleanHex(name)
                if metaset=='false':
                        addLink(name,url,100,icon,'',fanart)
                else: addDir(name,url,100,'',len(match),isFolder=False)
        try:
                url=re.compile("<link rel='next' href='(.+?)'/>").findall(link)[0]
                addDir2('Next Page>>',url,1,icon,'',fanart)
        except: pass
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')
        
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))


def SEARCH():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Search Online Movies Pro')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
        url = 'http://onlinemovies.pro/?s='+ search_entered
        link = open_url(url)
        GETMOVIES(url,name)

def PLAYLINK(name,url,iconimage):
        link = open_url(url)
        try: url=re.compile('src="(.+?)" allowFullScreen></iframe>').findall(link)[0]
        except: url=re.compile("src='(.+?)' allowFullScreen></iframe>").findall(link)[0]
        ua='|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
        #### THANKS TO LAMBDA ####
        import client
        import jsunpack
        url = urlparse.urlparse(url).query
        url = urlparse.parse_qsl(url)[0][1]
        url = 'http://videomega.tv/cdn.php?ref=%s' % url
        result = client.request(url)
        unpacked = ''
        packed = result.split('\n')
        for i in packed: 
            try: unpacked += jsunpack.unpack(i)
            except: unpacked += i
        result = unpacked
        result = re.sub('\s\s+', ' ', result)
        url = re.compile('"video".+?"src"\s*\,\s*"(.+?)"').findall(result)
        url += client.parseDOM(result, 'source', ret='src', attrs = {'type': 'video.+?'})
        url = url[0]+ua
        #### THANKS TO LAMBDA ####

        ok=True
        liz=xbmcgui.ListItem(name, iconImage=icon,thumbnailImage=icon); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(url, liz, False)

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

def addLink(name,url,mode,iconimage,description,fanart):
        xbmc.executebuiltin('Container.SetViewMode(50)')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir2(name,url,mode,iconimage,description,fanart):
        xbmc.executebuiltin('Container.SetViewMode(50)')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir(name,url,mode,iconimage,itemcount,isFolder=False):
        if metaset=='true':
            splitName=name.partition('(')
            simplename=""
            simpleyear=""
            if len(splitName)>0:
                simplename=splitName[0]
                simpleyear=splitName[2].partition(')')
            if len(simpleyear)>0:
                simpleyear=simpleyear[0]
            mg = metahandlers.MetaData()
            meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&site="+str(site)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels= meta )
            contextMenuItems = []
            contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
            liz.addContextMenuItems(contextMenuItems, replaceItems=True)
            if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
            else: liz.setProperty('fanart_image', fanart)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
            return ok
        else:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&site="+str(site)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            liz.setProperty('fanart_image', fanart)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
            return ok
        
def open_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON2.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON2.getSetting(viewType) )

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass

print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)
print params

if mode==None or url==None or len(url)<1: CATEGORIES()
elif mode==1: GETMOVIES(url,name)
elif mode==2: GETTV(url,name)
elif mode==3: SEARCH()
elif mode==100: PLAYLINK(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))


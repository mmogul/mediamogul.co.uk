import os, xbmc, xbmcaddon
import binascii
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[B][COLOR red]**[COLOR white]Media Mogul[COLOR red]**[/COLOR][/B]'
BUILDERNAME    = 'Media Mogul Pro Toolkit'
#########################Make sure to change the repo to yours!!!!
EXCLUDES       = [ADDON_ID, 'repository.mediamogul', 'My_Builds', 'backupdir']
BUILDFILE      = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/wizard/build.txt'
UPDATECHECK    = 0
APKFILE        = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/wizard/apk.txt'
YOUTUBETITLE   = 'http://'
YOUTUBEFILE    = 'http://'
ADDONFILE      = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/wizard/addon.txt'
ADVANCEDFILE   = 'http://'
ROMPACK        = 'http://'
EMUAPKS        = 'http://'
ADDONPACK      = 'http://'
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################

##Alway test to see the color combo!!

#### NEW GUI THEME ###################################
# Choose from the following 
# Only these colors avalable
# white , blue , orange , yellow , red , purple , pink , lime , cyan, green
#Button focus color
FOCUS_BUTTON_COLOR = 'red'
EXIT_BUTTON_COLOR = 'green'
#Highlight outline for lists
HIGHLIGHT_LIST = 'red'
##No TXT file Banner
NO_TXT_FILE = 'red'

############################################
############################################
### The full list of colors for below can found @ https://forum.kodi.tv/showthread.php?tid=210837

#Top Main buttons
MAIN_BUTTONS_TEXT = 'white'
#All other buttons
OTHER_BUTTONS_TEXT = 'red'
#all list text color
##FYI any color placed in the txt file will overide this
LIST_TEXT = 'white'


#Description text title color
DES_T_COLOR = 'red'
#Description color
DESCOLOR = 'white'

#Wizard title name and verion color
WIZTITLE = 'Media Mogul Pro Toolkit / Wizard'
WIZTITLE_COLOR = 'white'
VERTITLE_COLOR = 'white'
VER_NUMBER_COLOR = 'red'
############################################################

## The colors and theme below is still used for the pop up dialogs
##Alway test to see the color combo
# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'blue'
COLOR2         = 'yellow'
COLOR3         = 'red'
COLOR4         = 'snow'
COLOR5         = 'lime'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR2+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR2+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'



#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmbuilds.png'
ICONMAINT      = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmmaint.png'
ICONAPK        = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmapks.png'
ICONADDONS     = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmaddons.png'
ICONYOUTUBE    = 'http://'
ICONSAVE       = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmsavedata.png'
ICONTRAKT      = 'http://'
ICONREAL       = 'http://'
ICONLOGIN      = 'http://'
ICONCONTACT    = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmcontact.png'
ICONSETTINGS   = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmsettings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'no'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Media Mogul Wizard.\r\n\r\nContact us, https://www.mediamogul.co.uk'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmcontact.png'
CONTACTFANART  = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmsplashdark.png'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'http://'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://'
# Url to folder zip is located in
REPOZIPURL     =  'http://'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/wizard/message.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font25'
HEADERMESSAGE  = 'Media Mogul Pro Toolkit'
# url to image if using Image 424x180
HEADERIMAGE    = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmptk.png'
# Font for Notification Window
FONTSETTINGS   = 'Font12'
# Background for Notification Window
BACKGROUND     = 'https://raw.githubusercontent.com/mmogul/mediamogul.co.uk/master/images/mmsplashdark.png'
############################    #############################
# -*- coding: utf-8 -*-

""" ^ SECTION 1:
    This should be at the top of your code to declare the type of text
    format you're using. Without this you may find some text editors save
    it in an incompatible format and this can make bug tracking extremely
    confusing! More info here: https://www.python.org/dev/peps/pep-0263/
"""
#----------------------------------------------------------------
"""
    SECTION 2:
    This is where you'd put your license details, the GPL3 license 
    is the most common to use as it makes it easy for others to fork
    and improve upon your code. If you're re-using others code ALWAYS
    check the license first, removal of licenses is NOT allowed and you
    generally have to keep to the same license used in the original work
    (check license details as some do differ).

    Although not all licenses require it (some do, some don't),
    you should always give credit to the original author(s). Someone may have spent
    months if not years on the code so really it's the very least you can do if
    you choose to use their work as a base for your own.
"""
#----------------------------------------------------------------
"""
    SECTION 3:
    This is your global imports, any modules you need to import code from
    are added here. You'll see a handful of the more common imports below.
"""
import os           # access operating system commands
import urlparse     # splits up the directory path - much easier importing this than coding it up ourselves
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)

# (*) = These modules require the noobsandnerds repo to be installed
import koding       # (*) a framework for easy add-on development, this template is to be used in conjunction with this module.
import nanscrapers  # (*) if you want to easily grab video links the hard work is done for you with this module.

from koding import Add_Dir  # By importing something like this we don't need to use <module>.<function> to call it,
                            # instead you can just use the function name - in this case Add_Dir().

from koding import route, Run # These are essential imports which allow us to open directories and navigate through the add-on.

#----------------------------------------------------------------
"""
    SECTION 4:
    These are our global variables, anything we set here can be accessed by any of
    our functions later on. Please bare in mind though that if you change the value
    of a global variable from inside a function the value will revert back to the
    value set here once that function has completed.
"""
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id
dialog       = xbmcgui.Dialog()                     # A basic dialog message command
home_folder  = xbmc.translatePath('special://home/')# Convert the special path of Kodi home folder to the physical path
addon_folder = os.path.join(home_folder,'addons')   # Join our folder above with 'addons' so we have a link to our addons folder
art_path     = os.path.join(addon_folder,addon_id)  # Join addons folder with the addon_id, we'll use this as a basic art folder
debug        = koding.Addon_Setting('debug')        # Grab the setting of our debug mode in add-on settings
#----------------------------------------------------------------
"""
    SECTION 5:
    This is optional, if you want to have your add-on hosted at noobsandnerds.com and
    would like to hook into their special framework then you need to add the following
    line. It has been commented out in this template, just uncomment if you want to use it
    but you will need to have your add-on approved by the noobsandnerds team for this functionality.
"""

# koding.User_Info()

#----------------------------------------------------------------
"""
    SECTION 6:
    Add our custom functions in here, it's VERY important these go in this section
    as the code in section 7 relies on these functions. If that code tries to run
    before these functions are declared the add-on will fail.

    You'll notice each function in here has a decorator above it (an @route() line of code),
    this assigns a mode to the function so it can be called with Add_Dir and it also tells
    the code what paramaters to send through. For example you'll notice the Main_Menu() function
    we've assigned to the mode "main" - this means if we ever want to get Add_Dir to open that
    function we just use the mode "main". This particular function does not require any extra
    params to be sent through but if you look at the Testing() function you'll see we send through
    2 different paramaters (url and description), if you look at the Add_Dir function in Main_Menu()
    you'll see we've snet these through as a dictionary. Using that same format you can send through
    as many different params as you wish.route
"""

#-----------------------------------------------------------
# EDIT THIS MAIN_MENU() FUNCTION - THIS IS FUN TO PLAY WITH!
#-----------------------------------------------------------
@route(mode="main")
def Main_Menu():

# Only show koding tutorials if debug mode is enabled in addon settings
    if debug=='true':
        Add_Dir(name='KODING TUTORIALS', url='', mode='tutorials', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))

    Add_Dir(name='TEST DIALOG', url='{"my_text":"My First Add-on[CR]Woohooo!!!","my_desc":"test description"}', mode='testing', folder=False, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))

# Once you've played with the above try uncommenting each of the following lines one by one.
# After uncommenting a line re-run the add-on to see your changes take place.

    # Add_Dir(name='OPEN FOLDER - TEST MODE', url='test_mode', mode='open_folder', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
    # Add_Dir(name='OPEN FOLDER - NO URL', url='', mode='open_folder', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
    # Add_Dir(name='VIDEO EXAMPLES', url='', mode='video_examples', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'), description='A couple of test videos for you to look at.', content_type='video')
    # Add_Dir(name='MUSIC EXAMPLE', url='', mode='music_examples', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'),content_type='song')

# This is our test zone, this just calls the Test_Function mode so feel free to play with the code in that function.
    # Add_Dir(name='TESTING ZONE', url='{"test1":"this is","test2":"some example","test3":"text"}', mode='test_function', folder=False, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
#-----------------------------
@route(mode="test_function", args=["test1","test2","test3"])
def Test_Function(test1, test2, test3):
# Example of sending multiple variables through the Add_Dir function
    xbmc.log(test1,2)
    xbmc.log(test2,2)
    xbmc.log(test3,2)
    dialog.ok('CHECK THE LOG','Take a look at your log, you should be able to see the 3 lines of example text we sent through.')
#-----------------------------
@route(mode="open_folder", args=["url"])
def Test_Folder(url):
    if url == 'test_mode':
        dialog.ok('Test Mode','open_folder has been called with the url being "test_mode". When you click OK you should open into and empty folder - this is because folder=True in our Add_Dir()')
    else:
        dialog.ok('TRY THESE EXAMPLES','If you\'ve left the mode as the default you\'ll receive a message explaining the mode does not exist. Feel free to change this to a mode that does exist.')
        Add_Dir(name='EXAMPLE FOLDER', url='', mode='changeme', folder=True, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
        Add_Dir(name='EXAMPLE ITEM', url='', mode='changeme', folder=False, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
        Add_Dir(name='EXAMPLE BAD FUNCTION', url='', mode='bad_function', folder=False, icon=os.path.join(art_path,'icon.png'), fanart=os.path.join(art_path,'fanart.jpg'))
#-----------------------------
@route(mode="bad_function")
def Bad_Function():
    if debug != 'true':
        dialog.ok('SET DEBUG TO TRUE','Go into your add-on settings and set debug mode to True then run this again. If debug is set to true we have proper error reporting in place to help your add-on development.')
        koding.Open_Settings(focus='1.1')
    xbmc.log(this_should_error)
#-----------------------------
@route(mode='testing', args=["my_text","my_desc"])
def Testing(my_text,my_desc):
    dialog.ok('TEST','Here are the params we recieved in Testing() function:', 'my_text: [COLOR=dodgerblue]%s[/COLOR]' % my_text,'my_desc: [COLOR=dodgerblue]%s[/COLOR]'%my_desc)
#-----------------------------
@route(mode="video_examples")
def Video_Examples():
    """
Below are some examples showing Add_Dir() with some artwork and infolabels sent through including trailer link for a movie
You would obviously use some sort of automated loop to auto-generate this info for large lists but hopefully this example may help
    """
    Add_Dir(name='[COLOR=dodgerblue][TV][/COLOR] Fraggle Rock S03E21', url='episode_dialog', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BNzg0MzQwODY3N15BMl5BanBnXkFtZTgwMjA2OTEwMjE@._V1_SY1000_CR0,0,789,1000_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMjI0MjI4NTEwNV5BMl5BanBnXkFtZTgwMzA4NTQ2MjE@._V1_.jpg',
        info_labels={"season":"03", "episode":"21", "genre":"Kids", "plot":"Get your cares away, worries for another day...", "mpaa":"U"})

    Add_Dir(name='[COLOR=dodgerblue][MOVIE][/COLOR] Trainspotting', url='movie_dialog', mode='scrape_sites', folder=False, content_type='Video',
        icon='https://images-na.ssl-images-amazon.com/images/M/MV5BMzA5Zjc3ZTMtMmU5YS00YTMwLWI4MWUtYTU0YTVmNjVmODZhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
        fanart='https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNjE3NzU2Nl5BMl5BanBnXkFtZTcwMzI0OTAyNg@@._V1_.jpg',
        info_labels={"originaltitle":"Trainspotting","genre":"crime,british", "plot":"Trainspotting is an awesome movie!", "mpaa":"18", "trailer":"plugin://plugin.video.youtube/play/?video_id=nBKWnAdmJJ8"})
    dialog.ok('CLICK INFO','Try bringing up the info for these items, you should see our artwork and other metadata has been populated.')
#-----------------------------
@route(mode="music_examples")
def Music_Examples():
    """
This is an example of adding a song, there's a good chance the scaper will find no results for this song,
it's only here as an example to show how to set things like artwork.
    """
    Add_Dir(name='Sally Cinnamon - Stone Roses', url='song_dialog', mode='scrape_sites', folder=False,
        icon='http://images.rapgenius.com/7929026cc89ab0c77669dee5cc323da9.530x528x1.jpg',
        fanart='http://www.flickofthefinger.co.uk/wp-content/uploads/2016/03/the-stone-roses-1.jpg',
        info_labels={"genre":"Rock,Inde,British", "artist":"Stone Roses", "title":"Sally Cinnamon"})
#-----------------------------
@route(mode="scrape_sites", args=["url"])
def Scrape_Sites(list_type):
    """
This is just a very rough example showing how simple it is to make use of the NaN Scrapers module.
We send through details of what we want to find and NaN Scrapers will search multiple websites for this content.
    """
    content = ''
    if list_type == 'movie_dialog':
        content = nanscrapers.scrape_movie_with_dialog(title='Trainspotting', year='1996', imdb='tt0117951', host=None, include_disabled=False, timeout=30)
    elif list_type == 'episode_dialog':
        content = nanscrapers.scrape_episode_with_dialog(title='Fraggle Rock', show_year='1983', year='1985', season='3', episode='4', imdb='tt0085017', tvdb=None, host=None, include_disabled=False, timeout=30)
    elif list_type == 'song_dialog':
        content = nanscrapers.scrape_song_with_dialog(title='Fools Gold', artist='Stone Roses', host=None, include_disabled=False, timeout=30)

# If the item returned is a dictionary that's great we know we have a list to work with
    if koding.Data_Type(content) == 'dict':
        xbmc.log(repr(content),2)
        playback = koding.Play_Video(video=content["url"], showbusy=True)
 
# It may be a plugin or direct url has been sent through, if so lets use the list_type variable
    elif not list_type.endswith('_dialog'):
        playback = koding.Play_Video(video=list_type, showbusy=True)

# Nothing useful has been found, lets exit back to the list
    else:
        return

# If the playback returned as True then it was successful but if it was False we know we need to try again for another source
    if not playback:
        if dialog.yesno('PLAYBACK FAILED','The video may have been removed, the web host may have altered their code or this video may not be available in your region. [COLOR=dodgerblue]Would you like to try another source?[/COLOR]'):
            Scrape_Sites(list_type)

#----------------------------------------------------------------
"""
    SECTION 7:
    Essential if creating list items, this tells kodi we're done creating our list items.
    The list will not populate without this
"""
Run()
xbmcplugin.endOfDirectory(int(sys.argv[1]))
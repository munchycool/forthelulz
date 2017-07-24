For this to import the necessary modules you must make sure you have the
noobsandnerds repository installed OR if you prefer you can add the modules4all repo
directory into your very own repo. Take a look at the noobsandnerds repo addon.xml
file and use that as a template.

If you'd prefer to use noobsandnerds repo then the steps are outlined below:

	1. In file manager add the following source: http://noobsandnerds.com/portal
	2. Name it whatever you want, it really doesn't matter
	3. System > Add-ons > Install from zip
	4. Click on the source you just added then click on noobsandnerds_repo.zip

ONCE NAN REPO IS INSTALLED:
That's it, you can now install this add-on by using the same "install from zip"
method you used above - just select this zip instead.

Make sure you install from zip (via the built-in Kodi add-on management system)
otherwise the relevant modules required will not be auto-installed.

You should now have the framework installed for your very own add-on.
Go through the default.py and read the comments for each section.
Enable each section in the Main_Menu() function one by one and start to see your add-on come to life!


<h3>Frequently Asked Questions:</h3>
Why do I need to install the noobsandnerds repo?
-- This add-on hooks into the python koding framework and that module is hosted on the noobsandnerds repo.

Why is the python koding module hosted on noobsandnerds repo?
-- There are a number of reasons:
   
   1: Some of the functions hook into the Add-on Portal framework at noobsandnerds.
   
   2: Many users already have that repo installed so it made perfect sense to put in a popular repo which may already be installed.
   
   3. The noobsandnerds team have offered a support forum for anyone wanting to use this module.

I want to develop an add-on and make it publicly available, what are my options?
-- You really have 3 options...

   1. Post up on the forum at http://noobsandnerds.com/support with a little introduction of what your add-on is about and state you'd like to have it officiallly supported at noobsandnerds.com. A member of the team will contact you, they can then get a proper support thread setup and put the add-on on the NaN repo (at your request and providing the add-on doesn't violate any site rules). By having your add-on hosted at noobsandnerds you will also have access to the special features that hook into their framework.

   2: Create your own repository and host on somewhere like github (it's free). If you contact the team at noobsandnerds they will happily add your repository to the daily Add-on Portal scan so your add-on can be accessed by the whole Kodi community.

   3: Just upload this zip file to your own server and add details to the Add-on Portal at http://noobsandnerds.com/addons. Their system allows for standalone zips which do not reside on repositories. This will allow the add-on to be installed via Community Portal but we would recommend using option 1 or 2 rather than this method - if you want to be able to push updates then you're really going to want it on a repository. Dealing with support when you only have standalone zips can be extremely hard work as you're never quite sure which version the user has installed, this was a big problem the XBMC foundation resolved a decade ago when they created the repository framework in Kodi (or XBMC as it was then).

Can I use this code commercially?
-- Please look at our TRMC system for commercial options: http://totalrevolution.tv


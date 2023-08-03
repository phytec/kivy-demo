Creating your own layer with Yocto 
===================================


Creating a layer
----------------

#. Start bitbake: :code:`source sources/poky/oe...-env`
#. Create layer: :code:`bitbake-layers create-layer meta-sdltest`
#. Move the repo in sources: :code:`mv meta-sdltest ../sources/`
#. Add the new layer inside the config file: :code:`nano confi/bblayers.conf` and add at the end :code:`BBLAYERS += "${BSPDIR}/sources/meta-sdltest "`
#. Check if layer added:  :code:`bitbake-layers show-layers`


Creating a recipe recette
--------------------------

Changing an existing layer 
---------------------------

Imagine you want to install Kivy and the recipe to install it already exist. Incredible right ? 
Now imagine that you try the recipe, and it's not working. You need to change something. 
However, if you directly modify a recipe in a layer you do not own (like openembedded), you then have a problem.
That's what the bbappend do to the recipe file (ending by the extension bb). 

To learn how to create and use bbappend, you can check the following links: 
Yocto 
PHYTEC 


How to debug on Yocto ?
-----------------------

Note: a bit tricky but I think the main thing to understand with yocto is that it is kind of a mega parser. 
It goes on, parse the update files and check what you have on your cache. 
A lot of stuff are done implicilty, for example if you follow the structure of the recipe folder, you can easily add bbappend in another parent folder without any problem. 
And some config are going to overlap over each other. It can be quite confusing sometimes. One of the best tools to use in yocto are : `find`, `grep` and `tree`. 
They can show interesting informations about the structure of your code in the sources folder. 

The pb with the cache is that sometimes, it does not reload something that changes and therefore, it is necessary to clean what is in the cache. 
You also need tools to be able to know exactly what you build, yocto provides some and you need to know where to look for more informations (manifest, bitbake -e, ...)

* find, grep, tree
* bitebake -e  
* manifest
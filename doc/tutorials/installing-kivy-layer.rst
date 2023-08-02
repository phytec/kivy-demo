Installing Kivy layer
=====================

First, you need to setup Yocto following the first steps with Yocto. 

The goal of this tutorial is to understand what is available in the ```meta-phykivy``` layer. 

What is available in this layer:

* kivy bbappend 
* sdl correction
* patches for kivy 
* kivy md + patches 
* weston for LVSD0 display by default
* image for kivydemo 

Installing the layer
--------------------

First install the qt6 demo (also called qtphy). To do that do the following 

Init with phyLinux init 
Choose you distro, ... 

Accept FSL EULA in the local.conf file. 
Git clone the layer and add it to your bblayer.conf file. 

Bake the recipe and tada, it should work !

Understanding the layer 
----------------------- 

The minimal files necessary to run Kivy are:

* sdl2 bbappend 
* kivy bbappend
* patch for the cameras for kivy 
* the image 

Kivy recipe and minimal version 
*******************************

Kivy is using sdl2 to work. However, sdl2 do not work out of the box for this product. 
You need first to force it to use wayland instead of X11. To do that, you need to add the bbappend. 

Th same for the patch, the cameras in kivy does not work as it should on the product. 

Disabling Kivy Demo 
-------------------

TMP 
---

You can build a layer using the following instructions : (cf notes)

Once the layer created, you can see the following structure in your layer: (show the layer with tree)

You can configure you layer using the ```layer.conf``` file. 
Inside, you can find the files you want to add to the final product using regex, you can also give a priority to your layer. 
It is possible for the layer to overlap and override some part. 
Therefore, the how with the highest priority is the one who cannot be overwritten. 

The recipes are separate in 4 folders: 

* devtools: contain the python dependencies such as kivy and kivymd. 
* examples: example programs for the target 
* graphics:  graphics dependencies such as sdl2 and wayland/weston 
* image: the image for the target, which means the recipe that is going to build my final image. 

With this recipe, I end up with a file with a .wic extensions and the rootfiles are build to have a full bootable image that I can copy on a sd card.

My goal was to add the package kivy that is normaly installed with pip (package management tools for Python) with yocto. 
On recipe was already available in openembedded directory. 
However, the graphics installed on my target were not compatible with kivy, each time I had a windows abort error with all kind of error message. 
In the kivy documentation, it was written that kivy could work with the following setup: ... . 

To disable the service in the layer, do : ```SYSTEMD_AUTO_ENABLE:kivyphy-service = "disable"```


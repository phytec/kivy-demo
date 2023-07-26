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

Maybe I can also add the command to stop the service also, like for qtphy !

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


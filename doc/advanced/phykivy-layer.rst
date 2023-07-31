Introduction to phykivy layer
=============================

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
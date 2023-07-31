First steps with Yocto
======================

Installing the BSP
------------------

Copy/Paste what's on the Yocto installation for the steps

Understanding a bit more
------------------------

More on yocto:
* source bitebake - you are then in build 

Okay, we have two main folder :
* build 
* sources 

In build, you have: 
* a conf folder with three files (I know 2 - local.conf and bblayer.conf)
* the image for your product 
* tmp folder where you can see all the result in your recipe

But before doing all this steps, you need to choose which machine you are going to work on:
* machine 
* BSP version
* image 

Note: a bit tricky but I think the main thing to understand with yocto is that it is kind of a mega parser. It goes on, parse the update files and check what you have on your cache. A lot of stuff are done implicilty, for example if you follow the structure of the recipe folder, you can easily add bbappend in another parent folder without any problem. And some config are going to overlap over each other. It can be quite confusing sometimes. One of the best tools to use in yocto are : `find`, `grep` and `tree`. They can show interesting informations about the structure of your code in the sources folder. 

Here is the structure inside a yocto project: 
* layer 
* recipe (files, patches, ... )

You have multiple layers, and it's not because some recipes or layers are inside your source folder that bitebake is going to compile and package them. No you have to add them

Créer une layer
---------------

Créer une recette
-----------------


Comment debugger ? 
------------------

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
Install a package in Yocto with pip
===================================

You project is going well and your application is beautiful, but you want to add this new wonderful package for your project. 
It's not a big deal in your computer, you just have to use `pip install` and voilà !

It is however important to know that if you want to customize your own image while keeping it small, you can add a package using Yocto. 
To do that make sure you understand the following before continuing: first steps with yocto. 

If you follow that, you normaly have your yocto folder installed. 

For more information, please check this page and this page (official pages).

Check if the recipe is already available in openembedded
--------------------------------------------------------

That's the simplest option, believe me ! (Make an example with something that work in real life!)

You need to check a few things first: 
* what version of Yocto are you using ? 

To do that do ... [idk yet how to know which version you are using, but probably in a config file no ?] 

Then go to the following website to check if a recipe already exist. 

You can also check if it is installed by going into the folder sources/meta-openembedded/python/...

Once there, you can check if you lib is available with the following command on linux: 
find -name "*my-lib*".

If you have some result, then it's a good sign. You first need to find the file with the extension .bb (for example kivy.bb). 
Keep the first part of file (for example if you have my-lib_0.1.2.bb you need to select my-lib) and add to your conf/local.conf file:
IMAGE_INSTALL += python3-my-lib

And then, bake the image first using the recipe name and finally the name of the full image. 

You are now ready to import this new lib on your target !

If the recipe is not available, download it from pip
----------------------------------------------------

First, you need to create a new recipe in your layer. If you don't have a layer, please check this part [link here].

To create a new recipe: 

1. Go check on pip the version you need for your project (warning: be careful of the version of your other lib and python version on the target)
2. Name you file mylib_version.bb
3. Add the following (code of a bb recipe for pip)

To get the tag, you need to go in pip and get that here.

4. Check the dependencies needed for you lib and add them in yocto
5. Try to bake the recipe 

If everything is working fine, that's great. 

Otherwise, here are some possible issues:

- problem with the setup file (method to fix it) - how to do a patch !
- problem of dependencies

Conclusion
----------

Installing the package library directly from Yocto can free some space not available because of pip.
There are other methods to add python package such as this or this.


Creating Your Own Layer with Yocto
==================================

You have successfully imported an existing layer in the previous tutorial :doc:`/tutorials/installing-kivy-layer`. 
However, you might want to create your own layer now, add your own recipe, or modify an existing recipe using a :code:`bbappend` file. 
If that's the case, you're in the right place!

Creating a Layer
----------------

Why Create Your Own Layer?
***************************

Think of a Yocto layer as a collection of recipes and configurations that you can add to your Linux build. 
Creating your layer allows you to keep your customizations separate from the core Yocto setup. 
This separation helps you keep things organized, maintain compatibility with updates, and share your creations with others.

How to Create Your Layer
*************************

Creating a layer is a straightforward process. Follow these steps:

1. Navigate to your yocto folder and start bitbake with:

.. code-block:: bash

    $ source sources/poky/oe-init-build-env`

2. Create and move your new layer inside the :code:`sources` folder:

.. code-block:: bash

    $ bitbake-layers create-layer <meta-mylayer> && mv <meta-mylayer> ../sources/

3. Add the new layer to the configuration file: Open :code:`conf/bblayers.conf` and add the following line at the end:

.. code-block:: bash
    
    BBLAYERS += "${BSPDIR}/sources/meta-mylayer"

4. Verify if the layer is added to your image using: :code:`bitbake-layers show-layers`.

Changing an Existing Recipe
----------------------------

Imagine you want to install Kivy, and the recipe to install it already exists. Incredible, right? However, after trying the recipe, you find it's not working, and you need to make some changes. If you directly modify a recipe in a layer you do not own (like openembedded), you'll run into problems.

That's where the file with the extension :code:`bbappend` comes into play. It allows you to extend the behavior of an existing recipe without modifying it directly.

To learn how to create and use bbappend, you can refer to the :code:`bbappend` files in the sources folder.

How to Debug on Yocto?
----------------------

You might encounter errors while creating your recipe. If that's the case, you need to understand a little about how Yocto works and where to check for information.

How to Find Files
******************

Yocto is a powerful parser that goes through update files and checks your cache. Many steps are done implicitly, which can sometimes lead to confusion. One of the best tools to use in Yocto are :code:`find`, :code:`grep`, and :code:`tree`. They can show you useful information about the structure in the :code:`sources` folder.

Don't Forget the Cache !
************************

The cache is quite useful. The first time you build your image, it might take a while. But the following builds are going to be much faster. That's because of the cache !

However, the cache sometimes doesn't reload something that has changed. That's why a good practice is to clean the cache when a problem occurs. 
To do that, you can use the following command

.. code-block:: bash 

    bitbake -c cleanall <myrecipe>

Check Your Recipe in the Image
*******************************

Because Yocto only compile a part of what is present in the sources folder, you sometimes have to check if what you added is really on the image. 
For that, you can use this tools:

* Look into the :code:`*.manifest` file in your image folder (where you obtain your final file you copy on the SD card).
* Look into the :code:`work/tmp` folder in the :code:`build` directory. You can find for each recipe a folder with all the files fetched by Yocto and the final result of the packaging inside the :code:`image` directory.
* Use the command :code:`bitbake -e`.

Conclusion
----------

You now have a better understanding of how to create and use a layer in Yocto. You're ready to customize your own version of Linux for your product. 
If you want to add a specific Python package to your board through Yocto, please check :doc:`/tutorials/yocto-pip`.
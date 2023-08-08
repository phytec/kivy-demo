Creating Your Own Layer with Yocto
==================================

You have successfully imported an existing layer in the previous tutorial :doc:`/tutorials/installing-kivy-layer`. 
However, you might want to create your own layer now, add your own recipe, or modify an existing recipe using a :code:`bbappend` file. 
If that's the case, you're in the right place!

Creating a Layer
----------------

Creating a layer is a straightforward process. Follow these steps:

1. Navigate to your :code:`yocto` folder.
2. Start bitbake: :code:`source sources/poky/oe-init-build-env`.
3. Create a new layer: :code:`bitbake-layers create-layer meta-mylayer`.
4. Move the repository to :code:`sources`: :code:`mv meta-sdltest ../sources/`.
5. Add the new layer to the configuration file: Open :code:`conf/bblayers.conf` and add the following line at the end: :code:`BBLAYERS += "${BSPDIR}/sources/meta-mylayer"`.
6. Verify if the layer is added to your image using: :code:`bitbake-layers show-layers`.

Changing an Existing Recipe
----------------------------

Imagine you want to install Kivy, and the recipe to install it already exists. Incredible, right? However, after trying the recipe, you find it's not working, and you need to make some changes. If you directly modify a recipe in a layer you do not own (like openembedded), you'll run into problems.

That's where the file with the extension :code:`bbappend` comes into play. It allows you to extend the behavior of an existing recipe without modifying it directly.

To learn how to create and use bbappend, you can refer to the `Yocto documentation on write a new recipe <https://docs.yoctoproject.org/dev-manual/new-recipe.html>`_.

How to Debug on Yocto?
----------------------

You might encounter errors while creating your recipe. If that's the case, you need to understand a little about how Yocto works and where to check for information.

How to Find Files
*********************

Yocto is a powerful parser that goes through update files and checks your cache. Many steps are done implicitly, which can sometimes lead to confusion. One of the best tools to use in Yocto are :code:`find`, :code:`grep`, and :code:`tree`. They can show you useful information about the structure in the :code:`sources` folder.

Don't forget the cache !
************************

The cache is quite useful. The first time you build your image, it might take a while. But the following builds are going to be much faster. That's because of the cache !

However, the cache sometimes doesn't reload something that has changed. That's why a good practice is to clean the cache when a problem occurs. 
To do that, you can use the following command

.. code-block:: bash 

    bitbake -c cleanall <myrecipe>

Check your recipe of layer in the image
*******************************************

You create your new recipe and no error message appears when creating your image. However, when you check your image, it's as if your image did not take into account what you just added. 

Because Yocto only compile a part of what is present in the sources folder, you can have to check if what you added is really on the image. 
For that, you can use this tools:

* `bitbake -e`: you have information
* Look into the `*.manifest` file in your image folder (where you obtain your final file you copy on the SD card).
* Look into the `work/tmp` folder in the `build` directory. You can find in this folder all the files fetched by Yocto and the final result in the :code:`image` directory.

Conclusion
----------

You now have a better understanding of how to create and use a layer in Yocto. You're ready to customize your own version of Linux for your product. 
If you want to add a specific Python package to your board through Yocto to create a lightweight image, please check :doc:`/tutorials/yocto-pip`.
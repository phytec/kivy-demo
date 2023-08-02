Install a Package in Yocto with Pip
===================================

Your project is going well, and your application is working beautifully, but now you want to add a new, wonderful package to your project. While installing packages using pip install is simple on your computer, you need to follow a different approach in Yocto if you want to customize your own image while keeping it small.

Before proceeding, ensure you understand the first steps with Yocto. If you haven't set up your Yocto environment yet, please refer to the official pages for more information.

Recipe is available in OpenEmbedded
------------------------------------

The simplest option is to check if the desired package already exists in OpenEmbedded. Follow these steps:

1. Determine the version of Yocto you are using. You can find this information in a configuration file.
2. Go to the following website to check if a recipe for your package already exists in OpenEmbedded. 
3. Alternatively, you can manually check if the package is installed by navigating to the folder :code:`sources/meta-openembedded/python/` in your Yocto setup and using the following command on Linux:

.. code-block:: bash

    find -name "my-lib"

If you get some results, it's a good sign. The first part of the file name is the recipe name (e.g., if you have my-lib_0.1.2.bb, the recipe name is my-lib).

4. Add the recipe to your Yocto configuration. Open the :code:`conf/local.conf` file and add the following line:

.. code-block:: bash

    IMAGE_INSTALL += "python3-my-lib"

5. Replace :code:`my-lib` with the actual name of your package.
6. Bake the Yocto image using the updated configuration.

Now, you are ready to use the new library on your Yocto target!

If the Recipe is Not Available, Download It from Pip
----------------------------------------------------

If the desired package's recipe is not available in OpenEmbedded, you can create a new recipe in your Yocto layer. Follow these steps:

1. Determine the version of the package you need for your project by checking the desired version on the official PyPI website.
2. Name your recipe file following the convention mylib_version.bb, where mylib is the name of your package, and version is the version you want.
3. Create a new recipe with the following content:

.. code-block:: python

    SUMMARY = "MyLib Python package"
    HOMEPAGE = "https://example.com/mylib"
    LICENSE = "MIT"
    LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

    SRC_URI[md5sum] = "1234567890abcdef1234567890abcdef"
    SRC_URI[sha256sum] = "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"

    inherit pypi

4. Replace the SRC_URI md5sum and sha256sum values with the actual checksums you obtained from the PyPI website.
5. Check the dependencies needed for your library and add them to your Yocto setup.
6. Attempt to build the recipe using the bitbake command.

If everything is working fine, that's great! You have successfully created a recipe for your package.

However, if you encounter issues, here are some possible solutions:

#. If there's a problem with the setup file, you may need to apply a patch to resolve it.
#. Ensure that all dependencies are correctly specified in the recipe.

The best way to learn more is to go check the recipes in the openembedded meta-python layer for recipe. 

Conclusion
-----------

Installing the package library directly from Yocto can help save space that may not be available due to using pip. Remember, there are other methods to add Python packages in Yocto, such as using recipes from OpenEmbedded layers or creating custom recipes for packages not available in the default Yocto repositories. Be sure to explore those options as well.

.. _official pages: https://example.com/yocto-setup
.. _check if a recipe: https://example.com/openembedded-recipes
.. _official PyPI website: https://pypi.org/project/mylib/

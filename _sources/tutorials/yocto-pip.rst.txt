Install a Python Package in Yocto
==================================

Your project is going well, and your application is working beautifully, but now you want to add a new, wonderful package to your project. 

While installing packages using :code:`pip install` is simple on your computer, you need to follow a different approach in Yocto if you want to customize your own image while keeping it small.

Before proceeding, make sure you understand the tutorial :doc:`/tutorials/first-steps-yocto`.

Check if the recipe is already available
------------------------------------------

You can check if a recipe is already available by going inside the :code:`sources` folder and doing:

.. code-block:: bash

    find -name "my-lib"

**NOTE** You can also check the `OpenEmbedded Website <https://layers.openembedded.org/layerindex/branch/master/layers/>`_ for available recipes. 

Add a recipe
-------------

If Yocto provides a recipe for your package, the integration process is straightforward. Here's how:

1. Open your :code:`conf/local.conf` file
2. Add the following line to include the package in your image:

.. code-block:: bash

    IMAGE_INSTALL += " python3-my-lib"

3. Replace :code:`my-lib` with the actual name of your package
4. Build your Yocto image to incorporate the package with: :code:`bitbake my-image`


Create your recipe with PyPI
-----------------------------

If you don't have an existing recipe and the package is available on PyPi, you have the power to create your own. 

Prerequisites
**************

Make sure you have your own layer installed and configured before creating your recipe. If it's not the case, check the tutorial :doc:`/tutorials/creating-my-layer`.

Creating the recipe
********************

1. Find the package version you need on the `PyPI website <https://pypi.org/>`_
2. Choose a version for you package and name your recipe following this format: :code:`mylib_1.2.3.bb`, replacing 'mylib' with the package name and '1.2.3' with the desired version
3. Create a new recipe with the following content:

.. code-block:: python

    SUMMARY = "MyLib Python package"
    HOMEPAGE = "https://example.com/mylib"
    LICENSE = "MIT"
    LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

    SRC_URI[md5sum] = "1234567890abcdef1234567890abcdef"
    # or
    # SRC_URI[sha256sum] = "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"

    inherit pypi setuptools3

6. Replace the :code:`LICENSE`, :code:`LIC_FILES_CHKSUM` and :code:`SRC_URI` values with the actual checksums you obtained from the PyPI website
7. Check the dependencies needed for your library and add them to your Yocto setup
8. Try building the recipe using the bitbake command: :code:`bitbake mylib`

If everything is working fine, that's great! You have successfully created a recipe for your package.

Troubleshooting
****************

Running into issues? Don't worry, it happens to the best of us. Here are some tips:

#. Ensure that all dependencies are correctly specified in the recipe and check the recipe of those dependencies
#. Create a patch to fix the broken code

To learn more on recipes, check the openembedded :code:`meta-python` layer. 

Conclusion
-----------

Yocto offers multiple ways to add Python packages, whether through existing recipes or custom recipes. 

Remember to refer to the official Yocto documentation and the PyPI website for valuable insights:

* `official Yocto page <https://docs.yoctoproject.org/>`_
* `official PyPI website <https://pypi.org/>`_

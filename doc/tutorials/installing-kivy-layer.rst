Installing the Kivy layer in Yocto
==================================

Before proceeding, make sure you have set up Yocto following the first steps with Yocto.

Installing the Layer
---------------------

To install the `meta-phykivy` layer and understand what is available in it, follow these steps:

1. Install the Qt6 demo (also called `qtphy`) by running:

.. code-block:: bash

   ./phyLinux init
   Choose your distro, …

2. Accept the FSL EULA in the :code:`local.conf` file.
3. Git clone the :code:`meta-phykivy` layer and add it to your `bblayer.conf` file.
4. Build the recipe by using the `bitbake kivyphy-image ...` command

That's it, you should then have the exact same image as the one you download during the first tutorial (link).

Understanding the Layer
------------------------

The minimal files necessary to run Kivy are:

* :code:`sdl2.bbappend`
* :code:`kivy.bbappend`
* Patch for the cameras for Kivy
* The image recipe 

Kivy Recipe and Minimal Version
--------------------------------

Kivy uses sdl2 to work, but sdl2 does not work out of the box for this product. To use wayland instead of X11, you need to add the `sdl2.bbappend`.

Similarly, the cameras in Kivy do not work as expected on the product, so you need a patch to fix this.

Disabling Kivy Demo
--------------------

To disable the Kivy demo inside the image, add the following line inside the :code:`local.conf` file:

.. code-block:: bash

    SYSTEMD_AUTO_ENABLE:kivyphy-service = "disable"

You can also disable the service on the board with:

.. code-block:: bash

    My code here 

That way, you can avoid to have the demo each time you boot the board. 
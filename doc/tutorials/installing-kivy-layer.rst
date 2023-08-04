Installing the Kivy layer in Yocto
==================================

Before proceeding, make sure you have set up Yocto following the :doc:`/tutorials/first-steps-yocto`.

Installing the Layer
---------------------

To install the :code:`meta-phykivy` layer and understand what is available in it, follow these steps:

1. Install the Qt6 demo (also called :code:`qtphy`) by running:

.. code-block:: bash

   DISTRO=ampliphy-vendor-xwayland MACHINE=phyboard-pollux-imx8mp-3 ./phyLinux init -p imx8mp -r BSP-Yocto-NXP-i.MX8MP-PD22.1.1

You can also only use :code:`./phyLinux init` and see all the options for the parameters before choosing one.
If you want more information on how to install your Phytec BSP with :code:`phyLinux`, you can check the `PHYTEC Yocto Reference Manual <https://www.phytec.de/cdocuments/?doc=UIHsG>`_

2. Uncomment :code:`ACCEPT_FSL_EULA = "1"` in the :code:`local.conf` file.
3. Git clone the :code:`meta-phykivy` layer in the source folder and add it to your :code:`bblayer.conf` file. 
4. Build the final image by using the :code:`bitbake phytec-kivydemo-image` command after starting bitbake.

That's it, you should then have the exact same image as the one you download during the first tutorial in :doc:`/tutorials/installation`.

Understanding the Layer
------------------------

The files necessary to run Kivy are:

* :code:`sdl2.bbappend`
* :code:`kivy.bbappend`
* Patch for the cameras for Kivy (:code:`camera_gi.patch` and :code:`kivy_opencv.patch`)
* The image recipe 

All the other files are optional. Some patch are present to fix some warnings in Kivy. 

Kivy Recipe and Minimal Version
--------------------------------

Kivy uses sdl2 to work, but sdl2 does not work out of the box for this product. To use Wayland instead of X11, you need to add the :code:`sdl2.bbappend`.

Similarly, the cameras in Kivy do not work as expected on the product, so you need a patch to fix this depending on you provider for the camera (:code:`gstreamer` or :code:`opencv`).
For more information about the cameras, you can check :doc:`/demo/camera`.

Disabling Kivy Demo
--------------------

To disable the Kivy demo inside the image, add the following line inside the :code:`local.conf` file:

.. code-block:: bash

    SYSTEMD_AUTO_ENABLE:kivyphy-service = "disable"

You can also disable the service on the board with:

.. code-block:: bash

    # to stop the service 
    systemctl stop kivyphy-service

    # to start the service again 
    systemctl start kivyphy-service

    #to disable permanently, so it does not start on boot
    systemctl disable kivyphy-service

That way, you can avoid to have the demo each time you boot the board. 
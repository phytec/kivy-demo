Installation
============

Product : Imx8mp 
-----------------

Before you start, make sure you have everything you need for setting up your device.

**Required Items:**

* SD Card (and an adaptator if needed for your computer)
* Power adapter (+24V)
* Ethernet cable 
* USB-A to USB-B Micro Cable 
* [OPTIONAL] USB camera

For the display, you have two options:

* Use an HDMI-connected screen
* Use an LVDS screen with its cables

To begin, ensure that the Boot Mode DIP Switch (S3) is set to :code:`SD Card`:

.. image:: ../images/SD_Card_Boot.png
  :width: 100
  :alt: board-front
  :align: center

Follow these steps to get your board up and running:

#. Connect the USB cable to your host PC and the Debug FTDI (X1).
#. Insert the Micro SD Card into the board (X7).
#. Connect the power adapter to the power supply connector (X23).
#. Turn on the power supply.

.. image:: ../images/board-front.png
  :width: 600
  :alt: board-front
  :align: center

For detailed setup instructions, refer to the `the i.MX8MP Product Documentation <https://www.phytec.de/fileadmin/phytec_base/images/01-Produkte/Component-Placement/L1025e.A0-phyBOARD-Pollux_iMX8M-Plus_web.pdf>`_.


Downloading a Bootable Image on the SD Card 
--------------------------------------------

To get started, your board needs an image. Here's how to download a pre-built image from Phytec to your SD Card.

First, download the pre-build image: 

.. code-block:: bash

    wget https://phytec/a_specific_folder/my_image_url.wic 

You should now have a file named :code:`my_image_url.wic` in your folder. 

If you need to customize the image or add packages using Yocto, refer to the turotial :doc:`/tutorials/first-steps-yocto` or check `the PHYTEC documentation <https://www.phytec.de/cdocuments/?doc=UIHsG>`_ .

Once the file is downloaded on your computer, you need to copy it on the SD card. 
To do that, you first need to find the name of your SD Card.

On linux, you have two ways to find this name: :code:`dmseg` or comparing the files in :code:`/dev` before and after pluging the SD Card to the computer.

Once you have the name of your SD Card (for example :code:`mmcblk0`), you need to unmount the partitions. The name of a partition is as follow: :code:`/dev/mmcblk0p1` with :code:`p1` indicating the first partition. 
To unmount a partition use the following command: 

.. code-block:: bash

    unmount /dev/mmcblk0p1

Once **ALL** you partitons are removed, you can copy the image using the :code:`dd` command:

.. code-block:: bash

    sudo dd if=<my_image_url.wic> of=/dev/mmcblk0 bs=1M conv=fsync status=progress

You need to replace :code:`my_image_url.wic` by the file downloaded previously. 


**WARNING** Be very careful when selecting the right drive for the SD card ! 
Selecting the wrong one can erase your hard drive!


Your SD Card is now ready to be used !
To test your image, add your SD card and power the board. You should see the Linux logo and then a demo for kivy starting.

Getting connected to the target
-------------------------------

There are two ways to connect to the board from your PC:

- `Serial Connection`_
- `Ethernet Connection`_


Serial Connection
*****************

To the target, you can use a connection. 
First check that your computer is linked to the board via the serial connector (X1: USB debug).

If it's not present on you computer, install :code:`tio` with the following command : 

.. code-block:: bash

    sudo apt install tio

Then to connect to the board, launch: 

.. code-block:: bash

    tio /dev/ttyUSB<num>

You need to replace the <num> part by your USB number. If you have any doubt check the number available with the following command:

.. code-block:: bash

    $ cd /dev

    $ find -name ttyUSB*

After connecting to the board with :code:`tio`. You will see a line asking for a password.
By default, the password is `root`. Once you enter this password, you should be able to access to the board.  

Congratulation, you are connected to your device ! 

Ethernet Connection
*******************
 
With an Ethernet connection, you can connect to the board using the :code:`ssh`. You can also copy files from your computer to your device using :code:`scp`. 

To create this connection, first use an Ethernet cable to link your device and your PC. 

You then need to setup manually the following information on your computer.  

.. _Device ip info table:
.. list-table:: Device IPv4 information
   :widths: 25 25 40
   :header-rows: 1

   * - IP address
     - Subnet mask
     - Gateway
   * - 192.168.3.10
     - 255.255.255.0 or /24
     - 192.168.3.10

You can do it on your own with the :code:`ifconfig` or :code:`ip` command. 

Otherwise, here are the steps to configure the Ethernet connection on Ubuntu. 
If you are not using Ubuntu but want still stay close to this tutorial, you can install and use a PHYTEC Virtual Machine. 

To configure the IPv4 device information on Ubuntu you need to:

#. Search "network" in the applications (Windows key to access the search bar on Ubuntu)
#. Select the Ethernet port used by the connection
#. Go to IPv4 setting 
#. Select the :code:`Manual` method and add a new adress with the information available in the :ref:`previous table <Device ip info table>`.

To test the connection, you can do :

.. code-block:: bash

    ping 192.168.3.11

**WARNING**  Your device need to be turned on when you test your connection.

If you receive the packets of data then congratulation, you are connected !

Display
-------

You need a display to render your graphic application. To setup the display with your board, you need to check the BSP Manual of your product.

For example, if you have a LVDS screen on a i.MX8MP boad, you need to modify the :code:`weston.ini` file and restart your board.
You can find more information in the `phyCORE-i.MX 8M Plus BSP Manual <https://www.phytec.de/cdocuments/?doc=mwDRJw&__hstc=12841640.7b3cea865c20ac90f4f0261768fbccc3.1685517610384.1685602240432.1685687289043.7&__hssc=12841640.1.1685687289043&__hsfp=2239254415&_ga=2.132368782.1467000783.1685517610-576238176.1685517609#L1017e-A5phyCOREi-MX8MPlusBSPManual-phyBOARD-PolluxComponentsphyBOARD-PolluxComponents>`_. 

Sources
-------

If you want to learn more on how to install the image on the board or how to configure the display, please check the `phyCORE-i.MX 8M Plus BSP Manual <https://www.phytec.de/cdocuments/?doc=mwDRJw&__hstc=12841640.7b3cea865c20ac90f4f0261768fbccc3.1685517610384.1685602240432.1685687289043.7&__hssc=12841640.1.1685687289043&__hsfp=2239254415&_ga=2.132368782.1467000783.1685517610-576238176.1685517609#L1017e-A5phyCOREi-MX8MPlusBSPManual-phyBOARD-PolluxComponentsphyBOARD-PolluxComponents>`_.

If you are working on another product (for example the imx6) you can check the BSP Manual on the PHYTEC website. 
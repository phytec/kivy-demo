Installation
============

Product : Imx8mp 
-----------------

You first need to setup the device. For that you need : 

* a SD Card (and an adaptator if needed for your computer)
* a power adapter +24V
* an ethernet cable 
* a USB-A to USB-B Micro Cable 
* [OPTIONAL] a USB camera

For the display, you have two choices:

* use a screen connected through an HDMI cable  
* an LVSD screen and its cables

To start your board, the first step is to check that the Boot Mode DIP Switch (S3) is set to :code:`SD Card` as follow:

.. image:: ../images/SD_Card_Boot.png
  :width: 100
  :alt: board-front
  :align: center

Once it's done, you can continue with the following steps: 

#. Connect the USB cable to your host PC and the Debug FTDI (X1).
#. Insert the Micro SD Card inside the board (X7).
#. Connect the power adapter to the power supply connector (X23).
#. Turn your power supply on.

.. image:: ../images/board-front.png
  :width: 600
  :alt: board-front
  :align: center

For more information on how to setup the board, please refer to `this document for the i.MX8MP product <https://www.phytec.de/fileadmin/phytec_base/images/01-Produkte/Component-Placement/L1025e.A0-phyBOARD-Pollux_iMX8M-Plus_web.pdf>`_.


Downloading a bootable image on the SD card 
--------------------------------------------

To start correcly, your board need an image. In this example, you will learn how to download a pre-build image made by Phytec on the SD Card.

First you need to download the pre-build image on your computer: 

.. code-block:: bash

    wget https://phytec/a_specific_folder/my_image_url.wic 

You should have in your folder a file named :code:`my_image_url.wic`. 

Everything you need for this tutorial is installed on this image. 
If you want to personalize the image or add new package using Yocto, you can go to the tutorial :doc:`/tutorials/first-steps-yocto` or check `the PHYTEC documentation <https://www.phytec.de/cdocuments/?doc=UIHsG>`_ .

Once the file is downloaded on your computer, you need to copy it on the SD card. 
To do that, you first need to find the name of your SD Card.

On linux, you have two ways to find the name of your SD Card: :code:`dmseg` or comparing the files in :code:`/dev` before and after pluging the SD Card to the computer.

Once you have the name of your sd card (for example :code:`mmcblk0`), you need to unmount the partitions. The name of a partition is as follow `/dev/mmcblk0p1` with `p1` indicating the first partition. 
To unmount a partition use the following command: 

.. code-block:: bash

    unmount /dev/mmcblk0p1

Once **ALL** you partitons are removed, you can copy the image using the :code:`dd` command:

.. code-block:: bash

    sudo dd if=my_image_url.wic of=/dev/mmcblk0 bs=1M conv=fsync status=progress

.. warning:: 

    Be very careful when selecting the right drive for the SD card ! 
    Selecting the wrong drive can erase your hard drive!


Your SD Card is now ready to be used !
To test your image, add you SD card and power the board. You should see the Linux logo and then a demo for kivy starting.

Getting connected to the target
-------------------------------

There are two ways to connect to the board from your PC:

- `Serial connection`_
- `Ethernet connection`_


Serial connection
*****************

If you want to connect to the target you can do that via the serial connection. 
First check that your computer is link to the board via the serial connector (X1: USB debug).

If it's not present on you computer, install :code:`tio` with the following command : 

.. code-block:: bash

    sudo apt install tio


Then launch: 

.. code-block:: bash

    tio /dev/ttyUSB<num>

You need to replace the <num> part by the good USB number. If you have any doubt check the number available with the following command:

.. code-block:: bash

    cd /dev
    find -name ttyUSB*

After connecting to the board with :code:`tio`. You see a line asking for a password.
The password is `root` when developping. Once you enter this password, you should be connected to the board as root.  

Congratulation, you are connected to your device ! 

Ethernet connection
*******************
 
With an Ethernet connection, you can connect to the board using the :code:`ssh`. You can also copy files from your computer to your device using :code:`scp`. 

To create this connection, first use an Ethernet cable to link your device and your PC. 


.. in Ubuntu. If you are not using Linux, you can follow how to install Phytec virtual Machine:

.. #. In the Unity-panel (left side of your desktop) click on the Ubuntu logo (topmost icon).
.. #. The Ubuntu dashboard will open; enter System Settings in the search field (you will see the corresponding icon showing up already during typing of the search string).
.. #. Open System Settings and click on the Network icon.
.. #.  Select the physical interface to which you have connected the Ethernet cable (if you have more than one network in the list) and click on Options.
.. #. Select the IPv4Settings (E) tab and choose Manual (F) in the Method drop down box.
.. #. Click Add (G) and enter the IP address 192.168.3.10 (H) and 255.255.255.0 as subnet mask (I) and 192.168.3.10 as gateway (J).
.. #. Last, click on Save (K) to save these connection settings and close the windows.

.. You are now ready to test the Ethernet network connection.

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

You can do it on your own with the :code:`ifconfig` or :code:`idk`. 

Otherwise, here are the setps to configure the Ethernet connection on Ubuntu. 
If you are not using Ubuntu but want still stay close to this tutorial, you can install and use a PHYTEC Virtual Machine. 

To configure the IPv4 device information on Ubuntu you need to:

#. Search "network" in the applications (Windows key to access the search bar on Ubuntu)
#. Select the Ethernet port used by the connection
#. Go to IPv4 setting 
#. Select the :code:`Manual` method and add a new adress with the information available in the :ref:`previous table <Device ip info table>`.

To test the connection, you can do :

.. code-block:: bash

    ping 192.168.3.11

WARNING:  Your device need to be turned on when you test your connection ! 

If you receive the packets of data then congratulation, you are connected !

Sources
-------

If you want to learn more on how to install the image on the board or how to configure the display, please check the `phyCORE-i.MX 8M Plus BSP Manual <https://www.phytec.de/cdocuments/?doc=mwDRJw&__hstc=12841640.7b3cea865c20ac90f4f0261768fbccc3.1685517610384.1685602240432.1685687289043.7&__hssc=12841640.1.1685687289043&__hsfp=2239254415&_ga=2.132368782.1467000783.1685517610-576238176.1685517609#L1017e-A5phyCOREi-MX8MPlusBSPManual-phyBOARD-PolluxComponentsphyBOARD-PolluxComponents>`_.
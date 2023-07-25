Installation
============

Product : Imx8mp 
-----------------

The first step is to setup the device. For that you need: 

* SD Card (and an adaptator if needed for your computer)
* power adapter +24V
* Ethernet cable 
* USB-A to USB-B Micro Cable 
* [optional] USB camera (WebCam)

For the display, you have two choices:

* HDMI cable with basic screen 
* LVSD screen with cables 

To see how to connect the cables, please refer to `this document for the i.MX8MP product <https://www.phytec.de/fileadmin/phytec_base/images/01-Produkte/Component-Placement/L1025e.A0-phyBOARD-Pollux_iMX8M-Plus_web.pdf>`_.

#. Connect the USB cable to your host PC and the Debug FTDI (X1).
#. Set the Boot Mode DIP Switch (S3) to SD Card (Figure 1).
#. Insert the USB drive into the host PC.
#. Power up the phyCORE-i.MX 8M Plus.
#. Connect the power adapter (+24 V DC) to the power supply connector (X23).
#. Turn your power supply on.

.. image:: images/board-front.png
  :width: 600
  :alt: board-front
  :align: center


Downloading a bootable image in the sd card 
--------------------------------------------

The first step is to download the image. To do that use the following command: 

.. code-block:: bash

    wget my_image_url.de 

You should have in your folder a file named :code:`my_image_url`. 

Everything you need for this tutorial is installed on this image already. 
If you want to personalize this image or add new package using yocto, you see how to do it with First steps with Yocto (link).

Once the file download on your computer, you need to copy it on the sd card. 
To do that, you first need to find the name of your sd card.

On linux, you have two ways to find the name of your sd card: :code:`dmseg` or :code:`other method`.

Once you have the name of your sd card, you need to unmount the partitions. The name of partitions is as follow `/dev/mysdcard0p1` with `p1` indicating the first partition. 
To unmount a partition use the following command: 

.. code-block:: bash

    unmount /dev/mysdcard0p1

Once **ALL** you partitons are removed, you can copy the image, you can copy it using the dd command:

.. code-block:: bash

    dd command 

.. warning:: the warning in the documentation 


Your SD Card is now ready to be used !

Assembling the Board
---------------------

You need to connect the following:

* the serial cable with your computer
* the power cable to the board 
* the ethernet cable to your computer (to use ssh connection between the two devices)

Add image or gif here to show how to do that ! 

Final steps
------------

Add the sd card to the board and power it. 
You should see the Linux Logo and then the kivy demo starting. 

If you want to connect to the target (the board) you can do that via the serial connection. 

First, install tio with the following command: 

.. code-block:: bash

    sudo apt install tio


Then launch: 

.. code-block:: bash

    tio /dev/ttyUSB<num>

You need to replace the <num> part by the good USB number. 

You should then access the board and be able to the the following line 
    First line on the board 

The password is `root` when developping. 

You can then play with your device ! 

You can for example try: python3, import kivy. 

Support
--------

If you have any question or something is not working, please contact us at the email adresse 
We would also very much appreciate your feedback on this documentation. You can give it to use using the following link: 


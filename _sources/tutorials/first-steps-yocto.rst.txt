First Steps with Yocto
======================

Installing the BSP
------------------

1. Start by creating a new project folder on your host machine: 

.. code-block:: bash 

    $ mkdir ~/yocto

2. Install :code:`phyLinux` inside the new folder:

.. code-block:: bash 

    # 1. Download the file
    $ wget https://download.phytec.de/Software/Linux/Yocto/Tools/phyLinux`

    # 2. Change the access mode to be able to launch the program
    $ chmod u+x phyLinux

    # 3. Link python2 to python3 temporarily
    $ ln -s which python2 python && export PATH=pwd:$PATH` 


3. Run phyLinux with :code:`./phyLinux init` and select the needed parameters for your device. Alternatively, use command-line arguments for settings. For example:

.. code-block:: bash 
    
    $ MACHINE=phyboard-mira-imx6-3 ./phyLinux init -p imx6 -r BSP-Yocto-Ampliphy-i.MX6-PD21.1.0

Choose parameters for the machine, platform, and release. After initialization, important notes and build process information will be displayed.

After the execution of the init command, :code:`phyLinux` will print a few important notes as well as information for the next steps in the build process.
For more information about :code:`phyLinux`, you can check the `PHYTEC Yocto Reference Manual <https://www.phytec.de/cdocuments/?doc=UIHsG>`_.


Start the Build
----------------

After you download all the metadata with :code:`phyLinux init`, you have to set up the shell environment variables. 
This needs to be done every time you open a new shell.  

From the root of your project directory type:

.. code-block:: bash 

    $ source sources/poky/oe-init-build-env

The shell's working directory should change to :code:`build/`. 

Before building for the first time, you should take a look at the main configuration file, your local modifications for the current build are stored here. 

.. code-block:: bash 

    $ nano conf/local.conf

Depending on the SoC, you might need to accept license agreements. For some images using Freescale/NXP you have to uncomment the corresponding line.

.. code-block:: bash 

    # Uncomment to accept NXP EULA                                                   
    # EULA can be found under ../sources/meta-freescale/EULA                         
    ACCEPT_FSL_EULA = "1"

Now you are ready to build your first image. We suggest starting with our smaller non-graphical image :code:`phytec-headless-image` to see if everything is working correctly:

.. code-block:: bash
    
    $ bitbake phytec-headless-image

The initial build might take around about 40 minutes on a modern Intel Core i7. All subsequent builds will use the filled caches and should take about 3 minutes.

Installing the Image on a SD card
----------------------------------

If the build worked, find the images in:

.. code-block:: bash

    cd yocto/build/deploy/images/<MACHINE>

Copy the files with :code:`.sdcard` or :code:`.wic` extensions onto the SD card. To find them, you can use the command :code:`find`:

.. code-block:: bash 

    find -name "*.wic"

Like in the :ref:`tutorials/installation:Downloading a bootable image on the SD card` tutorial, you have to unmout the partitions and then copy the image on the SD Card. For example:

.. code-block:: bash 

    #unmount partitions of the SD Card
    umount /dev/mmcblk0p1
    umount /dev/mmcblk0p2

    #Copy the image on the SD Card called mmcblk0
    sudo dd if=phytec-kivydemo-image-phyboard-pollux-imx8mp-3.wic of=/dev/mmcblk0 bs=1M conv=fsync

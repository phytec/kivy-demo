First steps with Yocto
======================

Installing the BSP
------------------

1. Create a new folder for your project in your host machine : 

.. code-block:: bash 

    $ mkdir ~/yocto

2. Install :code:`phyLinux` inside the new folder.

   #. Download the file : :code:`wget https://download.phytec.de/Software/Linux/Yocto/Tools/phyLinux`
   #. Change the access mode to be able to launch the program with :code:`chmod u+x phyLinux`
   #. Link python2 to python3 temporarily: :code:`ln -s which python2 python && export PATH=pwd:$PATH` 


3. Run phyLinux from the new folder with :code:`./phyLinux init`. If you do not want to use the selector, phyLinux also supports command-line arguments for the several settings:

.. code-block:: bash 
    
    host$ MACHINE=phyboard-mira-imx6-3 ./phyLinux init -p imx6 -r BSP-Yocto-Ampliphy-i.MX6-PD21.1.0

You need to choose 3 parameters for the BSP you are going to work on:

* the machine 
* the plateform
* the release

After the execution of the init command, :code:`phyLinux` will print a few important notes as well as information for the next steps in the build process.


For more information on the :code:`phyLinux` file, you can check the `PHYTEC Yocto Reference Manual <https://www.phytec.de/cdocuments/?doc=UIHsG>`_.


Start the Build
----------------

After you download all the metadata with :code:`phyLinux init`, you have to set up the shell environment variables. This needs to be done every time you open a new shell for starting builds. 
We use the shell script provided by Poky in its default configuration. 

From the root of your project directory type:

.. code-block:: bash 

    $ source sources/poky/oe-init-build-env

The current working directory of the shell should change to :code:`build/`. 

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

The first compile process takes about 40 minutes on a modern Intel Core i7. All subsequent builds will use the filled caches and should take about 3 minutes.

Installing the image on a SD card
----------------------------------

If everything worked previously, the images should be found under:

.. code-block:: bash

    cd yocto/build/deploy/images/<MACHINE>

You can copy on the SD card the files with the extension :code:`.sdcard` or :code:`.wic`. To find them, you can use the command :code:`find` like that:

.. code-block:: bash 

    find -name "*.wic"

Like in the :ref:`tutorials/installation:Downloading a bootable image on the SD card` documentation, you have to unmout the partitions and copy the image you found with:

.. code-block:: bash 

    sudo dd if=phytec-headless-image-<MACHINE>.sdcard of=/dev/<your_device> bs=1M conv=fsync

Understanding the Yocto structure
----------------------------------

More on yocto:

* source bitebake - you are then in build 

Okay, we have two main folder :

* build 
* sources 

In build, you have: 

* a conf folder with three files (I know 2 - local.conf and bblayer.conf)
* the image for your product 
* tmp folder where you can see all the result in your recipe

Note: a bit tricky but I think the main thing to understand with yocto is that it is kind of a mega parser. It goes on, parse the update files and check what you have on your cache. A lot of stuff are done implicilty, for example if you follow the structure of the recipe folder, you can easily add bbappend in another parent folder without any problem. And some config are going to overlap over each other. It can be quite confusing sometimes. One of the best tools to use in yocto are : `find`, `grep` and `tree`. They can show interesting informations about the structure of your code in the sources folder. 

Here is the structure inside a yocto project: 

* layer 
* recipe (files, patches, ... )

You have multiple layers, and it's not because some recipes or layers are inside your source folder that bitebake is going to compile and package them. No you have to add them

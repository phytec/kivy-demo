First steps with Kivy
=====================

Introduction
------------

Kivy is an open-source library that offers a graphical user interface (GUI) framework. 
It works across various platforms, such as Linux, MacOS, Windows, as well as mobile devices and embedded systems (including Raspberry Pi or i.MX8MP). 

The advantage of Kivy is that it allows you to create GUI applications on your computer and export it directly on the target.
That way, you can avoid the complexity of cross-compilation or Yocto.

Setup the environment on you computer
--------------------------------------

Begin by installing the appropriate version of Kivy on your computer:

.. code-block:: bash
    
    # install kivy
    pip install kivy=2.1.0dev0

If you're planning to package your program you need to use Python virtual environment. 
For more information on the subject, check `Python documentation for virtual environment <https://docs.python.org/3/library/venv.html>`_

**WARNING** The providers you are using on your computer and on your board are probably going to be different, you need to check regularly that your file is working correctly on the board.

**NOTE** If you're using a virtual environment, remember to restart it each time you return to your project.

To check your setup, run the following Python code:

.. code-block:: python
    
    import kivy
    kivy.require('2.1.0') # replace with your current kivy version !

    from kivy.app import App
    from kivy.uix.label import Label


    class MyApp(App):

        def build(self):
            return Label(text='Hello world')


    if __name__ == '__main__':
        MyApp().run()

If no errors occur, go to the next step. 
Otherwise, please check `the Kivy documentation: Getting started <https://kivy.org/doc/stable/gettingstarted/intro.html>`_. 

Kivy tutorial: Ping Pong Game
------------------------------

Follow the Ping Pong tutorial
*******************************

If you want to understand how Kivy work, you can follow `this fantastic tutorial <https://kivy.org/doc/stable/tutorials/pong.html>`_. It provides detailed, step-by-step instructions. 
Alternatively, you can directly download the `files inside the Pong folder <https://github.com/kivy/kivy/tree/2.2.0dev0/examples/tutorials/pong>`_. 

**WARNING** Make sure you're using **version 2.1.0** of Kivy, not the latest version, when checking the `Github repository of Kivy <https://github.com/kivy/kivy/tree/2.2.0dev0>`_ or the `Documentation of Kivy <https://kivy.org/doc/stable/>`_.

Install your files on the target
*********************************

Once you have the necessary files for the Pong game, test them on your computer. If they work, the next goal is to install the files on your target device. 

#. Setup the Ethernet connexion (check :ref:`tutorials/installation:Ethernet connection` for more indication)
#. Use scp to copy the file on the target (you can check :ref:`faq:How to use scp command ?`)
#. Connect to the target via :ref:`Serial connection or Ethernet connection <tutorials/installation:Getting connected to the target>`
#. Once logged in, launch your program. For example, if your main program (with the App object) is named :code:`main.py`, run:

.. code-block:: bash

    python3 main.py 

You should see the game running on your target.

**WARNING**: Make sure your display is connected to the board. You can check the :code:`weston.init` file in the target file to see if your display is setup as :code:`current`. 
If needed, you can change that setting and reboot your device. 

Configuration of Kivy
----------------------

Once installed, you can configure Kivy to meet your need. 

Here are some useful options already setup thanks to the :code:`kivyconfig.sh` file:

* **mouse**: you need to tell Kivy to disable the mouse input when you touch the screen with :code:`disable_on_activity`
* **fullscreen**: you need to use :code:`auto` to adjust automaticaly the size of the windows. By default, it is going to be fullscreen. 
* **keyboard**: use the :code:`systemanddock` option to add a tactile keyboard in Kivy at the bottom of you window when you want to type something.
* :code:`LIMIT_EGL`: set this option to 1 to avoid bad surprise due to EGL usage on the board.  

To change of check the config options of Kivy, check the :code:`.kivy/conf.ini` file.

You can also define those configuration parameters with environement variables: 

.. code-block:: bash

    export KCFG_KIVY_FULL_SCREEN=auto KIVY_GLES_LIMITS=1

For more information, you can check `the Kivy documentation on Configuration object <https://kivy.org/doc/stable-2.1.0/api-kivy.config.html>`_. 

**WARNING** Make sure your touch screen works correctly by configuring fullscreen and mouse options.



Conclusion
-----------

To install your Kivy program on the target: you need to:

#. Develop on your computer an application
#. Copy the files on the target
#. Test them on the board

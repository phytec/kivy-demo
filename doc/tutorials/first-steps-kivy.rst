First steps with Kivy
=====================

Introduction
------------

Kivy is an open source library used to provide GUI interface. 
It is crossplateform, which means that it can be used on all kind of OS such as Linux, MacOS, Windows, but also on other device like phone (Android or IOS) and embedded devices (RaspberryPi or Imx8mp).

The advantage is that you can easily start a GUI application without worrying about corss-compilation or Yocto. 

That's what we are going to do in this tutorial !

Setup the environment on you computer
--------------------------------------

The first step is to install the good version of kivy on you computer. To do that, do the following:

.. code-block:: bash
    
    # create a new folder for your project
    mkdir My_project
    cd My_project
    
    # install kivy
    pip install kivy=2.1.0dev0

If you plan to make a service and package your program, you should work in a Python virtual environment. For more information on the subject, check `Python documentation for virtual environment <https://docs.python.org/3/library/venv.html>`_

**WARNING** The providers you are using on your computer and on your board are probably going to be different, please check regularly that your file is working correctly on the board too.

**NOTE** If you are using a virtual environment, each time you go back to your project, you need to restart your environment !

Try the following python code to check that everything is working as it should on your computer.

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

If no error occurs, then you can go to the next step. 
Otherwise, please check `the Kivy documentation: Getting started <https://kivy.org/doc/stable/gettingstarted/intro.html>`_. 

Kivy tutorial: Ping Pong Game
------------------------------

To understand how kivy work, you can follow `this fantastic tutorial <https://kivy.org/doc/stable/tutorials/pong.html>`_. Every steps are detailed and well-explained. 
However if you don't want to spend too much time with the tutorial, you can simply download the following files: link to the game. 

The first step is to check if it is working on you computer. If that's the case, our next goal is to install the files in your target. 

First, start the board. You should end up with a demo starting. You can exit the application clicking the top right button. 

To install your file on the target you need to :

#. Connect on the target via serial connection with tio (if you are not sure about this part, please check :ref:`tutorials/installation:Serial connection`)
#. Setup the ethernet connexion (check :ref:`tutorials/installation:Ethernet connection` for more indication)
#. Use scp to copy the file on the target ()
#. Launch it from the target 

For the last step, if your main program (the one with the App object) is named :code:`main.py` you need to do:

.. code-block:: bash

    python3 main.py 

You should see the game working on your target.

If you want to see the game in full screen or change some configuration please check the next section. 
If the device is not detected, please check that one screen is connected or change the weston init file. For more information check the PHYTEC documentation ...

Configuration of kivy
----------------------

The game is working, but you want to play with a friend and realise that having the fullscreen can be useful.
You can do that using the configuration of Kivy. 

Here are some useful config option:

* mouse: you need to tell Kivy to disable the mouse input when you touch the screen
* fullscreen:  
* keyboard: use the systemanddock to add a tactile keyboard in Kivy
* LIMIT EGL: set this part to 1 to avoid bad surprise 

To do that, go to the :code:`.kivy/conf.ini` file and change the following:

.. code:: python

    mouse = mouse, disable_on_activity
    full_screen=auto
    gles_limits=1
    keyboard=systemanddock


There are several way to change the configuration in Kivy. The easiest one is to change the .kivy/conf.ini file. 

You can also define those configuration parameters with environement variables like that: 

.. code-block:: bash

    export KCFG_KIVY_FULL_SCREEN=auto KIVY_GLES_LIMITS=1

For more information, you can check `the Kivy documentation on Configuration object <https://kivy.org/doc/stable-2.1.0/api-kivy.config.html>`_. 

**WARNING** For the touch screen to work properly, you need to configurate the following parameters: fullscreen and mouse.



Conclusion
-----------

If you want to install your own kivy program on the target, you need to:

#. Develop on your computer an application
#. Copy the files on the tarfet
#. Test them on the board

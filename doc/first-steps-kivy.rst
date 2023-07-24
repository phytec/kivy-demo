First steps with Kivy
=====================

Introduction
------------

Kivy is an open source library used to provide GUI interface. 
It is crossplateform, which means that it can be used on all kind of OS such as Linux, MacOS, Windows, but also on other device like phone (Android or IOS) and embedded devices (RaspberryPi or Imx8mp).

The advantage is that you can easily start a GUI application. Without worrying about corsscompilation or Yocto. 

That's what we are going to do in this tutorial !

Setup the environement on you computer
--------------------------------------

The first step is to install the good version of kivy on you computer. To do that, do the following:
1. create a new folder 
2. virtual env 
3. install kivy=2.1.0dev0 and other dependencies 

.. note:: each time you go back to your project, restart the virtual environement with: ...

If you want to deactive the virtual env, do ...

Try the following python code ... to check that everything is working as it should. If no error occurs, then you can go to the next step. 
Otherwise, please check that ... or contact us here. 

Follow the first Kivy tutorial: Ping Pong Game
-----------------------------------------------

To understand a little how kivy work, you can follow this fantastic tutorial. Every steps are detailed and explained. 
If you don't want to spend too much time with the tutorial, you can simply download the following files: link to the game. 

The first step is to check if it is working on you computer. If that's the case, our next goal is to install the files in your target. 

To do that, do the following:
1. Connection with tio
2. Setup the ethernet connexion 
3. Use scp to copy the file on the target
4. Launch it from the target 

You should see the game working on your computer. 

Configuration of kivy
----------------------

The game is working, but you want to play it with a friend and realise that having the fullscreen can be useful.
You can do that using the configuration of kivy. 

Here are some useful config option:
- keyboard 
- mouse
- fullscreen 
- LIMIT EGL

For more information, you can check this page in the kivy documentation. 

If you don't want to think to much, you can do the following:
.. code-block:: bash
    export my_option1=1 myoption2=2 ...

.. note:: for the touch screen to work properly, you need to do the following: fullscreen and mouse 

Conclusion
-----------

If you want to install your own kivy program on the target, you need to:
1. develop in your virtual environement
2. copy the files using scp 
3. try them on the board

Warning
--------

- The virtual environement work for the basic stuff, but not for the camera for example, those need to be tested on the board directly 
- Some warnings present in the computer are removed in the target, it is normal (patch added in the image)
- 
Camera with Kivy 
================

How to run the demo with the camera
-----------------------------------

The camera is not able by default on the demo. In fact, if you do not provide a camera before starting the dom with the video enable, you will end up with an error.

Important infos 
---------------

Two providers have been tested:

* gstreamer (with patch): already installed, used for images and videos
* opencv (with patch): a lot of features available in opencv 

WARNING: If you want to use opencv, you need to install it on the board (if you're not sure how to do it, check :ref:`tutorials/yocto-pip`)

One type of camera has been tested:

* USB camera

If you try other type of cameras
---------------------------------

If you tested another type of camera or provider and made it work, feel free to add it to this documentation by opening an issue.

If it's not working, you can check the camera folder in the core part of the Kivy repository to understand how it work. 



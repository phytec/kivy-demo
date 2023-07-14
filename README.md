# Demo Kivy 

## Description

The goal of this program is to show the possibilities of kivy on embedded systems developped by PHYTEC. 
This program was tested after installing kivy using this documentation: [link to the documentation with title]


## Installation 

Dependencies: 
- kivy 2.1dev0
- gstreamer 

To install and launch the program : 
1. Go inside the project folder
1.1. [OPTIONAL] Install and start a virtual environnement: `python -m venv .venv` and ` source .venv/bin/activate`
2. Install the package: `pip install --editable .`
3. Launch the program with: `kivydemo`

If you use the the image with meta-phykivy, you just have to follow the last step.

> NOTES: if you want to test the video player on your virtual environment, you need to have at least one of the provider for video available. If that's not the case, you can can do the following 
> ```(myenv)$ pip install ffpyplayer```

For the camera, no idea how to make it work in the virtual environment for the moment. 

## Credits

To make the program, we used the following examples available on the kivy repository or visible on the documentation: 
- [touchtracer](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/demo/touchtracer) 
- [showcase](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/demo/showcase)
- [3D rendering (renamed MonkeyRendering)](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/3Drendering) 
- [camera](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/camera)

## LICENSE 

This code is under the MIT license. See `LICENSE` for the full terms and conditions.

Images, videos and fonts can have a different license. See the different license in the folder for each resources. 
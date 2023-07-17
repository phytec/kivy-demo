# Demo Kivy 

![Test kivydemo](https://github.com/MarineVovard/kivy-demo/actions/workflows/python-package.yml/badge.svg)

## Description

This program demonstrates the capabilities of Kivy on embedded systems developed by [PHYTEC](https://www.phytec.eu/en/startseite/). It serves as a showcase for Kivy's features and functionalities. Please refer to the [documentation](link to the documentation for later) for instructions on installing Kivy on PHYTEC products before running this program.

## Installation 

Dependencies: 
- kivy[full]==2.1dev0

Follow these steps to install and launch the program:
1. Go to the project folder
2. Set up and activate a virtual environment:: `python3 -m venv .venv` and `source .venv/bin/activate`
3. Install the package: `pip install --editable .`
4. Launch the program with the following command: `kivydemo`

If you are using the `meta-phykivy` layer, you can skip to the last step.

> NOTE: If you want to test the camera in your virtual environment, make sure you have at least one camera provider available. If not, you can install OpenCV by running the following command
> ```(myenv)$ pip install opencv-python``` 

> NOTE: To exit the virtual environment, you can use the `deactivate` command. For more information, refer to [this link](https://docs.python.org/3/library/venv.html)

## Credits

This program was developed using the following examples from the Kivy repository and documentation:
- [touchtracer](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/demo/touchtracer) 
- [showcase](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/demo/showcase)
- [3D rendering (renamed MonkeyRendering)](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/3Drendering) 
- [camera](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/camera)

## LICENSE 

This code is under the MIT license. See `LICENSE` for the full terms and conditions.

Images, videos and fonts can have a different license. See the different license in the folder for each resources. 
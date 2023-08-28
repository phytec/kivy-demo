# Demo Kivy 

![Test kivydemo](https://github.com/MarineVovard/kivy-demo/actions/workflows/kivydemo-workflow.yml/badge.svg)

## ✨ Description

This program demonstrates the capabilities of Kivy on embedded systems developed by [PHYTEC](https://www.phytec.eu/en/startseite/). It serves as a showcase for Kivy's features and functionalities. Please refer to the [documentation](link to the documentation for later) for instructions on installing Kivy on PHYTEC products before running this program.

## 🛠️ Installation 

Dependencies: 
- kivy[full]==2.1dev0

Follow these steps to install and launch the program:
1. Go to the project folder
2. Set up and activate a virtual environment: `python3 -m venv .venv` and `source .venv/bin/activate`
3. Install the package: `pip install --editable .`
4. Launch the program with the following command: `kivydemo`

If you are using the `meta-phykivy` layer, you can skip to the last step.

If you want to try the demo with the camera, use the following command: `kivydemo -- --camera`. 
To use the audio, do: `kivydemo -- --audio`

> NOTE: If you want to test the camera in your virtual environment, make sure you have at least one camera provider available. If not, you can install OpenCV by running the following command
> ```(myenv)$ pip install opencv-python``` 

> NOTE: To exit the virtual environment, you can use the `deactivate` command. For more information, refer to [this link](https://docs.python.org/3/library/venv.html)

## 👥 Credits

This program was developed using the following examples from the Kivy repository and documentation:
- [touchtracer](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/demo/touchtracer) 
- [showcase](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/demo/showcase)
- [3D rendering (renamed MonkeyRendering)](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/3Drendering) 
- [camera](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/camera)
- [audio](https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/audio)

## 📝 Documentation 

We are using [Sphinx](https://www.sphinx-doc.org/en/master/) and [Read the doc's template](https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html) to document this project. Here are the steps to build the documenation.

1. Go to the doc folder 
2. Build the html files: `make html`
3. The files are in the `_build` folder, you can launch the generated files in a browser with : `firefox _build/html/index.html`

You can also check if all the links in the documentation are working with: `make linkcheck`.


## 📜 LICENSE 

This code is under the MIT license. See `LICENSE` for the full terms and conditions.

Images, videos and fonts can have a different license. See the different license in the folder for each resources. 

3D Phytec Logo made by Manon Girard (https://manon_girard.artstation.com/) and licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

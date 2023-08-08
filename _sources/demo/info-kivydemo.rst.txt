Demo Kivy 
=========

This program demonstrates the capabilities of Kivy on embedded systems developed by `PHYTEC <https://www.phytec.eu/en/startseite/>`_. 
It serves as a showcase for Kivy's features and functionalities. Please refer to the :doc:`/tutorials/installing-kivy-layer` for instructions on how to install Kivy on PHYTEC products before running this program.

Installation 
------------

Dependencies: 

* kivy[full]==2.1dev0

Follow these steps to install and launch the program:

#. Go to the project folder
#. Set up and activate a virtual environment: :code:`python3 -m venv .venv` and :code:`source .venv/bin/activate`
#. Install the package: :code:`pip install --editable .`
#. Launch the program with the following command: :code:`kivydemo`

If you are using the :code:`meta-phykivy` layer, you can skip to the last step.

If you want to try the demo with the camera, use the following command: :code:`kivydemo -- --camera`. 
To use the audio, do: :code:`kivydemo -- --audio`

**NOTE** If you want to test the camera in your virtual environment, make sure you have at least one camera provider available. If not, you can install OpenCV by running the following command
 
.. code-block:: bash

    (myenv)$ pip install opencv-python 

**NOTE** To exit the virtual environment, you can use the :code:`deactivate` command. For more information, refer to `the virtual environment documentation <https://docs.python.org/3/library/venv.html>`_

Credits
-------

This program was developed using the following examples from the Kivy repository and documentation:

* `Touchtracer <https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/demo/touchtracer>`_
* `Showcase <https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/demo/showcase>`_
* `3D rendering (renamed MonkeyRendering) <https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/3Drendering>`_
* `Camera <https://github.com/kivy/kivy/tree/2.1.0.dev0/examples/camera>`_

LICENSE 
-------

This code is under the MIT license. See :code:`LICENSE` for the full terms and conditions.

Images, videos and fonts can have a different license. See the different license in the folder for each resources. 

3D Phytec Logo made by Manon Girard and licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.
Frequently Asked Questions
==========================

Yocto - How to import files from a git repository ?
----------------------------------------------------

To add sources using git, you need to: 

#. Get the url of your repo and remove the https part.
#. Add the new source to your recipe (you can precise the protocol and the branch): :code:`SRC_URI = "git://github.com/MarineVovard/kivy-demo;protocol=https;branch=main"`
#. Add `SRCREV` with the commit number you want to use: :code:`SRCREV = "a1d631d82f761ce78bfb4bdaeed9f673f4a3bed4"`

Bake your recipe and voilà !
Now, you just need to update the :code:`SRCREV` to have the commit you want !

For more information check the `Yocto Manual <https://docs.yoctoproject.org/index.html>`_.

**WARNING** The repo needs to be public

How to use Vim (and vi) commands ?
----------------------------------

Each time you want to use a command, do first ESC. 

* to exit: :code:`:q!`
* to modify (insert): :code:`i`
* to undo: :code:`u`
* to save: :code:`:w`
* to save and exit: :code:`:wq`

If you want to learn more commands check `An introduction to the vi editor made by RedHat <https://www.redhat.com/sysadmin/introduction-vi-editor>`_.

How to use scp command ?
-------------------------

Scp stand for secure copy protocol. It enables you to copy a file to or from an other machine. 

Here are some useful commands:

* Copy file from remote host: :code:`scp user@remotehost:myfile.txt /my/local/directory`
* Copy file to the remote host: :code:`scp myfile.txt user@remote:/remote/directory`
* can use the option :code:`-r` fo recursive copy and :code:`-P` for the port

If you want to learn more, you can check `Example syntax for Secure Copy <https://www.hypexr.org/linux_scp_help.php>`_ or check the man.


How to test your Python package on your computer ?
---------------------------------------------------

#. Create a virtual environment: :code:`python3 -m venv .venv`
#. Launch the virtual environnement with :code:`source .venv/bin/activate`
#. Install your package: :code:`pip install --editable .`

You can also uninstall your package with: :code:`pip uninstall <mypackage>`.

How to manage services in Linux ?
---------------------------------

* List of services: :code:`systemctl`
* List of failed services: :code:`systemctl list-units --failed`
* To see the log of a service: :code:`journalctl -u <mywonderful.service>`
* Restart a service: :code:`systemctl daemon-reload`
* Start a service: :code:`systemctl start <mywonderful.service>`


Yocto - How to create a new layer ?
-----------------------------------

#. Start bitbake: :code:`source sources/poky/oe...-env`
#. Create layer: :code:`bitbake-layers create-layer meta-sdltest`
#. Move the repo in sources: :code:`mv meta-sdltest ../sources/`
#. Add the new layer inside the config file: :code:`nano confi/bblayers.conf` and add at the end :code:`BBLAYERS += "${BSPDIR}/sources/meta-sdltest "`
#. Check if the layer is added:  :code:`bitbake-layers show-layers`

For more information, check `How to add a new layer and a new recipe in Yocto <https://community.nxp.com/t5/i-MX-Processors-Knowledge-Base/How-to-add-a-new-layer-and-a-new-recipe-in-Yocto/ta-p/1102230>`_. 

How to add a tactile keyboard to your kivy app ?
------------------------------------------------

To add the keyboard with kivy: :code:`systemanddock` or :code:`systemandmulti`
(:code:`KCFG_KIVY_KEYBOARD_MODE` env variable).

Check the `Configuration object in the Kivy documentation <https://kivy.org/doc/stable/api-kivy.config.html>`_.
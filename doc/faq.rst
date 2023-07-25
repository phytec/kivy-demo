FAQ
===


To solve the problem with the touch 
-----------------------------------

Add that to the ```.kivy/config.ini``` file part input:
```
mouse = mouse,disable_on_activity
```

To make everything work: 

- KIVY_FULL_SCREEN=auto
- KIVY_GLES_LIMITS=1 


Import repo from git - yocto 
----------------------------

In the recipe, I tried https and ssh protocol but was able to do something only with https. 

.. warning:: The repo needs to be public

Two steps to make it work (well 3 in fact):

1. Get the url of your repo and remove the https part : 
2. Add the new source (you can precise the protocol and the branch): :code:`SRC_URI = "git://github.com/MarineVovard/kivy-demo;protocol=https;branch=main"`
3. Add `SRCREV`, ie le numero du commit que tu veux récupérer: `SRCREV = "a1d631d82f761ce78bfb4bdaeed9f673f4a3bed4"`

Bake your recipe and tada !
Now, just need to update the `SRCREV` to have a new version of code !

Vim (and vi) commands 
---------------------

- to exit: :code:`:q!`
- to modify (insert): :code:`i`
- to save: :code:`:w`
- to save and exit: :code:`:wq`

Other commands: https://www.redhat.com/sysadmin/introduction-vi-editor

scp command
-------------

- Copy file from remote host: :code:`scp user@remotehost:myfile.txt /my/local/directory`
- Copy file to the remote host: :code:`scp myfile.txt user@remote:/remote/directory`
- can use the option :code:`-r` fo recursive copy and :code:`-P` for the port

https://www.hypexr.org/linux_scp_help.php


Packaging Python programs 
-------------------------

- launch virtual environnement: :code:`source .venv/bin/activate`
- install my package: :code:`pip install --editable .`
- uninstall my package: :code:`pip uninstall <mypackage>`

Services
---------

- list of service: :code:`systemctl`
- list of failed services: :code:`systemctl list-units --failed`
- To see the log of a service: :code:`journalctl -u <mywonderful.service>`
- restart service: :code:`systemctl daemon-reload`
- start a service: :code:`systemctl start <mywonderful.service>`


Yocto - create layer and recipe 
-------------------------------

1. Start bitbake: :code:`source sources/poky/oe...-env`
2. Create layer: :code:`bitbake-layers create-layer meta-sdltest`
3. Move the repo in sources: :code:`mv meta-sdltest ../sources/`
4. Add the new layer inside the config file: :code:`nano confi/bblayers.conf` and add at the end :code:`BBLAYERS += "${BSPDIR}/sources/meta-sdltest "`

.. note:: Tried with `bitbake-layers add-layer meta-sdltest` but didn't work well (not good directory). So just add it in the config file

5. Check if layer added:  :code:`bitbake-layers show-layers`

https://community.nxp.com/t5/i-MX-Processors-Knowledge-Base/How-to-add-a-new-layer-and-a-new-recipe-in-Yocto/ta-p/1102230 

Keyboard 
--------

To add the keyboard with kivy: :code:`systemanddock` or :code:`systemandmulti`
(:code:`KCFG_KIVY_KEYBOARD_MODE` env variable)

Other
-----

- **Place where to change the display** : :code:`/etc/xdg/weston/weston.ini`

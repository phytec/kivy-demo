from kivy.uix.screenmanager import  Screen
from kivy.lang.builder import Builder

from subprocess import check_output
from os import uname

from kivy.properties import StringProperty
 

class InfoScreen(Screen):
    
    phytec_description = StringProperty("We have been developping and manufacturing embedded components for reliable electronic series product for more than 30 years.\n\nOur products and services shorten your time to market, reduce your developpement costs and your risk int the developpement and production of industrial embedded. \n\nFor more information, check our website at ... !")
    device_description = StringProperty("")

    def __init__(self,*args, **kwargs):
        Builder.load_file("info/infoScreen.kv")
        super().__init__(*args, **kwargs)
        self.device_description = self.get_device_description()
        # print(self.device_description)

    def get_info(self):
        infos = []
        info_uname = uname()
        infos.append(['system', info_uname[0]])
        infos.append(['kernel_version', info_uname[2]])
        infos.append(['machine', info_uname[1]])
        infos.append(['architecture', info_uname[-1]])
        cmd1 = "cat /proc/cpuinfo | grep processor | wc -l"
        cmd2 = "cat /proc/meminfo | grep MemTotal | cut -d\":\" -f 2"
        try: 
            infos.append(['CPU', check_output(cmd1, shell=True).strip().decode("utf-8")])
            infos.append(['RAM', check_output(cmd2, shell=True).strip().decode("utf-8")])
        except:
            print("ERROR: commands cat /proc/cpuinfo or/and cat /proc/meminfo not valid") 

        return infos
    
    def get_device_description(self):
        infos_device = self.get_info()
        print(infos_device)
        formated_info = ["    - [b]{}:[/b] {}\n".format(key,value) for [key, value] in infos_device]
        return ''.join(formated_info)


from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

from subprocess import check_output
from os import uname, path
from kivydemo import path_demo

from kivy.properties import StringProperty


class InfoScreen(Screen):

    phytec_description = StringProperty("We have been developping and manufacturing "
                                        "embedded components for reliable electronic series "
                                        "product for more than 30 years.\n\n"
                                        "For many decades, our products have proven themselves "
                                        "under the most demanding conditions, including in medical technology"
                                        ", traffic and transport, the energy industry, avionics, building "
                                        "automation, drive technology, agricultural technology "
                                        "and the automotive industry.\n\n"
                                        "Our products and services shorten your time to market, "
                                        "reduce your developpement costs and your risk int the "
                                        "developpement and production of industrial embedded.\n\n"
                                        "For more information, check our website at[u]https://www.phytec.eu/[/u]!")
    device_description = StringProperty("")

    def __init__(self, *args, **kwargs):
        Builder.load_file(path.join(path_demo, "info/infoScreen.kv"))
        super().__init__(*args, **kwargs)
        self.device_description = self.get_device_description()

    def get_info(self):
        infos = []
        info_uname = uname()
        infos.append(['system', info_uname[0]])
        infos.append(['kernel_version', info_uname[2]])
        infos.append(['machine', info_uname[1]])
        infos.append(['architecture', info_uname[-1]])
        cmd1 = "cat /proc/cpuinfo | grep processor | wc -l"
        cmd2 = "cat /proc/meminfo | grep MemTotal | cut -d\":\" -f 2"
        infos.append(['CPU', check_output(
            cmd1, shell=True).strip().decode("utf-8")])
        infos.append(['RAM', check_output(
            cmd2, shell=True).strip().decode("utf-8")])

        return infos

    def get_device_description(self):
        infos_device = self.get_info()
        formated_info = [
            "    - [b]{}:[/b] {}\n".format(key, value) for [key, value] in infos_device]
        return ''.join(formated_info)

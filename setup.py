from setuptools import setup, find_packages
import urllib.request
import os

# Import images
# scatter, background and logo images
files = ["IMG_7942.JPG", "PHYTEC_Produkte.jpg",
         "phytec_logo_medium.png", "COPYING", "COPYING.utf8"]
url = "https://download.phytec.de/Software/Linux/Applications/Media/"


def download_file(url, file_path, file_name):
    full_path = file_path + file_name
    full_url = url + file_name
    try:
        urllib.request.urlretrieve(full_url, full_path)
    except:
        print("WARNING: file ", file_name, "fetch at ", full_url, "not working")


path_demo = os.path.dirname(__file__)
path_to_images = path_demo + '/kivydemo/images/'
for f in files:
    download_file(url, path_to_images, f)


setup(
    name='kivydemo',
    version='0.1.0',
    description='Kivy demo for Phytec Products',
    author='Marine Vovard',
    author_email='m.vovard@phytec.de',
    packages=find_packages(include=['kivydemo*']),
    package_dir={"kivydemo": "kivydemo"},
    install_requires=['kivy[full]==2.1.0.dev0'],
    entry_points={
        'console_scripts': ['kivydemo=kivydemo.main:runMainFunction']
    },
    package_data={'': ['*.kv', '*.jpg', '*.png', '*.obj', '*.glsl'],
                  "kivydemo": ["images/*"],
                  "kivydemo.audio": ["*.wav"],
                  "kivydemo.showcase": [
                      "data/images/*",
                      "data/icons/*.png",
                      "data/screens/*.kv"
    ]},
    include_package_data=True
)

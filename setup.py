from setuptools import setup, find_packages

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

from setuptools import setup, find_packages

setup(
    name='kivydemo',
    version='0.1.0',
    description='Kivy demo for Phytec Products',
    author='Marine Vovard',
    author_email='m.vovard@phytec.de',
    packages=find_packages(include=['kivydemo*']),
    install_requires=['kivy'],
    entry_points={
        'console_scripts': ['kivydemo=kivydemo.main:runMainFunction']
    },
    package_data={'': ['*.kv', '*.jpg', '*.png']}
)

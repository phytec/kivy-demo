import os

path_demo = os.path.dirname(__file__)
"""Path to DemoKivy package directory."""

path_images = path_demo+'/images'
if len(os.listdir(path_images)) <= 2:  # images folder empty except __init__ file and pycache
    path_images = '/usr/share/phytecvisuals'

# Debug
# print("Path for my images", path_images)

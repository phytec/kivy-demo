import os

path_demo = os.path.dirname(__file__)
"""Path to DemoKivy package directory."""

path_images = path_demo+'/images'
if len(os.listdir(path_images)) <= 1:  # images folder empty except __init__ file
    path_images = '/usr/share/phytecvisuals'

print("Path for my images", path_images)

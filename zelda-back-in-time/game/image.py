import arcade
from constants import *

class Image:
    def __init__(self, image_file):
        self._image_file = image_file
        
    def load(self):
        self._image = arcade.load_texture(IMAGE_DIRECTORY + self._image_file)
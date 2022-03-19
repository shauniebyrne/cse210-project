import arcade
from constants import *

class Image:
    def __init__(self, image_filename):
        self._image = arcade.load_texture(IMAGE_DIRECTORY + image_filename)

    def get_image(self):
        return self._image
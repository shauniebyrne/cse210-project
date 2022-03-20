import arcade
from game.constants import *

class Image:
    def __init__(self, image_filename):
        self._image = arcade.load_texture(IMAGES_DIRECTORY + image_filename)

    def get_image(self):
        return self._image
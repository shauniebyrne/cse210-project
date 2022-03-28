import arcade

from game.constants import *

from game.casting.image import Image
from game.casting.position import Position

class Actor:
    """
    Create what is needed for the actors in the code.
    """
    def __init__(self, image_filename, position = None):
        """
        Create a new actor using the image and position

        Arg:
            image_filename: file associated with the actors image
            position (None): position of the actor in the code
        """
        self._image = Image(image_filename)

        if position != None:
            self._position = Position(position[0], position[1])

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self._position.get_x() * IMAGE_WIDTH, self._position.get_y() * IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_HEIGHT, self._image.get_image())

    def get_position(self):
        return self._position
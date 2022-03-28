import arcade

from game.constants import *
from game.casting.actor import Actor

class Background(Actor):
    """Create the background for the levels of the game.
    
    Arg:
        type (int): Background image for level number

    Attribute:
        _type (int): Allows more than one background to be made.
    """
    def draw(self):
        """Create background with image"""
        for x in range(0, int(SCREEN_WIDTH / IMAGE_WIDTH)):
            for y in range(0, int(SCREEN_HEIGHT / IMAGE_HEIGHT)):
                arcade.draw_lrwh_rectangle_textured(x * IMAGE_WIDTH, y * IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_HEIGHT, self._image.get_image())
import arcade

from game.constants import *
from game.actor import Actor

class Background(Actor):
    def draw(self):
        for x in range(0, int(SCREEN_WIDTH / IMAGE_WIDTH)):
            for y in range(0, int(SCREEN_HEIGHT / IMAGE_HEIGHT)):
                arcade.draw_lrwh_rectangle_textured(x * IMAGE_WIDTH, y * IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_HEIGHT, self._image.get_image())
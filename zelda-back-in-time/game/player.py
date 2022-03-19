import arcade
from constants import *
from game.image import Image

class Player(Image):
    def draw(self):
        arcade.draw_lrwh_rectangle_textured(64, 64, 64, 64, self._image)
import arcade
from constants import *
from game.element import Element

class Player(Element):
    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self._point.get_x() * IMAGE_SIZE, self._point.get_y() * IMAGE_SIZE, IMAGE_SIZE, IMAGE_SIZE, self._image.get_image())
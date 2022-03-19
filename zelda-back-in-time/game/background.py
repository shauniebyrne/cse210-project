import arcade
from constants import *
from game.element import Element

class Background(Element):
    def draw(self):
        for x in range(0, int(SCREEN_WIDTH / IMAGE_SIZE)):
            for y in range(0, int(SCREEN_HEIGHT / IMAGE_SIZE)):
                arcade.draw_lrwh_rectangle_textured(x * IMAGE_SIZE, y * IMAGE_SIZE, IMAGE_SIZE, IMAGE_SIZE, self._image.get_image())
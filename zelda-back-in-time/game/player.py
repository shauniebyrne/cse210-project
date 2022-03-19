import arcade
from constants import *

class Player:
    def load(self):
        self._image = arcade.load_texture("zelda-back-in-time/assets/images/female_idle.png")

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(64, 64, 64, 64, self._image)
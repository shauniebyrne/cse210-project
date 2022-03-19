import arcade
from constants import *

from game.background import Background
from game.player import Player

class Window(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME)

    def setup(self):
        self._background = Background('tile01.png')

        self._player = Player('female_idle.png', [2, 3])

    def on_draw(self):
        self._background.draw()

        self._player.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self._player._point.get_y() <= 8:
                self._player._point.set_y(self._player._point.get_y() + 1)
        elif key == arcade.key.DOWN:
            if self._player._point.get_y() >= 1:
                self._player._point.set_y(self._player._point.get_y() - 1)
        elif key == arcade.key.LEFT:
            if self._player._point.get_x() >= 1:
                self._player._point.set_x(self._player._point.get_x() - 1)
        elif key == arcade.key.RIGHT:
            if self._player._point.get_x() <= 13:
                self._player._point.set_x(self._player._point.get_x() + 1)
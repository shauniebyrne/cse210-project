import arcade
from constants import *

from game.background import Background
from game.player import Player

class Window(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME)

        self._background = Background('tile01.png')

        self._player = Player('female_idle.png')

    def setup(self):
        self._background.load()

        self._player.load()

    def on_draw(self):
        self._background.draw()

        self._player.draw()
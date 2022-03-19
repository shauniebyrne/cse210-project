import arcade

from game.window import Window

class Director:
    def __init__(self):
        window = Window()

        window.setup()

    def start_game(self):
        arcade.run()
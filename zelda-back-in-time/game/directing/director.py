import arcade

from game.constants import *
from game.casting.background import Background
from game.casting.actor import Actor
from game.casting.level import Level
from game.casting.cast import Cast

# The Director is an inherited class of parent arcade.Window. 
# This is because in the Arcade library, the Window class does act like the "director"
class Director(arcade.Window):
    """A class that directs the game.
    
    Attribute:
        _cast (Cast): Seperate actors to create.
    """
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME)

        self._cast = Cast()

    def setup(self):
        """Create all Cast members"""
        self._background = Background('grass.png')
        self._background2 = Background('ground.png')
        self._background3 = Background('bluesky.png')

        self._level1 = Level('1.csv', self._cast)
        self._level2 = Level('2.csv', self._cast)
        self._level3 = Level('3.csv', self._cast)

        # This is the current level
        self._level = self._level1
        self._level_number = 1

        self._player = Actor('player.png', [3, 3])
        self._player2 = Actor('badguy.png', [11, 8])
        self._food = Actor('apple.png', [5, 6])
        self._food2 = Actor('cherries.png', [8, 5])
        self._key = Actor('key.png', [13, 7]) 
        self._key2 = Actor('key.png', [7, 4]) 

    def on_draw(self):
        """Draw all Cast members"""
        self._background.draw()
        self._player.draw()
        self._player2.draw()
        self._level.draw()
        self._food.draw()
        self._food2.draw()
        self._key.draw()
        self._key2.draw()

    def on_key_press(self, key, modifiers):
        """ Move player around gameboard.

        Args:
            key: Key pressed by player.
            modifiers: Necessary to make changes.
        
        """
        position = self._player.get_position()
        
        x = position.get_x()
        y = position.get_y()

        # Check if player is within the boundaries of the window
        if key == arcade.key.UP:
            if y <= 8:
                y = y + 1
        elif key == arcade.key.DOWN:
            if y >= 1:
                y = y - 1
        elif key == arcade.key.LEFT:
            if x >= 1:
                x = x - 1
        elif key == arcade.key.RIGHT:
            if x <= 13:
                x = x + 1

        if self._level_number == 1:
            if x == 0 and y == 5:
                self._level = self._level2
                self._level_number = 2
                self._player.get_position().set_x(1)
                self._player.get_position().set_y(5)
            elif x == 14 and y == 5:
                self._level = self._level3
                self._level_number = 3
                self._player.get_position().set_x(13)
                self._player.get_position().set_y(5)
        elif self._level_number == 2:
            if x == 0 and y == 5:
                self._level = self._level1
                self._level_number = 1
        elif self._level_number == 3:
            if x == 14 and y == 5:
                self._level = self._level1
                self._level_number = 1

        # Check for player collision with any elements. If there is a collision, return to prevent the collision
        for actor in self._cast.get_actors('elements'):
            if x == actor.get_position().get_x() and y == actor.get_position().get_y():
                return

        position.set_x(x)

        position.set_y(y)
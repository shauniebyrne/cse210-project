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

        self._intro = True

        self._game_over = False

        self._audio = ('LOZ_Get_Heart.wav', False)
        self._music = ('The Legend of Zelda A Link To The Past OST.mp3', False)

    def setup(self):
        self._background = Background('grass.png')

        if self._intro or self._game_over:
            return

        """Set up the game and create the cast."""

        self._level1 = Level('1.csv', self._cast)
        self._level2 = Level('2.csv', self._cast)
        self._level3 = Level('3.csv', self._cast)

        # This is the current level
        self._level = self._level1
        self._level_number = 1

        self._player = Actor('player.png', [3, 3])

        self._badguy_l1 = Actor('badguy.png', [11, 8])
        self._badguy_l1_2 = Actor('badguy.png', [8, 5])
        self._badguy_l1_3 = Actor('badguy.png', [2, 7])
        self._badguy_l1_4 = Actor('badguy.png', [6, 3])
        self._badguy_l1_5 = Actor('badguy.png', [4, 2])
        self._badguy_l1_6 = Actor('badguy.png', [5, 6])
        self._badguy_l1_7 = Actor('badguy.png', [10, 3])
        self._badguy_l1_8 = Actor('badguy.png', [1, 5])
        self._badguy_l1_9 = Actor('badguy.png', [13, 5])

        self._badguy_l2 = Actor('badguy.png', [11, 8])
        self._badguy_l2_2 = Actor('badguy.png', [8, 5])
        self._badguy_l2_3 = Actor('badguy.png', [2, 7])
        self._badguy_l2_4 = Actor('badguy.png', [6, 3])
        self._badguy_l2_5 = Actor('badguy.png', [4, 2])
        self._badguy_l2_6 = Actor('badguy.png', [5, 6])
        self._badguy_l2_7 = Actor('badguy.png', [10, 3])
        self._badguy_l2_8 = Actor('badguy.png', [1, 5])
        self._badguy_l2_9 = Actor('badguy.png', [13, 5])

        self._badguy_l3 = Actor('badguy.png', [11, 8])
        self._badguy_l3_2 = Actor('badguy.png', [8, 5])
        self._badguy_l3_3 = Actor('badguy.png', [2, 7])
        self._badguy_l3_4 = Actor('badguy.png', [6, 3])
        self._badguy_l3_5 = Actor('badguy.png', [4, 2])
        self._badguy_l3_6 = Actor('badguy.png', [5, 6])
        self._badguy_l3_7 = Actor('badguy.png', [10, 3])
        self._badguy_l3_8 = Actor('badguy.png', [1, 5])
        self._badguy_l3_9 = Actor('badguy.png', [13, 5])

        self._food1_l1 = Actor('apple.png', [4, 8])
        self._food2_l1 = Actor('cherries.png', [8, 1])

        self._food1_l2 = Actor('apple.png', [4, 8])
        self._food2_l2 = Actor('cherries.png', [8, 1])

        self._food1_l3 = Actor('apple.png', [4, 8])
        self._food2_l3 = Actor('cherries.png', [8, 1])

        self._key1_l1 = Actor('key.png', [13, 7]) 
        self._key2_l1 = Actor('key.png', [7, 4]) 

        self._key1_l2 = Actor('key.png', [13, 7]) 
        self._key2_l2 = Actor('key.png', [7, 4]) 

        self._key1_l3 = Actor('key.png', [13, 7]) 
        self._key2_l3 = Actor('key.png', [7, 4]) 

        # Lives
        self._life = START_LIFE

        # Key count
        self._keypoints = KEY_COUNT

    def on_draw(self):
        """Draw everything for the game"""
        arcade.start_render()

        if self._game_over:
            self._background.draw()
            arcade.draw_text('GAME OVER', 325, 325, arcade.color.WHITE, 20, 300, "center", "arial", True)
            return
        elif self._intro:
            self._background.draw()

            arcade.draw_text(GAME_NAME, 325, 400, arcade.color.BLACK, 20, 300, "center", "arial", True)
            arcade.draw_text('Collect all 6 keys to win. Eat fruit to add to your life. Watch out for the trolls.', 325, 365, arcade.color.WHITE, 20, 300, "center", "arial", True)
            arcade.draw_text('Press [Enter] to Begin', 325, 200, arcade.color.BLACK, 20, 300, "center", "arial", True)
            arcade.draw_text('Press [Q] to Quit at any time', 325, 150, arcade.color.BLACK, 20, 300, "center", "arial", True)
            return

        self._background.draw()
        self._player.draw()
        self._level.draw()

        if self._level_number == 1:
            self._badguy_l1.draw()
            self._badguy_l1_2.draw()
            self._badguy_l1_3.draw()
            self._badguy_l1_4.draw()
            self._badguy_l1_5.draw()
            self._badguy_l1_6.draw()
            self._badguy_l1_7.draw()
            self._badguy_l1_8.draw()
            self._badguy_l1_9.draw()

        if self._level_number == 2:
            self._badguy_l2.draw()
            self._badguy_l2_2.draw()
            self._badguy_l2_3.draw()
            self._badguy_l2_4.draw()
            self._badguy_l2_5.draw()
            self._badguy_l2_6.draw()
            self._badguy_l2_7.draw()
            self._badguy_l2_8.draw()
            self._badguy_l2_9.draw()

        if self._level_number == 3:
            self._badguy_l3.draw()
            self._badguy_l3_2.draw()
            self._badguy_l3_3.draw()
            self._badguy_l3_4.draw()
            self._badguy_l3_5.draw()
            self._badguy_l3_6.draw()
            self._badguy_l3_7.draw()
            self._badguy_l3_8.draw()
            self._badguy_l3_9.draw()

        if self._level_number == 1 and self._food1_l1:
            self._food1_l1.draw()

        if self._level_number == 1 and self._food2_l1:
            self._food2_l1.draw()

        if self._level_number == 2 and self._food1_l2:
            self._food1_l2.draw()

        if self._level_number == 2 and self._food2_l2:
            self._food2_l2.draw()

        if self._level_number == 3 and self._food1_l3:
            self._food1_l3.draw()

        if self._level_number == 3 and self._food2_l3:
            self._food2_l3.draw()

        if self._level_number == 1 and self._key1_l1:
            self._key1_l1.draw()
        if self._level_number == 1 and self._key2_l1:
            self._key2_l1.draw()

        if self._level_number == 2 and self._key1_l2:
            self._key1_l2.draw()
        if self._level_number == 2 and self._key2_l2:
            self._key2_l2.draw()

        if self._level_number == 3 and self._key1_l3:
            self._key1_l3.draw()
        if self._level_number == 3 and self._key2_l3:
            self._key2_l3.draw()

        # Put the Lives on the screen
        output = f"Lives:{self._life}"
        arcade.draw_text(output, 875, 620, arcade.color.WHITE, 16, 50, "right", "arial", True)

        # Put the Key Points on the screen
        output2 = f"Keys: {self._keypoints}"
        arcade.draw_text(output2, 10, 620, arcade.color.WHITE, 16, 30, font_name="arial", bold=True,)

    def on_key_press(self, key, modifiers):
        """ Create what needs to happen as the hero moves around the
        game (as keys are pressed by the player).

        Args:
            key: Key pressed by player.
            modifiers: Keys like Ctrl, Shift, etc and their controls.
        
        """

        if self._game_over:
            arcade.close_window()

        # Create keys to end game
        if key == arcade.key.Q:
            # Quit game
            self.game_over()
            return

        if self._intro:
            if key == arcade.key.ENTER:
                self._intro = False
                self.setup()
                arcade.play_sound(self._music, 1.0, 0, False)
            return

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

        # Switch between levels (the hero)
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

        # Add key points and take keys away
        if self._level_number == 1 and x == 13 and y == 7:
            arcade.play_sound(self._audio, 2, -1, False)
            self._key1_l1 = None
            self._keypoints = self._keypoints + 1
        elif self._level_number == 1 and x == 7 and y == 4:
            arcade.play_sound(self._audio, 2, -1, False)
            self._key2_l1 = None
            self._keypoints = self._keypoints + 1

        if self._level_number == 2 and x == 13 and y == 7:
            arcade.play_sound(self._audio, 2, -1, False)
            self._key1_l2 = None
            self._keypoints = self._keypoints + 1
        elif self._level_number == 2 and x == 7 and y == 4:
            arcade.play_sound(self._audio, 2, -1, False)
            self._key2_l2 = None
            self._keypoints = self._keypoints + 1

        if self._level_number == 3 and x == 13 and y == 7:
            arcade.play_sound(self._audio, 2, -1, False)
            self._key1_l3 = None
            self._keypoints = self._keypoints + 1
        elif self._level_number == 3 and x == 7 and y == 4:
            arcade.play_sound(self._audio, 2, -1, False)
            self._key2_l3 = None
            self._keypoints = self._keypoints + 1

        # Take away life points (bad guy)
        elif x == 11 and y == 8:
            self._life = self._life - 1
        elif x == 8 and y == 5:
            self._life = self._life - 1
        elif x == 2 and y == 7:
            self._life = self._life - 1
        elif x == 6 and y == 3:
            self._life = self._life - 1
        elif x == 4 and y == 2:
            self._life = self._life - 1
        elif x == 5 and y == 6:
            self._life = self._life - 1
        elif x == 10 and y == 3:
            self._life = self._life - 1
        elif x == 1 and y == 5:
            self._life = self._life - 1
        elif x == 13 and y == 5:
            self._life = self._life - 1


        # Add life points and take food away
        elif self._level_number == 1 and x == 4 and y == 8:
            arcade.play_sound(self._audio, 2, -1, False)
            self._food1_l1 = None
            self._life = self._life + 1
        elif self._level_number == 1 and x == 8 and y == 1:
            arcade.play_sound(self._audio, 2, -1, False)
            self._food2_l1 = None
            self._life = self._life + 1

        elif self._level_number == 2 and x == 4 and y == 8:
            arcade.play_sound(self._audio, 2, -1, False)
            self._food1_l2 = None
            self._life = self._life + 1
        elif self._level_number == 2 and x == 8 and y == 1:
            arcade.play_sound(self._audio, 2, -1, False)
            self._food2_l2 = None
            self._life = self._life + 1

        elif self._level_number == 3 and x == 4 and y == 8:
            arcade.play_sound(self._audio, 2, -1, False)
            self._food1_l3 = None
            self._life = self._life + 1
        elif self._level_number == 3 and x == 8 and y == 1:
            arcade.play_sound(self._audio, 2, -1, False)
            self._food2_l3 = None
            self._life = self._life + 1

        if self._life == 0:
            self.game_over()

        if self._keypoints == 6:
            self.game_over()

        # Check for player collision with any elements. 
        # If there is a collision, return to prevent the collision
        for actor in self._cast.get_actors('elements'):
            if x == actor.get_position().get_x() and y == actor.get_position().get_y():
                return

        position.set_x(x)

        position.set_y(y)

    def on_update(self, delta_time: float):
        """Updates the position and status of all actors.
        
        Arg:
            delta_time (float): Time since the last update"""

        if self._intro or self._game_over:
            return

        # Draw different backgrounds
        if self._level_number == 1:
            self._background = Background('grass.png')
            self._background.draw()
        if self._level_number == 2:
            self._background = Background('ground.png')
            self._background.draw()
        elif self._level_number == 3:
            self._background = Background('bluesky.png')
            self._background.draw()

    def game_over(self):
        self._game_over = True
        #arcade.close_window()
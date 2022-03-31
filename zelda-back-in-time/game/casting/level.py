import arcade
import csv

from game.constants import *
from game.casting.actor import Actor

class Level:
    """
    To add the actors that are needed in each level in the game. 
    """
    def __init__(self, file_name, cast):
        """
        Constructs a cast and map for the level.

        Args:
            file_name: Name of the file needed
            cast: What is needed to be done from the Cast class
        """
        self._file_name = file_name

        self._cast = cast

        self._map = []

        with open(LEVELS_DIRECTORY + self._file_name) as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                self._map.append(row)

    def draw(self):
        self._cast.remove_all_actors()

        for y in range(0, len(self._map)):
            for x in range(0, len(self._map[y])):
                actor = None

                if self._map[y][x] == 'b':
                    actor = Actor('bush.png', [x, y])
                if self._map[y][x] == 't':
                    actor = Actor('tree.png', [x, y])
                if self._map[y][x] == 'r':
                    actor = Actor('rock.png', [x, y])
                if self._map[y][x] == 'gc':
                    actor = Actor('whitecloud.png', [x, y])
                if self._map[y][x] == 'd':
                    actor = Actor('door.png', [x, y])

                if actor:
                    self._cast.add_actor('elements', actor)

                    arcade.draw_lrwh_rectangle_textured(actor._position.get_x() * IMAGE_WIDTH, actor._position.get_y() * IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_HEIGHT, actor._image.get_image())
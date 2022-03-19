from game.image import Image
from game.point import Point

class Element:
    def __init__(self, image_filename, point = None):
        self._image = Image(image_filename)

        if point != None:
            self._point = Point(point[0], point[1])
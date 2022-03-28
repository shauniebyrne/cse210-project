class Position:
    """Finds the position of the Actor.

    Arg:
        x (int): Value of x on the grid
        y (int): Value of y on the grid

    Attributes:
        _x: Value of x
        _y: Value of y
    
    """
    def __init__(self, x, y):
        self._x = x

        self._y = y

    def get_x(self):
        """Get the value of x and return it."""
        return self._x

    def get_y(self):
        """Get the value of y and return it."""
        return self._y

    def set_x(self, value):
        """Set the value of x."""
        self._x = value

    def set_y(self, value):
        """Set the value of y"""
        self._y = value
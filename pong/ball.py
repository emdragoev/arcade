import pygame

class Ball():
    MAX_SPEED = 5

    def __init__(self, size: int, screen_width: int, screen_height: int) -> None:
        """Creates a ball object"""
        self._size = size
        self._color = (255,255,255)
        self._x = screen_width / 2
        self._y = screen_height / 2
        self._x_speed = self.MAX_SPEED
        self._y_speed = 0

    def draw(self, surface) -> None:
        """Draws the ball"""
        pygame.draw.circle(surface, self._color, (self._x, self._y), self._size)
    
    def get_size(self) -> int:
        """Returns the size of a ball"""
        return self._size

    def get_coords(self) -> list:
        """Returns the coordinates of the ball"""
        return [int(self._x), int(self._y)]

    def set_x(self, x: int) -> None:
        """Sets the coordinates of the ball"""
        self._x = x

    def set_y(self, y: int) -> None:
        """Sets y coordinates of the ball"""
        self._y = y

    def get_y_speed(self) -> int:
        """Return y speed of the ball"""
        return self._y_speed

    def set_y_speed(self, speed: int) -> None:
        """Sets y speed of the ball"""
        self._y_speed = speed

    def get_x_speed(self) -> int:
        """Returns x speed of the ball"""
        return self._x_speed

    def set_x_speed(self, speed: int) -> None:
        """Sets x speed of the ball"""
        self._x_speed = speed

    def move(self) -> None:
        """Moves ball"""
        self._x += self._x_speed
        self._y += self._y_speed
    
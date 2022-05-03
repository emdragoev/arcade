from tkinter.messagebox import YES
import pygame
from pygame.locals import *

class Paddle:
    COLOR = (255,255,255)
    SPEED = 6

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """Creates paddle object"""
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def get_x(self) -> int:
        """Returns x position"""
        return self._x

    def set_x(self, x: int) -> None:
        """Sets x position"""
        self._x = x

    def get_y(self) -> int:
        """Returns y position"""
        return self._y

    def set_y(self, y: int) -> None:
        """Sets y position"""
        self._y = y

    def move(self, up: bool) -> None:
        """Moves the paddle up and down"""
        if up:
            self._y -= self.SPEED
        else:
            self._y += self.SPEED

    def draw(self, surface: pygame.Surface):
        """Draws the paddle"""
        pygame.draw.rect(surface, self.COLOR, (self._x, self._y, self._width, self._height))
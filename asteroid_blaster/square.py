import pygame, sys, time, random
from pygame.locals import *

class Square:
    def __init__(self, x: int, y:int, width: int, height: int, colour=(0,0,200)) -> None:
        """Initiates object attributes

            Args:
            x: x coordinate.
            y: y coordinate.
            width: Width of square.
            height: Height of square.
            colour: Colour of square, has a preset value.

            Returns:
                None
        """
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour

    def change_width(self, new_width: int) -> None:
        """Changes length of square

            Args:
            new_length: New length of square.

            Returns:
                None
        """
        self.width = new_width

    def draw(self, surface: pygame.display) -> None:
        """Draws object

            Args:
            surface: Where object is displayed.

            Returns:
                None
        """
        pygame.draw.rect(surface, (self.colour), (self.x, self.y, self.width, self.height))

    def get_rect(self) -> pygame.Rect:
        """Returns a rect object

            Args:
                None

            Returns:
                A pygame rect object
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)
# Import the pygame module
import pygame, sys, time, random
from pygame.locals import *

class Laser(pygame.sprite.Sprite):
    SPEED = 4

    def __init__(self, x: int, y: int, width: int, height: int):
        super(Laser, self).__init__()
        self.surface = pygame.Surface((width, height))
        self.surface.fill((255,255,255))
        self.rect = self.surface.get_rect(topleft=(x,y))

    def update(self) -> None:
        self.rect.move_ip(0, -self.SPEED)
        if self.rect.top < 0:
            self.kill()
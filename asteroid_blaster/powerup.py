# Import the pygame module
import pygame, sys, time, random
from asteroid import Asteroid
from pygame.locals import *
from player import Player

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, width: int):
        super(PowerUp, self).__init__()
        self.surface = pygame.image.load("star.png").convert()
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.width = width
        self.rect = self.surface.get_rect(center=(random.randint(20, self.width - 20), 0))
        self.speed = 7

    def update(self, stats: Player) -> None:
        self.rect.move_ip(0, self.speed)
        if self.rect.top > 550:
            self.kill()
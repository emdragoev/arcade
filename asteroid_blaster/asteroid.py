# Import the pygame module
import pygame, sys, time, random
from pygame.locals import *
from player import Player

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, width: int):
        super(Asteroid, self).__init__()
        self.surface = pygame.image.load("meteor.png").convert()
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.width = width
        self.rect = self.surface.get_rect(center=(random.randint(20, self.width - 20), 0))
        self.speed = random.randint(3,5)

    def update(self) -> None:
        self.rect.move_ip(0, self.speed)

    def freeze(self) -> None:
        self.rect.move_ip(0, 0)
    
    def check_pos(self) -> bool:
        if self.rect.top > 550:
            self.kill()
            return False
        return True

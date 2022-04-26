# Import the pygame module
import pygame, sys, time, random
from laser import Laser
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.image.load("spaceship.png").convert()
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surface.get_rect(topleft=(150,520))
        self.powerup = False
        self.score = 0
        self.lives = 10

    def update(self, pressed_keys: list) -> None:
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-6.5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(6.5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 400:
            self.rect.right = 400
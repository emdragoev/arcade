import pygame

class Text():
    def __init__(self, txt: str, x: int, y:int, size:int):
        self.txt = txt
        self.x = x
        self.y = y
        self.size = size

    def draw(self, surface: pygame.display) -> None:
        font = pygame.font.Font("OpenSans-Regular.ttf", self.size)
        img = font.render(self.txt, True, (255,255,255))
        surface.blit(img, (self.x, self.y))
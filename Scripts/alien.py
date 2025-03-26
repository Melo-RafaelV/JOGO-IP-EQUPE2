import pygame
class Alien:
    def __init__(self):
        self.img = pygame.image.load("images/ufo.png").convert_alpha()
        self.img = pygame.transform.scale(self.img,(50,50))

        self.x = 1350
        self.y = 350

        self.rect = self.img.get_rect()
import pygame
import random
class Alien:
    def __init__(self):
        self.img = pygame.image.load("images/ufo.png").convert_alpha()
        self.img = pygame.transform.scale(self.img,(60,60))

        self.x = 1350
        self.y = 350
        self.aceleracao = 1

        self.rect = self.img.get_rect()
    
    def respawn(self):
        self.x = 1350
        self.y = random.randint(1,644)
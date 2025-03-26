import pygame
class Disparos:
    def __init__(self):
        self.img = pygame.image.load("images/bullet.png").convert_alpha()
        self.img = pygame.transform.scale(self.img,(25,25))
        self.vel = 0
        self.x = 200
        self.y = 300
        self.rect = self.img.get_rect()
        self.status = False
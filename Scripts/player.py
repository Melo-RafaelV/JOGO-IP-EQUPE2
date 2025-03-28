import pygame
class Player:
    def __init__(self):
        self.img =  pygame.image.load("images/spaceship.png").convert_alpha()
        self.img = pygame.transform.scale(self.img,(50,50))
        self.img = pygame.transform.rotate(self.img, -90)
        self.x = 200
        self.y = 300
        self.rect = self.img.get_rect()
        self.pontos = 50
import pygame
import random

class Coletaveis:
    def __init__(self):
        self.x = 1350
        self.y = random.randint(1,650)
        self.cura = pygame.image.load("images/vida.png").convert_alpha()
        self.cura = pygame.transform.scale(self.cura,(50,50))
        self.rect = None
        self.cura_qnt = 0
        self.status = False

    
    def desenhar_coletaveis(self,screen):
        self.rect = self.cura.get_rect(topleft=(self.x, self.y))
        screen.blit(self.cura,(self.x,self.y))
    def restaurar(self):
        self.x = 1350
        self.y = random.randint(1,650)
        
        
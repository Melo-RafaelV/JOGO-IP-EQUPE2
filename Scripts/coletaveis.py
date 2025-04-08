import pygame
import random

class Coletaveis:
    def __init__(self):
        self.x = 1350
        self.y = random.randint(1,650)
        self.cura = pygame.image.load("images/vida.png").convert_alpha()
        self.cura = pygame.transform.scale(self.cura,(50,50))
        self.energetico = pygame.image.load("images/energetico.png").convert_alpha()
        self.energetico = pygame.transform.scale(self.energetico,(50,50))
        self.rect = None
        self.cura_qnt = 0
        self.energetico_qnt = 0
        self.status = False
        self.tipo = None
        self.num = 0
        self.tempo = 0

    
    def desenhar_coletaveis(self,screen,player):
        if not self.tipo:
            if player.vidas < 3:
                self.num = random.randint(1,2)
            else:
                self.num = 2
        if self.num == 1:
            self.rect = self.cura.get_rect(topleft=(self.x, self.y))
            self.tipo = "cura"
            screen.blit(self.cura,(self.x,self.y))
        elif self.num == 2 :
            self.rect = self.energetico.get_rect(topleft=(self.x, self.y))
            self.tipo = "energetico"
            screen.blit(self.energetico,(self.x,self.y))
    def restaurar(self):
        self.x = 1350
        self.y = random.randint(1,650)
        
        
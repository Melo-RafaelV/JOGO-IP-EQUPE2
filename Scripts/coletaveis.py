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
        self.slow = pygame.image.load("images/slowdown.png").convert_alpha()
        self.slow = pygame.transform.scale(self.slow,(50,50))
        self.rect = None
        self.cura_qnt = 0
        self.energetico_qnt = 0
        self.slow_qnt = 0
        self.status = False
        self.tipo = None
        self.num = 0
        self.tempo = 0

    
    def desenhar_coletaveis(self,screen,player):
        if not self.tipo:
            if player.pontos == 5:
                self.num = 1
            elif player.pontos == 10:
                self.num = 2
            elif player.pontos == 15:
                self.num =3
            elif player.vidas < 5:
                self.num = random.randint(1,3)
            else:
                self.num = random.randint(2,3)
        if self.num == 1:
            self.rect = self.cura.get_rect(topleft=(self.x, self.y))
            self.tipo = "cura"
            screen.blit(self.cura,(self.x,self.y))
        elif self.num == 2 :
            self.rect = self.energetico.get_rect(topleft=(self.x, self.y))
            self.tipo = "energetico"
            screen.blit(self.energetico,(self.x,self.y))
        elif self.num ==3:
            self.rect = self.slow.get_rect(topleft=(self.x, self.y))
            self.tipo = "slow"
            screen.blit(self.slow,(self.x,self.y))

    def desenhar_qnt_coletaveis(self,screen):
        fonte = pygame.font.SysFont("fonte/Minecraft.ttf", 25)

        cont_e = fonte.render(f": {int(self.energetico_qnt)} ",True,(255,255,255))
        screen.blit(self.energetico,(20,85))
        screen.blit(cont_e,(70,100))
        cont_s = cont_e = fonte.render(f": {int(self.slow_qnt)} ",True,(255,255,255))
        screen.blit(self.slow,(20,135))
        screen.blit(cont_s,(70,155))



    def restaurar(self):
        self.x = 1350
        self.y = random.randint(1,650)
        
        
import pygame
class Player:
    def __init__(self):
        self.img =  pygame.image.load("images/spaceship.png").convert_alpha()
        self.img = pygame.transform.scale(self.img,(50,50))
        self.img = pygame.transform.rotate(self.img, -90)
        self.x = 200
        self.y = 300
        self.rect = self.img.get_rect()
        self.pontos = 0
        self.vidas = 4
        self.coracao =  pygame.image.load("images/vida.png").convert_alpha()
        self.coracao =  pygame.transform.scale(self.coracao,(30,30))
        self.aceleracao = 1

        
    def desenhar_vida(self,screen):
        for i in range(self.vidas):
            screen.blit(self.coracao, (20 + i * 30, 10)) #ajustando as posições dos corações 
        
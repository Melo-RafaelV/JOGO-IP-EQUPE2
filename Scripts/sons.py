import pygame 

class Sons:
    def __init__(self):
        self.som_disparo = pygame.mixer.Sound("sons/disparo.wav")
        self.som_disparo.set_volume(0.02)
        self.som_energetico = pygame.mixer.Sound("sons/energetico.wav")
        self.som_vida = pygame.mixer.Sound("sons/vida.wav")
        self.som_vida.set_volume(0.1)
        self.som_game_over = pygame.mixer.Sound("sons/gameover.mp3")
        self.som_game_over.set_volume(3)
        self.som_hit = pygame.mixer.Sound("sons/hit.mp3")
        self.som_hit.set_volume(0.2)
    def disparo(self):
        self.som_disparo.play()
    def energetico(self):
        self.som_energetico.play()
    def vida(self):
        self.som_vida.play()
    def game_over(self):
        self.som_game_over.play()
    def hit(self):
        self.som_hit.play()
    #falta a funçao de quando atingir um alien ou quando perder uma vida, e o som do slow
import pygame 

class Sons:
    def __init__(self):
        self.som_disparo = pygame.mixer.Sound("sons/disparo.wav")
        self.som_disparo.set_volume(0.2)
        self.som_energetico = pygame.mixer.Sound("sons/energetico.wav")
        self.som_vida = pygame.mixer.Sound("sons/vida.wav")
        self.som_vida.set_volume(0.8)
        self.som_game_over = pygame.mixer.Sound("sons/gameover.wav")
        self.som_game_over.set_volume(0.5)
    def disparo(self):
        self.som_disparo.play()
    def energetico(self):
        self.som_energetico.play()
    def vida(self):
        self.som_vida.play()
    def game_over(self):
        self.som_game_over.play()
    #falta a funçao de quando atingir um alien ou quando perder uma vida, e o som do slow
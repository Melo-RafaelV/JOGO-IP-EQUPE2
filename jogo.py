import pygame

from Scripts.player import Player
from Scripts.alien import Alien
from Scripts.disparos import Disparos
from Scripts.coletaveis import Coletaveis


def colisoes(player,alien,disparo,coletaveis):
    if player.rect.colliderect(alien.rect) or alien.rect.x == 60:
        player.vidas -= 1
        return True
    elif disparo.rect.colliderect(alien.rect):
        player.pontos += 1
        return True
    elif coletaveis.status:
        if disparo.rect.colliderect(coletaveis.rect):
            player.vidas = min(player.vidas + 1, 5)
            coletaveis.status = False
            disparo.atirar(player)
            coletaveis.rect = None
            coletaveis.x = 1350
            return False
    else:
        return False


def tela_menu(screen):
    # Tela inicial do menu
    bg_menu = pygame.image.load("images/menu_bg.png").convert()
    bg_menu = pygame.transform.scale(bg_menu, (1280, 720))

    while True:
        screen.blit(bg_menu, (0, 0))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                jogo(screen)

def game_over(screen, pontuacao):
    # tela de Game Over - pontuação e reiniciar
    bg_menu = pygame.image.load("images/gameover_bg.png").convert()
    bg_menu = pygame.transform.scale(bg_menu, (1280, 720))

    while True:
        screen.blit(bg_menu, (0, 0))

        fonte = pygame.font.SysFont("fonte/Minecraft.ttf", 35)
        pontuacao_final = fonte.render(f"Pontuação final: {pontuacao} pontos", True, (255, 255, 255))
        tempo_final = fonte.render(f"Tempo final: 0 segundos", True, (255, 255, 255))
        screen.blit(pontuacao_final, (430, 450))
        screen.blit(tempo_final, (430, 490))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogo(screen)

def jogo(screen):
    x = 1280
    y = 720

    fonte = pygame.font.SysFont("fonte/Minecraft.ttf", 25)
    pygame.display.set_caption("JOGO DA NAVE")

    #Criação do Fundo do jogo
    bg = pygame.image.load("images/fundo.jpg").convert_alpha()
    bg = pygame.transform.scale(bg,(x,y))

    player = Player()
    alien = Alien()
    disparo = Disparos()
    coletaveis = Coletaveis()

    rodando = True

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
        
        screen.blit(bg,(0,0))

        rel_x = x % bg.get_rect().width
        screen.blit(bg,(rel_x - bg.get_rect().width,0))
        if rel_x <1280:
            screen.blit(bg,(rel_x,0))


        #comandos
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w] and player.y > 1:
            player.y -=1
            if not disparo.status:
                disparo.y -=1

        if tecla[pygame.K_s] and player.y < 665:
            player.y += 1
            if not disparo.status:
                disparo.y +=1

        if tecla[pygame.K_SPACE]:
            disparo.status = True
            disparo.vel = 4

        #respawn
        if alien.x == 50:
            alien.respawn()
        
        if coletaveis.x <=60:
                coletaveis.status = False
                coletaveis.rect = None
                coletaveis.restaurar()
        
        if disparo.x == 1300 :
            disparo.atirar(player)

        if colisoes(player,alien,disparo,coletaveis):
            alien.respawn()
            disparo.atirar(player)
        
        if player.pontos%10 == 0 and player.pontos > 0 and not coletaveis.status:
            coletaveis.status = True
        
        if coletaveis.status:
            coletaveis.desenhar_coletaveis(screen)
            

        if player.vidas == 0:
            rodando = False

        #movimentos
        x -=0.5
        alien.x -= 2 #movimentando o alienww
        disparo.x += disparo.vel
        if coletaveis.status:
            coletaveis.x -=0.5

        player.desenhar_vida(screen)

        #posições rect
        player.rect.y,player.rect.x = player.y,player.x
        disparo.rect.x,disparo.rect.y = disparo.x,disparo.y
        alien.rect.x,alien.rect.y = alien.x,alien.y

        points = player.pontos
        pontuacao = fonte.render(f"Pontos: {int(points)} ",True,(255,255,255))
        screen.blit(pontuacao,(50,50))


        #Criando imagens
        screen.blit(alien.img,(alien.x,alien.y))
        screen.blit(disparo.img,(disparo.x,disparo.y))
        screen.blit(player.img, (player.x,player.y))

        pygame.display.update()

        if not rodando: # fim de jogo
            game_over(screen, points)
    
if __name__ == "__main__":
    pygame.init()  # Inicializa o pygame
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("JOGO DA NAVE")
    tela_menu(screen)  # Exibe o menu inicial
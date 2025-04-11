import pygame

from Scripts.player import Player
from Scripts.alien import Alien
from Scripts.disparos import Disparos
from Scripts.coletaveis import Coletaveis
from Scripts.sons import Sons
import time


def colisoes(player,alien,disparo,coletaveis,sons):
    if player.rect.colliderect(alien.rect) or alien.rect.x <= 60:
        if player.pontos >= 1:
            sons.hit()
        player.vidas -= 1
        alien.respawn()
        return False
    elif disparo.rect.colliderect(alien.rect):
        #somde colisao
        player.pontos += 1
        return True
    elif coletaveis.status:
        if disparo.rect.colliderect(coletaveis.rect):
            if coletaveis.tipo == "cura":
                sons.vida()
                player.vidas = min(player.vidas + 1, 5)
                coletaveis.cura_qnt +=1

            elif coletaveis.tipo == "energetico":
                sons.energetico()
                player.aceleracao = 2
                coletaveis.tempo = time.perf_counter()
                coletaveis.energetico_qnt += 1
           
            elif coletaveis.tipo == "slow":
                sons.moeda()
                alien.aceleracao = 0.5
                coletaveis.tempo = time.perf_counter()
                coletaveis.slow_qnt += 1
            

            coletaveis.status = False
            coletaveis.rect = None
            coletaveis.x = 1350
            coletaveis.tipo = None
            disparo.atirar(player)
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

def game_over(screen, pontuacao,tempo,sons,maior_pontuacao):
    # tela de Game Over - pontuação e reiniciar
    bg_menu = pygame.image.load("images/gameover_bg.png").convert()
    bg_menu = pygame.transform.scale(bg_menu, (1280, 720))
    sons.game_over()
    while True:
        screen.blit(bg_menu, (0, 0))

        fonte = pygame.font.SysFont("fonte/Minecraft.ttf", 35)
        pontuacao_final = fonte.render(f"Pontuação Final: {pontuacao} pontos", True, (255, 255, 255))
        tempo_final = fonte.render(f"Tempo Final: {tempo} segundos", True, (255, 255, 255))
        score = fonte.render(f"Top Score: {maior_pontuacao} pontos",True, (255, 255, 255))
        screen.blit(pontuacao_final, (500, 350))
        screen.blit(tempo_final, (500, 400))
        screen.blit(score, (500,450))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # botão para reiniciar o jogo
                    jogo(screen)

def jogo(screen):
    x = 1280
    y = 720

    fonte = pygame.font.SysFont("fonte/Minecraft.ttf", 25)
    pygame.display.set_caption("JOGO DA NAVE")

    #Criação do Fundo do jogo
    bg = pygame.image.load("images/fundo.png").convert_alpha()
    bg = pygame.transform.scale(bg,(x,y))
    pause_bg = pygame.image.load("images/Jogo Pausado.png").convert_alpha()
    pause_bg = pygame.transform.scale(pause_bg,(x,y))

    player = Player()
    alien = Alien()
    disparo = Disparos()
    coletaveis = Coletaveis()
    sons = Sons()
    rodando = True
    tempo = time.perf_counter()
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.blit(bg,(0,0))

        rel_x = x % bg.get_rect().width
        screen.blit(bg,(rel_x - bg.get_rect().width,0))
        if rel_x <1280:
            screen.blit(bg,(rel_x,0))

        if time.perf_counter() - coletaveis.tempo >= 10:
            player.aceleracao = 1
            coletaveis.tempo = 0
            alien.aceleracao = 1

        #comandos
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w] and player.y > 1:
            if player.pontos > 40:
                player.y -= 1 *player.aceleracao
            elif player.pontos > 20:
                player.y -= 0.7 *player.aceleracao
            else:
                player.y -= 0.5 * player.aceleracao
            
            if not disparo.status:
                if player.pontos > 40:
                    disparo.y -= 1 *player.aceleracao
                elif player.pontos > 20: 
                    disparo.y -= 0.7 *player.aceleracao
                else:
                    disparo.y -= 0.5 *player.aceleracao
                

        if tecla[pygame.K_s] and player.y < 665:
            if player.pontos > 40:
                player.y -= 1 *player.aceleracao
            elif player.pontos > 20:
                player.y += 0.7 *player.aceleracao
            else:
                player.y += 0.5 *player.aceleracao
            
            if not disparo.status:
                if player.pontos > 40:
                    disparo.y -= 1 *player.aceleracao
                elif player.pontos > 20: 
                    disparo.y += 0.7 *player.aceleracao
                else:
                    disparo.y +=0.5 *player.aceleracao

        if tecla[pygame.K_SPACE]:
            sons.disparo()
            disparo.status = True
            disparo.vel = 2

        #respawn
        if alien.x == 50:
            alien.respawn()
        
        if coletaveis.x <=60:
                coletaveis.status = False
                coletaveis.rect = None
                coletaveis.restaurar()
        
        if disparo.x == 1300 :
            disparo.atirar(player)

        if colisoes(player,alien,disparo,coletaveis,sons):
            alien.respawn()
            disparo.atirar(player)
        
        if player.pontos%5 == 0 and player.pontos > 0 and not coletaveis.status:
            coletaveis.status = True
        
        if coletaveis.status:
            coletaveis.desenhar_coletaveis(screen, player)
            

        if player.vidas == 0:
            rodando = False
        
        if tecla[pygame.K_p]:
            pause = True
            screen.blit(pause_bg,(0,0))
            pygame.display.update()
            while pause:

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pause = False
                    if event.type == pygame.QUIT:
                        pause = False
                        rodando = False
        

        #movimentos
        x -=0.5
        #movimento do alien
        if player.pontos < 20:
            alien.x -= 1 * alien.aceleracao 
        elif player.pontos <40:
            alien.x -= 1.5 * alien.aceleracao 
        else:
            alien.x -= 2 * alien.aceleracao
        
        disparo.x += disparo.vel
        if coletaveis.status:
            coletaveis.x -=0.5

        player.desenhar_vida(screen)
        coletaveis.desenhar_qnt_coletaveis(screen)

        #posições rect
        player.rect.y,player.rect.x = player.y,player.x
        disparo.rect.x,disparo.rect.y = disparo.x,disparo.y
        alien.rect.x,alien.rect.y = alien.x,alien.y

       
        pontuacao = fonte.render(f"Pontos: {int(player.pontos)} ",True,(255,255,255))
        screen.blit(pontuacao,(30,50))


        #Criando imagens
        screen.blit(alien.img,(alien.x,alien.y))
        screen.blit(disparo.img,(disparo.x,disparo.y))
        screen.blit(player.img, (player.x,player.y))

        pygame.display.update()


        if not rodando: # fim de jogo
            with open("Scripts/score.txt","r") as arquivo:
                score = arquivo.read()
            if int(score) < player.pontos:
                maior_pontuacao = player.pontos
                with open("Scripts/score.txt","w") as arquivo:
                    arquivo.write(str(maior_pontuacao))
            else:
                maior_pontuacao = score

            game_over(screen, player.pontos, int(time.perf_counter()- tempo),sons,maior_pontuacao)
 
if __name__ == "__main__":
    pygame.init()  # Inicializa o pygame
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("SPACE INVADERS")
    tela_menu(screen)  # Exibe o menu inicial

from Scripts.player import Player
from Scripts.alien import Alien
from Scripts.disparos import Disparos



import pygame
import random






def colisoes(player,alien,disparo):
    player.pontos
    if player.rect.colliderect(alien.rect) or alien.rect.x == 60:
        player.pontos -= 1
        return True
    elif disparo.rect.colliderect(alien.rect):
        player.pontos += 1
        return True
    else:
        return False
        





pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("JOGO DA NAVE")

#Criação do Fundo
bg = pygame.image.load("images/fundo.jpg").convert_alpha()
bg = pygame.transform.scale(bg,(x,y))



player = Player()
alien = Alien()
disparo = Disparos()

rodando = True

fonte = pygame.font.SysFont("fonte/Minecraft.ttf", 25)

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
    
    if disparo.x == 1300 :
        disparo.atirar(player)

    if colisoes(player,alien,disparo):
        alien.respawn()
        disparo.atirar(player)
    
    if player.pontos == -1:
        rodando = False

    #movimentos
    x -=0.5
    alien.x -= 2 #movimentando o alien
    disparo.x += disparo.vel


    #posições rect
    player.rect.y,player.rect.x = player.y,player.x

    disparo.rect.x,disparo.rect.y = disparo.x,disparo.y

    alien.rect.x,alien.rect.y = alien.x,alien.y


    pontuacao = fonte.render(f"Pontos: {int(player.pontos)} ",True,(255,255,255))
    screen.blit(pontuacao,(50,50))



    #Criando imagens
    screen.blit(alien.img,(alien.x,alien.y))
    screen.blit(disparo.img,(disparo.x,disparo.y))
    screen.blit(player.img, (player.x,player.y))

    

    pygame.display.update()
import pygame
import random


def respawn():
    x = 1350
    y = random.randint(1,644)
    return (x,y)



def disparos():
    disparado = False
    respawn_x = pos_player_x
    respawn_y = pos_player_y
    vel_disparo= 0
    return [respawn_x,respawn_y,disparado,vel_disparo]


def colisoes():
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -= 1
        return True
    elif disparo_rect.colliderect(alien_rect):
        pontos += 1
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

#Criação da nave alien

alien = pygame.image.load("images/ufo.png").convert_alpha()
alien = pygame.transform.scale(alien,(50,50))

#Criação da nave player
playerImg = pygame.image.load("images/spaceship.png").convert_alpha()
playerImg = pygame.transform.scale(playerImg,(50,50))
playerImg = pygame.transform.rotate(playerImg, -90)

#disparo da nave
disparo = pygame.image.load("images/bullet.png").convert_alpha()
disparo = pygame.transform.scale(disparo,(25,25))

pontos = 1

pos_alien_x = 1350
pos_alien_y = 350

pos_player_x = 200
pos_player_y = 300


vel_disparo = 0
pos_x_disparo =200
pos_y_disparo = 300

rodando = True
disparado = False

fonte = pygame.font.SysFont("fonte/Minecraft.ttf", 25)

player_rect = playerImg.get_rect()
alien_rect = alien.get_rect()
disparo_rect = disparo.get_rect()

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
    if tecla[pygame.K_w] and pos_player_y > 1:
        pos_player_y -=1
        if not disparado:
            pos_y_disparo -=1

    if tecla[pygame.K_s] and pos_player_y < 665:
        pos_player_y += 1
        if not disparado:
            pos_y_disparo +=1

    if tecla[pygame.K_SPACE]:
        disparado = True
        vel_disparo = 2

    #respawn
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    
    if pos_x_disparo == 1300 :
        pos_x_disparo,pos_y_disparo,disparado,vel_disparo = disparos()

    if colisoes():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
        pos_x_disparo,pos_y_disparo,disparado,vel_disparo = disparos()
    
    if pontos == -1:
        rodando = False

    #movimentos
    x -=0.5
    pos_alien_x -= 2 #movimentando o alien
    pos_x_disparo += vel_disparo


    #posições rect
    player_rect.y,player_rect.x = pos_player_y,pos_player_x

    disparo_rect.x,disparo_rect.y = pos_x_disparo,pos_y_disparo

    alien_rect.x,alien_rect.y = pos_alien_x,pos_alien_y


    pontuacao = fonte.render(f"Pontos: {int(pontos)} ",True,(255,255,255))
    screen.blit(pontuacao,(50,50))



    #Criando imagens
    screen.blit(alien,(pos_alien_x,pos_alien_y))
    screen.blit(disparo,(pos_x_disparo,pos_y_disparo))
    screen.blit(playerImg, (pos_player_x,pos_player_y))

    

    pygame.display.update()
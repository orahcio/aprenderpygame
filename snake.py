
import pygame
from pygame.locals import *
from sys import exit
from random import randint


VERMELHO = (255,0,0)
VERDE = (0,255,0)
AMARELO = (255,255,0)
AZUL = (0,0,255)
FUNDO = (255,255,255)

largura = 800
altura = 640

def jogo_na_matrix():

    pygame.init()
    
    tela = pygame.display.set_mode((largura,altura))
    relogio = pygame.time.Clock()

    # inicialmente a tela está em branco
    buffer = []
    for i in range(32):
        buffer.append([])
        for j in range(40):
            buffer[i].append(0)


    # Controle do snake
    controle = {
        K_w: (0,-1),
        K_s: (0,1),
        K_a: (-1,0),
        K_d: (1,0)
        }

    # snake começa no canto superior da tela
    buffer[0][0] = 1
    snake = [(0,0)]
    v = (1,0)

    rodando = True
    alterna = 0

    while rodando:
        relogio.tick(15)
        tela.fill(FUNDO)
        # apaga matriz
        for i in range(32):
            for j in range(40):
                buffer[i][j] = 0

        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodando = False
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    rodando = False
                if evento.key == K_w and v[1]<=0:
                    v = [0,-1]
                if evento.key == K_s and v[1]>=0:
                    v = [0,1]
                if evento.key == K_d and v[0]>=0:
                    v = [1,0]
                if evento.key == K_a and v[0]<=0:
                    v = [-1,0]
                # if event.key in controle:
                #     i,j = v
                #     il,jl = controle[event.key]
                #     e = i*il+j*jl
                #     e *= e
                #     v = (i-il)*e+il, (j-jl)*e+jl
                #     print(v)


        # preenche o próximo passo
        x = (v[0]+snake[-1][0])%40
        y = (v[1]+snake[-1][1])%32
        snake.append((x,y))
        # alterna = 0

        # desenhar a matriz conforme o snake
        for i,j in snake:
            buffer[j][i] = 1
        
        # desenhar retângulos conforme a matriz buffer
        for i in range(32):
            for j in range(40):
                if buffer[i][j] == 1:
                    pygame.draw.rect(tela,VERDE,(j*20,i*20,20,20))
        
        # limita o tamanho do snake
        if len(snake) > 4:
            snake.pop(0)

        pygame.display.flip()

    
    pygame.quit()
            

def main():
    pygame.init()

    altura = 640
    largura = 800

    tela = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption('Joguinho da cobrinha')
    relogio = pygame.time.Clock()


    cabeca = Rect(largura/2,altura/2,20,20)
    maca = Rect(randint(20,largura-20),randint(20,altura-20),20,20)
    cobra = []
    compr = 1
    s = 5
    controle = {
        K_w: (0,-s),
        K_s: (0,s),
        K_a: (-s,0),
        K_d: (s,0)
        }

    x,y = (0,0)
    v = (s,0)

    rodando = True

    while rodando:
        relogio.tick(30)
        tela.fill(FUNDO)
        corpo = cabeca.copy()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodando = False
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    rodando = False
                if evento.key in controle:
                    x,y = v
                    xn,yn = controle[evento.key]
                    escalar = (x*xn+y*yn)/(s*s)
                    escalar *= escalar
                    v = (x-xn)*escalar+xn, (y-yn)*escalar+yn
                    print(v)
        cabeca.move_ip(v)
        if (cabeca.x,cabeca.y) in cobra:
            rodando = False
        cobra.append((cabeca.x,cabeca.y))
        for c in cobra:
            pygame.draw.rect(tela,VERDE,(c[0],c[1],20,20))
            
        rect_obj = pygame.draw.rect(tela,VERMELHO,maca)
        cabeca.x %= largura
        cabeca.y %= altura
        if cabeca.colliderect(maca):
            maca.x = randint(20,largura-20)
            maca.y = randint(20,altura-20)
            compr += 3

        if len(cobra) > compr:
            cobra.pop(0)
        pygame.display.flip()

    pygame.quit()


if __name__=="__main__":
    jogo_na_matrix()
    exit()

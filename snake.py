import pygame
from pygame.locals import *
from sys import exit
from random import randint


VERMELHO = (255,0,0)
VERDE = (0,255,0)
AMARELO = (255,255,0)
AZUL = (0,0,255)
FUNDO = (255,255,255)
PRETO = (0,0,0)

largura = 800
altura = 640

a = 51

l = int(largura/a)
h = int(altura/a)

def jogo_na_matrix():

    pygame.init()
    
    tela = pygame.display.set_mode((largura,altura))
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont('Times',35,False,False)

    # Controle do snake
    controle = {
        K_w: (0,-1),
        K_s: (0,1),
        K_a: (-1,0),
        K_d: (1,0)
        }

    # snake começa no canto superior da tela
    snake = [(0,0)]
    maçã = (int(l/2),int(h/2))
    v = (1,0)
    comprimento = 6

    pontos = 0

    rodando = True

    while rodando:
        relogio.tick(7)
        tela.fill(FUNDO)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodando = False
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    rodando = False
                if evento.key in controle:
                    # A sequencia de ifs pode ser substituída por essa sequência
                    i,j = snake[-1][0]-snake[-2][0],snake[-1][1]-snake[-2][1]
                    il,jl = controle[evento.key]
                    e = i*il+j*jl
                    e *= e
                    v = (i-il)*e+il, (j-jl)*e+jl

        # preenche o próximo passo
        i = (v[0]+snake[-1][0])%l
        j = (v[1]+snake[-1][1])%h

        # Se ela acertar a própria cauda morre
        if (i,j) in snake:
            rodando = False
        
        snake.append((i,j))

        # Colidindo
        if maçã == (i,j):
            comprimento += 1
            pontos += 1
            maçã = randint(0,l-1),randint(0,h-1)
            while maçã in snake:
                maçã = randint(0,l-1),randint(0,h-1)

        # desenhar maçã e snake
        x,y = maçã
        pygame.draw.rect(tela,VERMELHO,(x*a,y*a,a,a))
        for i,j in snake:
            pygame.draw.rect(tela,VERDE,(i*a,j*a,a,a))
        
        # limita o tamanho do snake
        if len(snake) > comprimento:
            snake.pop(0)

        # Atualiza o placar
        mensage = f'Pontos: {pontos}'
        placar = fonte.render(mensage,True,PRETO)
        tela.blit(placar,(500,0))

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

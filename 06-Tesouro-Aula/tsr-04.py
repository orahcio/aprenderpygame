# Escreva o seu código aqui :-)
import pgzrun
import random
from pgzhelper import*

#Fundo de Tela
WIDTH = 800
HEIGHT = 600
bg = Actor('background')

# Navio
ship = Actor('ship')
ship.x = 400
ship.y = 550
ship.scale = 0.8

# Moeda
coin = Actor('coin')
coin.x = random.randint(20, 780)
coin.y = 0
coin.scale = 0.5

# Bomba
bomb = Actor('bomb')
bomb.x = random.randint(20,780)
bomb.y = 0
bomb.scale = 0.5

# Pontuação
score = 0

def draw():
    bg.draw()
    ship.draw()
    coin.draw()
    bomb.draw()

    texto = ' score: ' + str(score)
    posicao = (15,10)
    screen.draw.text(texto, posicao, \
        color=(255,255, 255), fontname='pixel', fontsize=15)




def update():

    # Navio
    if keyboard.left:
        ship.x = ship.x -7
        if ship.left < 0:
            ship.left = 0
    if keyboard.right:
        ship.x = ship.x +7
        if ship.right > WIDTH:
            ship.right = WIDTH

    # Moeda
    coin.y += 7
    if coin.y > HEIGHT:
        coin.x = random.randint(20, 780)
        coin.y = 0

    # Colisão com Moeda
    global score
    if coin.colliderect(ship):
        score = score + 1
        coin.x = random.randint (20, 780)
        coin.y = 0


    # Colisão com Moeda
    if coin.colliderect(ship):
        coin.x = random.randint (20, 780)
        coin.y = 0





    # Bomba
    bomb.y +=8
    if bomb.y > HEIGHT:
        bomb.x = random.randint(20,780)
        bomb.y=0

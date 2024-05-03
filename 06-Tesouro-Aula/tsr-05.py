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

# Vidas
lives = 3

# Fim de Jogo
game_over = False

def draw():
    bg.draw()
    if not game_over:
        ship.draw()
        coin.draw()
        bomb.draw()

    texto = ' score: ' + str(score)
    posicao = (15,10)
    screen.draw.text(texto, posicao, \
        color=(255,255, 255), fontname='pixel', fontsize=15)

    texto = ' lives: ' + str(lives)
    posicao = (650,10)
    screen.draw.text(texto, posicao, \
        color=(255,255, 255), fontname='pixel', fontsize=15)

def update():
    global game_over
    if not game_over:
        update2()

def update2():
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

    # Pontuação Moeda
    global score
    if coin.colliderect(ship):
        score = score + 1
        coin.x = random.randint (20, 780)
        coin.y = 0
        sounds.coleta.play()

    # Bomba
    bomb.y +=8
    if bomb.y > HEIGHT:
        bomb.x = random.randint(20,780)
        bomb.y=0

    # Vidas
    global lives, game_over
    if bomb.colliderect(ship):
        lives = lives -1
        if lives == 0:
            game_over = True
        bomb.x = random.randint(20,780)
        bomb.y = 0
        sounds.explosao.play()


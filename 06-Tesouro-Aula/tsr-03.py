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

def draw():
    bg.draw()
    ship.draw()
    coin.draw()

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


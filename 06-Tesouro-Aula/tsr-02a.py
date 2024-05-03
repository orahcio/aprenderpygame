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

def draw():
    bg.draw()
    ship.draw()

def update():
    if keyboard.left:
        ship.x = ship.x -7
        if ship.left < 0:
            ship.left = 0
    if keyboard.right:
        ship.x = ship.x +7
        if ship.right > WIDTH:
            ship.right = WIDTH


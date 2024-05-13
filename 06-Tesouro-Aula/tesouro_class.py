from random import randint
# from pgzhelper import *

class Hero(Actor):

    vel = 7
    life = 3
    score = 0

    def update(self):
        if keyboard.left or keyboard.a:
            ship.x -= self.vel
            if ship.left < 0: # Parede à esquerda
                ship.left = 0
        if keyboard.right or keyboard.d:
            ship.x += self.vel
            if ship.right > WIDTH: # Parede à direita`
                ship.right = WIDTH
    

    def collide(self, item, c=1):
        if self.colliderect(item):
            if c>0: self.score += c
            else: self.life += c
            item.set_pos()
            item.som()



class Item(Actor):
    global HEIGHT

    vel = 7

    def set_pos(self):
        self.midtop = randint(20,780), 0

    
    def update(self):
        self.y += self.vel
        if self.bottom > HEIGHT:
            self.set_pos()
    

    def set_sound(self, som):
        self.som = som.play


WIDTH = 800
HEIGHT = 600

ship = Hero('ship', midbottom=(WIDTH/2,HEIGHT))

coin = Item('coin')
coin.set_pos()
coin.set_sound(sounds.coleta)

bomb = Item('bomb')
bomb.set_pos()
bomb.set_sound(sounds.explosao)

game_over = False

def draw():
    global game_over

    if not game_over:
        screen.blit('background',(0,0))
        ship.draw()
        coin.draw()
        bomb.draw()
        screen.draw.text(f'Pontos: {ship.score}',topleft=(0,0), fontname='pixel', color=(255,255,255), fontsize=15)
        screen.draw.text(f'Vidas: {ship.life}', topright=(800,0), fontname='pixel' ,color=(255,255,255), fontsize=15)
    
    else:
        screen.blit('background',(0,0))
        screen.draw.text(f'Game Over', (400,300), fontname='pixel', color=(255,255,255), fontsize=30)
        screen.draw.text(f'Pontos: {ship.score}', (370,350), fontname='pixel', color=(255,255,255), fontsize=15)
        screen.draw.text(f'Vidas: {ship.life}', (370,370), fontname='pixel', color=(255,255,255), fontsize=15)


def update():
    global game_over

    if not game_over:
        ship.update()

        coin.update()
        bomb.update()

        ship.collide(coin)
        
        ship.collide(bomb, -1)

        if ship.life == 0:
            game_over = True
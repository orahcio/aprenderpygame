from random import randint
# from pgzhelper import *


class Hero(Actor):
    def __init__(self, image, pos=None, anchor=None, vel=7, life=3, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        self.vel = vel
        self.life = life
        self.score = 0
        
        
    def update(self):
        if keyboard.left or keyboard.a:
            ship.x -= self.vel
            if ship.left < 0: # Parede à esquerda
                ship.left = 0
        if keyboard.right or keyboard.d:
            ship.x += self.vel
            if ship.right > WIDTH: # Parede à direita`
                ship.right = WIDTH
    

    def collide(self, item, items, c=1):
        if self.colliderect(item):
            if c>0: self.score += c
            else: self.life += c
            item.set_pos()
            item.som()
            items.remove(item)


class Item(Actor):
    global HEIGHT


    def __init__(self, image, pos=None, anchor=None, vel=7, som=None, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        self.vel = vel
        self.midtop = randint(20,780), 0
        self.som = som.play


    def set_pos(self):
        self.midtop = randint(20,780), 0

    
    def update(self):
        self.y += self.vel
        if self.bottom > HEIGHT:
            self.midtop = randint(20,780), 0


WIDTH = 800
HEIGHT = 600

ship = Hero('ship', midbottom=(WIDTH/2,HEIGHT))

coins = [Item('coin', som=sounds.coleta)]
bombs = [Item('bomb', som=sounds.explosao)]

game_over = False
timeout = 0

def draw():
    global game_over

    if not game_over:
        screen.blit('background',(0,0))
        ship.draw()

        for coin in coins:
            coin.draw()
        for bomb in bombs:
            bomb.draw()

        screen.draw.text(f'Pontos: {ship.score}',topleft=(0,0), fontname='pixel', color=(255,255,255), fontsize=15)
        screen.draw.text(f'Vidas: {ship.life}', topright=(800,0), fontname='pixel' ,color=(255,255,255), fontsize=15)
    
    else:
        screen.blit('background',(0,0))
        screen.draw.text(f'Game Over', center=(WIDTH/2,HEIGHT/2),\
                         fontname='pixel', color=(255,255,255), fontsize=30)
        screen.draw.text(f'Pontos: {ship.score}', center=(WIDTH/2,HEIGHT/2+35), fontname='pixel', color=(255,255,255), fontsize=15)


def update():
    global game_over, timeout

    if not game_over:
        ship.update()

        if timeout>100:
            timeout = 0
            coins.append(Item('coin', som=sounds.coleta))
            if len(bombs) < 3:
                bombs.append(Item('bomb', som=sounds.explosao))
            else:
                bombs.pop(0)
                print(len(bombs))

        for coin in coins:
            coin.update()
            ship.collide(coin, coins)

        for bomb in bombs:
            bomb.update()
            ship.collide(bomb, bombs, -1)

        if ship.life == 0:
            game_over = True
        
        timeout += 1

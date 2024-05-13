from random import randint

WIDTH = 800
HEIGHT = 600


class Item(Actor):
    global HEIGHT

    vel = 7

    def set_pos(self):
        self.midtop = randint(20,780), 0


    def update(self):
        self.y += self.vel
        if self.bottom > HEIGHT:
            self.set_pos()    
        


class Hero(Actor):
    global WIDTH

    vel = 7


    def update(self):
        if keyboard.left or keyboard.a:
            ship.x -= self.vel
            if ship.left < 0: # Parede à esquerda
                ship.left = 0
        if keyboard.right or keyboard.d:
            ship.x += self.vel
            if ship.right > WIDTH: # Parede à direita`
                ship.right = WIDTH


ship = Hero('ship', midbottom=(WIDTH/2,HEIGHT))

coin = Item('coin')
coin.set_pos()
bomb = Item('bomb')
bomb.set_pos()

game_over = False


def draw():
    global game_over

    if not game_over:
        screen.blit('background',(0,0))
        coin.draw()
        bomb.draw()
        ship.draw()
    
    else:
        screen.blit('background',(0,0))
        screen.draw.text(f'Game Over', (400,300),\
                         fontname='pixel', color=(255,255,255),
                         fontsize=30)


def update():
    if not game_over:
        coin.update()
        bomb.update()
        ship.update()
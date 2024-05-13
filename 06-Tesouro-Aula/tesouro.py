from random import randint

WIDTH = 800
HEIGHT = 600

bg = Actor('background')

ship = Actor('ship')
ship.x = 400      # Posição horizontal
ship.y = 550      # Posição vertical
ship.scale = 0.8  # Tamanho em relação ao arquivo original

coin = Actor('coin')
coin.x = randint(20,780)
coin.y = 0
coin.scale = 0.5

bomb = Actor('bomb')
bomb.x = randint(20,780)
bomb.y = 0
bomb.scale = 0.5

score = 0
life = 3
game_over = False

def draw():
    global game_over

    if not game_over:
        bg.draw()
        ship.draw()
        coin.draw()
        bomb.draw()
        screen.draw.text(f'Pontos: {score}', (5,5), fontname='pixel', color=(255,255,255), fontsize=15)
        screen.draw.text(f'Vidas: {life}', (690,5), fontname='pixel' ,color=(255,255,255), fontsize=15)
    
    else:
        bg.draw()
        screen.draw.text(f'Game Over', (400,300), fontname='pixel', color=(255,255,255), fontsize=30)
        screen.draw.text(f'Pontos: {score}', (370,350), fontname='pixel', color=(255,255,255), fontsize=15)
        screen.draw.text(f'Vidas: {score}', (370,370), fontname='pixel', color=(255,255,255), fontsize=15)


def update():
    global score, life, game_over

    if not game_over:
        if keyboard.left:
            ship.x -= 7
            if ship.left < 0: # Parede à esquerda
                ship.left = 0
        if keyboard.right:
            ship.x += 7
            if ship.right > WIDTH: # Parede à direita`
                ship.right = WIDTH

        coin.y += 7
        if coin.bottom > HEIGHT:
            coin.y = 0
            coin.x = randint(20,780)
            
        bomb.y += 7
        if bomb.bottom > HEIGHT:
            bomb.y = 0
            bomb.x = randint(20,780)
        
        if ship.colliderect(coin):
            coin.y = 0
            coin.x = randint(20,780)
            score += 1
            sounds.coleta.play()
        
        if ship.colliderect(bomb):
            bomb.y = 0
            bomb.x = randint(20,780)
            life -= 1
            sounds.explosao.play()

        if life == 0:
            game_over = True
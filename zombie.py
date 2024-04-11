from pygame import Color

# Tamanho d janela
WIDTH, HEIGHT = (800,640)
CHAO = 520
VY = - 15
GV = 0.6


class Boneco(Actor):
    
    index = 0
    pulo = 0
    vy = 0


    def update(self):
        self.y += self.vy
        self.vy += GV
        if self.y > CHAO:
            self.y = CHAO
            self.vy = 0
            self.t = 0
        if self.vy != 0: self.animate(0.07)
        if self.vy == 0: self.animate()
        

    def animate(self, v=0.3):
        self.index += v
        self.index = self.index%len(self.images)
        self.image = self.images[int(self.index)]


pumphead = Boneco('walk1',(170,CHAO))
pumphead._rect = ZRect(50,CHAO,50,198)
print(pumphead._rect)
print(ZRect(100,CHAO,50,198))
pumphead.images = [f'walk{i}' for i in range(1,11)]
obstacles = [Actor('cactus',(700,CHAO+70))]
game_over = False
hit = False

def draw():
    global game_over
    if game_over:
        screen.draw.text('Game Over', centerx=400, centery=270, color=(Color('White')), fontsize=60)
    else:
        screen.clear()
        screen.draw.rect(pumphead._rect,Color('Red'))
        pumphead.draw()
        obstacles[0].draw()


def update():
    global game_over, hit
    if keyboard.space and pumphead.vy == 0:
        pumphead.vy = VY
    pumphead.update()
    
    for obs in obstacles:
        obs.x -= 3
        if obs.x < 0:
            obs.x = 820
        
    hit = pumphead.collidelist_pixel(obstacles)
    # print(hit)
    if hit != -1:
        game_over = True


# images = [f'walk{i}' for i in range(1,11)]
# image_counter = 0

# clock.schedule_interval(pumphead.animate, 0.07)
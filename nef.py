from pygame import *
from random import randint
from random import choice

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.rect.w = w
        self.rect.w = w

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y +=self.speed
        if self.rect.y>500-self.rect.height:
            self.rect.x = randint(5,700-5-self.rect.width)
            self.rect.y = -self.rect.height
            self.speed = randint(1,3)
            lost +=1

class Ball(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.speed_x = 0 
        self.speed_y = 0

    def set_direction(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x +=self.speed_x*self.speed
        self.rect.y +=self.speed_y*self.speed

    def check_direction(self, pl1, pl2):
        global point_l, point_r
        if self.rect.y <=0:
            self.speed_y*=-1
        elif self.rect.y >=500-self.rect.height:
            self.speed_y*=-1
        elif self.rect.colliderect(pl1.rect):
            self.speed_x *= -1
        elif self.rect.colliderect(pl2.rect):
            self.speed_x *= -1

        elif self.rect.x <=0:
            point_r += 1
            self.rect.x = 700/2-self.rect.width/2  
            self.rect.y = 500/2-self.rect.height/2  
            self.set_direction(choice([-1,1]), choice([1,1]))

        elif self.rect.x >=700-self.rect.width:
            point_l += 1
            self.rect.x = 700/2-self.rect.width/2  
            self.rect.y = 500/2-self.rect.height/2
            self.set_direction(choice([-1,1]), choice([1,1]))


point_l = 0
point_r = 0
direction= [-1,1]
ball = Ball('asteroid.png', 700/2-25, 500/2-25, 50,50,2)
ball.set_direction(choice(direction), choice(direction))

pl1 = Player('kur.png', 580, 200, 110, 100, 5)
pl2 = Player('kur.png', 30, 30, 110, 100, 5)
enemy_count = 5
enemyes = sprite.Group()


window = display.set_mode((700,500))
display.set_caption('курицы')

background = transform.scale(image.load('fon.jpg'), (700,500))

mixer.init()
mixer.music.load('ok.ogg')
mixer.music.play()

clock = time.Clock()
FPS = 60
game = True

speed_x = 4
speed_y = 4

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    

    window.blit(background, (0,0))
    ball.update()
    ball.check_direction(pl1, pl2)
    ball.reset()
    pl1.update1()
    pl2.update2()
    pl1.reset()
    pl2.reset()




    display.update()
    clock.tick(FPS)
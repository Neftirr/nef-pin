from pygame import *
from random import randint

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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x-=self.speed
        if keys[K_RIGHT] and self.rect.x<700 - 5 - self.rect.width:
            self.rect.x+=self.speed

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y +=self.speed
        if self.rect.y>500-self.rect.height:
            self.rect.x = randint(5,700-5-self.rect.width)
            self.rect.y = -self.rect.height
            self.speed = randint(1,3)
            lost +=1

class ball (GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, spedd)
        self.speed.x = 0 
        self.speed.y = 0

    def set_diretion(self, speed_x, speed_y):
        self.speed.x = speed_x
        self.speed.y = speed_y

    def update(self):
        self.rect.x +=self.speed_x*self.speed
        self.rect.x +=self.speed_y*self.speed

    def check_direction(self, pl1, pl2)
    global point_l, point_r
    if self.rect.y <=-0:
        self.speed_y*=-1
    elif self.rect.y >=500-self.rect.height:
        self.speef_y*=-1
    elif self.rect.spritecollide(pl1.rect):
        self.speed.x *= -1
         elif self.rect.spritecollide(pl2.rect):
        self.speed.x *= -1

    elif self.rect.x <=0:
        point_r += 1
        self.rect.x = 700/2-self.rect.width/2  
        self.rect.x = 700/2-self.rect.height/2  

     elif self.rect.x <=500-self.rect.width:
        point_l += 1
        self.rect.x = 700/2-self.rect.width/2  
        self.rect.x = 700/2-self.rect.height/2  


point_l = 0
point_r = 0
direction []

player  = Player('kur.png', 280, 400, 110, 100, 5)
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

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))



    display.update()
    clock.tick(FPS)
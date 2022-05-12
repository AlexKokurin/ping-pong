
from pygame import *

from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,player_image1,x,y,speed,e,e1):
        super().__init__()
        self.image = transform.scale(image.load(player_image1),(e,e1))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.f = 0
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):    
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > -110:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 330:
            self.rect.y += self.speed
    def update_l(self):    
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -110:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 330:
            self.rect.y += self.speed

class Bal(GameSprite):
    pass

window = display.set_mode((800,600))
display.set_caption('Ping pong')
background = transform.scale(image.load('background.jpg'),(800,600))

bal = Bal('p_p.png',150,150,2,90,90)
Player1 = Player('stena.png',8,50,2,20,390)
Player2 = Player('stena.png',770,50,2,20,390)

game = True
finish = False
clock = time.Clock()
FPS = 60
flag = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        bal.reset()
        Player1.update_l()
        Player2.update_r()
        Player1.reset()
        Player2.reset()
    display.update()

from pygame import *

from random import randint
from time import time as timer

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
        if keys[K_UP] and self.rect.y > -10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed
    def update_l(self):    
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 430:
            self.rect.y += self.speed

class Bal(GameSprite):
    pass

window = display.set_mode((800,600))
display.set_caption('Ping pong')
background = transform.scale(image.load('background.jpg'),(800,600))

ball = Bal('p_p.png',150,150,2,90,90)
Player1 = Player('stena.png',8,50,3,20,150)
Player2 = Player('stena.png',770,50,3,20,150)

font.init()
font = font.Font(None,70)
lose1 = font.render('Player1 lose!',True,(255,215,0))
lose2 = font.render('Player2 lose!',True,(255,215,0))
start1 = timer()
start = timer()
speed_x = 3
speed_y = 3
game = True
finish = False
clock = time.Clock()
FPS = 150
flag = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        if timer()-start > 10:
            if speed_x < 0:
                speed_x -= 1
            else:
                speed_x += 1
            if speed_y < 0:
                speed_y -= 1
            else:
                speed_y += 1
            start = timer()
        window.blit(background,(0,0))
        ball.reset()
        Player1.update_l()
        Player2.update_r()
        Player1.reset()
        Player2.reset()
        clock.tick(FPS)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 0 or ball.rect.y > 500:
            speed_y *= -1
        if sprite.collide_rect(Player1,ball) or sprite.collide_rect(Player2,ball):
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(lose1,(10,10))
            finish = True
        if ball.rect.x > 690:
            window.blit(lose2,(10,10))
            finish = True
        t = font.render(str(int(timer()-start1)),True,(0,0,0))
        window.blit(t,(750,0))
    display.update()
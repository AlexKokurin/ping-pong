
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


window = display.set_mode((800,600))
display.set_caption('Ping pong')
background = transform.scale(image.load('background.jpg'),(800,600))

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
    display.update()
# Разработай свою игру в этом файл
from pygame import *
window = display.set_mode((700,500))
display.set_caption("First_Game")
picture = transform.scale(image.load('white.png'), (700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_x_speed,player_y_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y +=self.y_speed
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.x_speed = 10
        elif self.rect.x >= 570:
            self.x_speed = - 10

wall_1 = GameSprite('black.png',300,150,50,350)
wall_2 = GameSprite('black.png',150,300,150,50)
wall_3 = GameSprite('black.png',500,300,200,50)
wall_4 = GameSprite('black.png',0,150,150,50)
wall_5 = GameSprite('black.png',300,150,250,50)
enemy = Enemy('finish.png',100,50,80,80,10)
packman = Player('boar_016.png',180,380,80,80,0,0)
run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key == K_LEFT:
                packman.x_speed = -8
            elif i.key == K_RIGHT:
                packman.x_speed = 8
            elif i.key == K_UP:
                packman.y_speed = -8
            elif i.key == K_DOWN:
                packman.y_speed = 8 
        elif i.type == KEYUP:
            if i.key == K_LEFT:
                packman.x_speed = 0
            elif i.key == K_RIGHT:
                packman.x_speed = 0
            elif i.key == K_UP:
                packman.y_speed = 0
            elif i.key == K_DOWN:
                packman.y_speed = 0
  
    window.blit(picture, (0,0))
    wall_1.reset()
    wall_2.reset()
    wall_3.reset()
    wall_4.reset()
    wall_5.reset()
    packman.reset()
    packman.update()
    enemy.reset()
    enemy.update()
    time.delay(50)
    display.update()
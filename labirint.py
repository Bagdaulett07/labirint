# Разработай свою игру в этом файл
from pygame import *
window = display.set_mode((700,500))
display.set_caption("First_Game")
picture = transform.scale(image.load('wallpaper.jpg'), (700, 500))
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
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_x_speed,player_y_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        if self.rect.x <= 470:
            self.rect.x += self.x_speed
        elif self.rect.x == 620:
            self.rect.x -= self.x_speed

wall_1 = GameSprite('wall.png',300,150,50,350)
wall_2 = GameSprite('wall.png',150,300,150,50)
wall_3 = GameSprite('wall.png',500,300,200,50)
wall_4 = GameSprite('wall.png',0,150,150,50)
wall_5 = GameSprite('wall.png',300,150,250,50)
enemy = Enemy('enemy(1).png',60,60,80,80,10,0)
packman = Player('hero.png',180,380,50,50,0,0)
final = GameSprite('pac-7.png',600,400,80,80)
lose = GameSprite('lose(1).png',0,0,700,500)
win = GameSprite('win.png',0,0,700,500)
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
    if sprite.collide_rect(packman, enemy) or sprite.collide_rect(packman, wall_1) or sprite.collide_rect(packman, wall_2) or sprite.collide_rect(packman, wall_3) or sprite.collide_rect(packman, wall_4) or sprite.collide_rect(packman, wall_5):
        lose.reset()
        display.update()
        time.delay(2000)      
        run = False
        
    
    elif sprite.collide_rect(packman, final):
        win.reset()
        display.update()
        time.delay(2000)
        finish = False

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
    final.reset()
    time.delay(30)
    display.update()
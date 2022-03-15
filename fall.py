from tkinter import image_types
import pygame
import random
pygame.init()


blue = (50, 153, 213)
black = (0, 0, 0)
white = (255, 255, 255)


dis_width = 1000
dis_height = 700

img_width = 60
img_height = 64

x1 = dis_width/2 - img_width/2

y1 = 565

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Anika's game")

anikaImg = pygame.image.load('self.png').convert_alpha()
space_debris = pygame.image.load('wires.png').convert_alpha()
belong_inspace = pygame.image.load('astronaut.png')




class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = anikaImg
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def restart(self):
        x1 = (dis_width/2) - (img_width/2)
        y1 = dis_height-img_height  
        self.rect.topleft = [x1, y1]



class fallSprites(pygame.sprite.Sprite):
    def __init__(self, debris, image_types, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_types
        self.capture = debris
        self.rect = self.image.get_rect()
        self.rect.topleft = pos



    def update(self):
        self.rect.y +=2
        if self.rect.y > dis_height:
            self.rect.topleft = [random.randint(0,dis_width), -20]
    def restart(self):
        self.rect.topleft= [random.randint(0,dis_width), -20]

    def is_collided_with(self, anika):
        
        return self.rect.colliderect(anika.rect)
    


wires = fallSprites(True, space_debris, [random.randint(0,dis_width), -20])
astronaut = fallSprites(False, belong_inspace, [random.randint(0,dis_width), -20])

anika = Player([x1, y1])
background = pygame.image.load("car.jpeg").convert()
myfont1 = pygame.font.SysFont('Comic Sans MS', 100)
myfont2 = pygame.font.SysFont('Comic Sans MS', 40)



y=dis_height
game_open = True
game_over = True
score = 0
while game_open:
    dis.fill(black)
    title = myfont1.render("Welcome to Space Trip!", True, white)
    beginbut = myfont2.render("press SPACE to begin", True, white)
    title_rect = title.get_rect(center = (dis_width/2, 300))
    beginbut_rect = beginbut.get_rect(center = (dis_width/2, 400))
    dis.blit(title, title_rect)
    dis.blit(beginbut, beginbut_rect)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_open = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        game_over = False

    while not game_over:
        rel_y = y % background.get_rect().height
        dis.blit(background, (0,rel_y - background.get_rect().height))
        if rel_y < dis_height:
            dis.blit(background, (0, rel_y))
        y+=1
        dis.blit(anika.image, anika.rect)
        dis.blit(wires.image, wires.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_open = False
                game_over = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and y1 > 0:
            x1 -= 2
        if keys[pygame.K_RIGHT] and y1 < dis_height-img_height:
            x1 += 2
       

        if wires.is_collided_with(anika):
            wires.restart()
            score = score+1


        anika.rect.topleft = [x1, y1]
        wires.update()
        pygame.display.update()
    pygame.display.update()




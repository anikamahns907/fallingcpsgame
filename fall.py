
from tkinter import image_types
import time
import pygame
import random
username = input("Hi there! welcome to my awesome game. whats your name?\n")
pygame.init()


blue = (50, 153, 213)
black = (0, 0, 0)
white = (255, 255, 255)


dis_width = 800
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
            self.rect.topleft = [random.randint(0,dis_width-75), -20]
    def restart(self):
        self.rect.topleft= [random.randint(0,dis_width-75), -20]

    def is_collided_with(self, anika):
        
        return self.rect.colliderect(anika.rect)


    


wires = fallSprites(True, space_debris, [random.randint(0,dis_width-30), -20])
astronaut = fallSprites(False, belong_inspace, [random.randint(0,dis_width-30), -20])

anika = Player([x1, y1])
background = pygame.image.load("car.jpeg").convert()
myfont1 = pygame.font.SysFont('Comic Sans MS', 70)
myfont2 = pygame.font.SysFont('Comic Sans MS', 40)
myfont3 = pygame.font.SysFont('Comic Sans MS', 40)
myfont4 = pygame.font.SysFont('Comic Sans MS', 20)


y=dis_height
game_open = True
game_over = True
completed = False
score = 0

lastcollided = []
multiplier = 1



while game_open:
    dis.fill(black)
    if completed == False:
        title = myfont1.render("Welcome to Space Trip!", True, white)
    else:
        title = myfont4.render("Mission complete. Time taken: " +str(round(final_time, 2)) + " seconds", True, white)
        
    beginbut = myfont4.render("press SPACE to begin a mission", True, white)
    title_rect = title.get_rect(center = (dis_width/2, 300))
    beginbut_rect = beginbut.get_rect(center = (dis_width/2, 400))
    dis.blit(title, title_rect)
    dis.blit(beginbut, beginbut_rect)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_open = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        start_time = time.time()
        print(start_time)
        game_over = False
        completed = False
        score = 0

        lastcollided = []
        multiplier = 1



     
    

    while not game_over:

        rel_y = y % background.get_rect().height
        dis.blit(background, (0,rel_y - background.get_rect().height))
        if rel_y < dis_height:
            dis.blit(background, (0, rel_y))
        y+=1
        dis.blit(anika.image, anika.rect)
        dis.blit(wires.image, wires.rect)
        dis.blit(astronaut.image, astronaut.rect)
        scoring = myfont3.render(str(username) +"'s score: " + str(score), True, white)
        dis.blit(scoring, (20, 20))

        multipliertext = myfont3.render("Multipler = " + str(multiplier), True, white)
        dis.blit(multipliertext, (600, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_open = False
                game_over = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x1 > 0:
            x1 -= 2
        if keys[pygame.K_RIGHT] and x1 < dis_width - 130:
            x1 += 2
       
        wrongitem = 0
        if wires.is_collided_with(anika):
            lastcollided.append(True)
            if len(lastcollided) > 3:
                lastcollided.pop(0)
            wires.restart()
            print(lastcollided)
            if all(lastcollided) and len(lastcollided) == 3:
                multiplier = 2
                print("hey")
            else:
                multiplier = 1
            score = score + (1 * multiplier)

        if astronaut.is_collided_with(anika):
            lastcollided.append(False)
            if len(lastcollided) > 3:
                lastcollided.pop(0)
            astronaut.restart()
            multiplier = 1
            score = score-1

        if score >= 5:
            print("score reached")
            final_time = time.time() - start_time
            game_over = True
            completed = True
        anika.rect.topleft = [x1, y1]
        wires.update()
        astronaut.update()
        pygame.display.update()
    
    # while completed and game_over:
    #     end = myfont1.render("GAME OVER | " + str(username) + " 's time: " + str(final_time), True, white)
    #     restart = myfont2.render("Press SPACE to play again", True, white)
    #     end_rect = end.get_rect(center = (dis_width/2, 300))
    #     restart_rect = restart.get_rect(center = (dis_width/2, 400))
    #     dis.blit(end, end_rect)
    #     dis.blit(restart, restart_rect)
    #     if keys[pygame.K_SPACE]:
    #         game_over = False
    #         completed = False
    #         break
    #     pygame.display.update()
       
       


        
    



        
        
        



    pygame.display.update()
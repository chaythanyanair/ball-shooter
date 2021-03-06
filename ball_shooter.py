# This is a small shooting game demo

import pygame, sys
from pygame.locals import *
import random
black=(0,0,0)
white=(255,255,255)
pygame.init()
level=0
# make window called screen 
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('my ball shooter game')
# load targets in array
targetnum = 2
target = []
for i in range(targetnum):
    targetimage = pygame.image.load('ball.jpg')
    targetimage = pygame.transform.scale(targetimage,(40,40))
    target.append([])
    target[i] = targetimage
blast = pygame.image.load('blast.png')
blast = pygame.transform.scale(blast,(40,40))
        
targetpos = []
for i in range(targetnum):
    targetpos.append([])
    targetpos[i].append((random.randrange(10,1000)+random.randrange(10,1000))/2)
    targetpos[i].append(random.randint(0,50))
		

# target visible set up of the array
targetvisible = []
for i in range(targetnum):
    targetvisible.append(True)

player = pygame.image.load('starship.jpg')
player = pygame.transform.scale(player,(50,40))
px,py = (width-50)/2,550
gameover = pygame.image.load('gameover.jpg')
gameover = pygame.transform.scale(gameover,(width,height))
restart = pygame.image.load('restart.jpeg')
restart = pygame.transform.scale(restart,(100,100))
bravo = pygame.image.load('bravo.jpeg')
bravo = pygame.transform.scale(bravo,(100,100))
gun=pygame.mixer.Sound('machine.wav')


# speed of game and other variables initiated
clock = pygame.time.Clock()
gamespeed = 15
movex = movey = 0

speed = []
for i in range(targetnum):
    speed.append([])
    for j in range(2):
        speed[i].append(gamespeed*random.randint(1,5))

score = 0

# this is the score text loading
gamefont = pygame.font.Font(None,30)
scoretext = gamefont.render("player score: "+str(score), 2, [255,0,0])
boxsize = scoretext.get_rect()
scoreXpos = (width-boxsize[2])/2
levelfont = pygame.font.Font(None,30)
leveltext = gamefont.render("LEVEL: "+str(level), 2, [255,0,0])
levelsize = scoretext.get_rect()
levelXpos = (width-levelsize[2]-200)/2
def blitnew(a):
    global targetnum
    global targetvisible
    global level
    global score
    level=level+1
    targetnum=targetnum+1
    global targetpos
    global speed
    global gamespeed
    global target
    global targetimage
    gamespeed=gamespeed+2
    if a==0:
        score=0
        level=0
        targetnum=2
        gamespeed=15
      

    targetpos = []
    for i in range(targetnum):
        targetpos.append([])
        targetpos[i].append(random.randrange(10,950))
        targetpos[i].append(random.randint(0,50))
    targetvisible = []
    for i in range(targetnum):
        targetvisible.append(True)
    speed = []
    for i in range(targetnum):
        speed.append([])
        for j in range(2):
            speed[i].append(gamespeed*random.randint(1,5))
    target = []
    for i in range(targetnum):
        targetimage = pygame.image.load('ball.jpg')
        targetimage = pygame.transform.scale(targetimage,(40,40))
        target.append([])
        target[i] = targetimage

def check_reset(x,y):
    print "hello check entered"
    if x>=450 and x<=550 and y>=450 and y<=650:
        print "hello reset is pressed"
        blitnew(0)
def brav_o():
    screen.fill(black)
    screen.blit(bravo,(width/2,height/2))
    font = pygame.font.Font(None,100)
    text = gamefont.render("Moving to next level.....", 4, [0,255,0])
    screen.blit(text,(300,450))
    pygame.display.update()

    pygame.time.delay(500)
    blitnew(1)
     
def game_over():
    screen.blit(gameover,[0,0])
    pygame.display.update()
    font = pygame.font.Font(None,100)
    text = gamefont.render("Restarting game.....", 4, [255,0,0])
    screen.blit(text,(300,450))
    pygame.display.update()

    pygame.time.delay(2000)
    blitnew(0)
    
    
# running of the game loop
while True:
    # image display updates
    seconds = clock.tick()/1000.0
    
    screen.fill(black)
    screen.blit(player,(px,py))
    leveltext=levelfont.render("LEVEL:"+str(level),2,[255,255,255])
    scoretext = gamefont.render("player score: "+str(score), 2, [255,255,255])
    screen.blit(scoretext,[scoreXpos,20])
    screen.blit(leveltext,[levelXpos-50,20])
    # target blited through a for loop
    for i in range(targetnum):
        if targetvisible[i]:
            targetpos[i][1] += seconds*speed[i][1]
            targetimage = target[i]
            x = targetpos[i][0]
            y = targetpos[i][1]
            screen.blit(targetimage, (x,y))
    pygame.display.update()
   # for i in range(targetnum):
   #    if targetpos[i][0]>=px and targetpos[i][0]<=px+50 and targetpos[i][1]>=py:
   #	    game_over()
            
    # keyboard and/or mouse movements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                movex = 5
            if event.key == K_LEFT:
                movex = -5
	    if event.key==pygame.K_SPACE:
                gun.play(loops=0,maxtime=0)
                x_c=22
                y_c=25
                temp=py
                while py>0:
                    pygame.draw.rect(screen,white,[px+x_c,py-y_c,5,20])
                    for i in range(targetnum):
                        if  px+x_c>targetpos[i][0] and px+x_c<targetpos[i][0]+40:
                            targetvisible[i]=False
                            screen.blit(blast,(targetpos[i][0],targetpos[i][1]))
                            score+=1
                            targetpos[i][0]=100000
                            targetpos[i][1]=100000

                            pygame.display.update()
                    py=py-y_c
                    pygame.display.flip()
                py=temp

        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                movex = 0
            if event.key == K_LEFT:
                movex = 0
                   
    px = px + movex
    py += movey
    flag=1
    win=1
    for i in range(targetnum):
        if targetpos[i][1]<height:
            flag=0
            break
    if flag==1:
        for i in range(targetnum):
            if targetpos[i][1]>550 and targetpos[i][1]<700:
                win=0
                game_over()
                break         
        if win==1:
            brav_o()
        


   
    
	

            
















import pygame
import math
import sys
import random
pygame.init()
size=(1000,700)
white=(255,255,255)
black=(0,0,0)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("my starship game")
done=False
    # load targets in array
targetnum = 10
target = []
for i in range(targetnum):
	targetimage = pygame.image.load('ball.jpg')
	targetimage = pygame.transform.scale(targetimage,(40,40))
	target.append([])
	target[i] = targetimage

targetpos = []
targetspace = 700/targetnum-10
for i in range(targetnum):
	targetpos.append([])
	for j in range(2):
		targetpos[i].append(i*j*targetspace+50)
 # target visible set up of the array
targetvisible = []
for i in range(targetnum):
	targetvisible.append(True)
star_ship=pygame.image.load('starship.jpg').convert()
star_ship = pygame.transform.scale(star_ship,(60,60))
gamespeed = 100
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
scoreXpos = (1000-boxsize[2])/2


plane_x=450
plane_y=600
x_change=25
x_change2=5
y_change=0
count=15
stone_list=[]
clock=pygame.time.Clock()
	
screen.fill(black)
while True:

	seconds=clock.tick()/1000.0
	#screen.blit(star_ship,[450,600])
	#screen.blit(star_ship,[450,600])
	
	        # target blited through a for loop
	for i in range(targetnum):
		if targetvisible[i]:
			targetpos[i][0] += seconds*speed[i][0]
			targetpos[i][1] += seconds*speed[i][1]
			targetimage = target[i]
			x = targetpos[i][0]
			y = targetpos[i][1]
			screen.blit(targetimage, (x,y))
		else:
			targetimage = target[i]
			x = width - 50
			y = height-(i+1)*targetspace
			screen.blit(targetimage, (x,y))
	pygame.display.update()

	for event in pygame.event.get():
		pygame.display.update()
		if event.type==pygame.QUIT:
        		pygame.quit()
			sys.exit()
		screen.fill(black)
		screen.blit(star_ship,[plane_x,plane_y])

		#pygame.display.flip()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				plane_x=plane_x-12
			elif event.key==pygame.K_RIGHT:
				plane_x=plane_x+12
			elif event.key==pygame.K_SPACE:
				x_c=40
				y_c=25
				temp=plane_y
				while plane_y>0:
					pygame.draw.rect(screen,white,[plane_x+x_c,plane_y-y_c,5,20])
					plane_y=plane_y-y_c
					pygame.display.flip()
			
				plane_y=temp
		if event.type==pygame.KEYUP:
                        if event.key==pygame.K_LEFT:
                                plane_x=plane_x-0
                        elif event.key==pygame.K_RIGHT:
                                plane_x=plane_x+0
                        elif event.key==pygame.K_SPACE:
                                x_c=40
                                y_c=25
                                temp=plane_y
                                while plane_y>0:
                                        pygame.draw.rect(screen,white,[plane_x+x_c,plane_y-y_c,5,20])
                                        plane_y=plane_y-y_c
                                        pygame.display.flip()

                                plane_y=temp

			
				
	pygame.display.flip()
	



























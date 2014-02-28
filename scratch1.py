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
star_ship=pygame.image.load('starship.jpg').convert()
done=False
plane_x=450
plane_y=600
x_change=25
x_change2=5
y_change=0
count=5
stone_list=[]
clock=pygame.time.Clock()
	
screen.fill(black)
for i in range(count):
	x=random.randrange(10,1000)
	y=random.randrange(10,700)
	stone_list.append([x,y])
while done==False:
	for i in range(len(stone_list)):
		screen.fill(black)
		screen.blit(star_ship,[plane_x,plane_y])
        	pygame.draw.circle(screen,white,stone_list[i],15)
                stone_list[i][1]+=3
                y=random.randrange(0,10)
                x=random.randrange(0,650)
                if stone_list[i][1]>700:
                	stone_list[i][1]=y
                        stone_list[i][0]=x
                        pygame.display.update()


	clock.tick(10)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
        		done=True
		screen.fill(black)
		screen.blit(star_ship,[plane_x,plane_y])
	#	for i in range(len(stone_list)):
 	 #     		pygame.draw.circle(screen,white,stone_list[i],15)
         #     		stone_list[i][1]+=3
       # 		y=random.randrange(0,10)
       # 		x=random.randrange(0,650)
       #        		if stone_list[i][1]>700:
     #                 		stone_list[i][1]=y
      #                		stone_list[i][0]=x
#			pygame.display.flip()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				plane_x=plane_x-x_change
			elif event.key==pygame.K_RIGHT:
				plane_x=plane_x+x_change
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
	



























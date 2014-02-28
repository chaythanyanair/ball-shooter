import sys, pygame 
import random 
import math 
pygame.init() 
 
resolution = (320,240) 
 
#Set up Screen 
screen = pygame.display.set_mode(resolution) 
pygame.display.set_caption('Tutorial 5 -- Pong') 
sfBackground = pygame.Surface(screen.get_size()) 
sfBackground = sfBackground.convert() 
sfBackground.fill((0,0,0)) 
 

class GameObject: 
    global screen 
    global background 
    global resolution 
     
    def __init__(self,x,y): 
        self.x = x 
        self.y = y 
     
    def move(self,dx,dy): 
        self.x = dx 
        self.y = dy 
 
 
class Ball(GameObject): 
    x,y = (0,0) 
    dx,dy = (0,0) 
    radius = 10 
 
    def __init__(self,pos,speed,radius): 
        GameObject.__init__(self,pos[0],pos[1])       
        self.dx = speed[0] 
        self.dy = speed[1] 
        self.radius = radius 
               
    def move(self): 
         
        self.x += self.dx  
        self.y +=  self.dy 
  
        if ((self.x > resolution[0] - self.radius ) or (self.x <= self.radius )): 
            self.x = resolution[0]//2 
            self.y = resolution[1]//2 
            return 
                
        if ((self.y >= resolution[1] - self.radius) or (self.y <= self.radius)): 
            self.dy *= -1 
             
        if ((self.x >= resolution[0] - self.radius) or (self.x <= self.radius)): 
            self.dx *= -1 
         
 
     
    def draw(self): 
        pygame.draw.circle(sfBackground,(255,255,255),(self.x,self.y),self.radius,0)         
 
 
class Paddle(GameObject): 
    def __init__(self,x,y,size): 
        GameObject.__init__(self, x, y) 
        self.size = size 
     
    def move(self,dy): 
        self.y += dy  
        if (self.y < 0 ): self.y = 0 
        if (self.y + self.size > resolution[1]): self.y = resolution[1] - self.size 
 
     
    def draw(self): 
        pygame.draw.rect(sfBackground, (255,255,255), (self.x, self.y, 3, self.size ), 0) 
 
 
      
player_one  = Paddle(0,resolution[1]//2-10,50) 
player_two  = Paddle(resolution[0]-4,resolution[1]//2-10,50) 
 
pos = (resolution[0]//2,resolution[1]//2) 
speed = (2,2) 
ball = Ball(pos,speed,5) 
                 
while 1: 
 
    for event in pygame.event.get(): 
        if (event.type == pygame.QUIT  or (event.type == pygame.KEYDOWN and event.key  == pygame.K_ESCAPE)): 
            sys.exit() 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: 
                player_one.move(-10) 
            elif event.key == pygame.K_z: 
                player_one.move(10) 
            elif event.key == pygame.K_k: 
                player_two.move(-10) 
            elif event.key == pygame.K_m: 
                player_two.move(10)                 
                     
    sfBackground.fill((0,0,0)) 
     
    player_one.draw() 
    player_two.draw() 
    ball.move() 
    if ( (abs(player_one.x - (ball.x - ball.radius)) <= 5) and (abs(player_one.y - (ball.y + ball.radius) ) <= player_one.size)): 
        ball.dx *= -1 
     
    if ((abs(player_two.x - (ball.x + ball.radius)) <= 5) and (abs(player_two.y - (ball.y + ball.radius) ) <= player_two.size)): 
        ball.dx *= -1 
     
    ball.draw()     
     
    screen.blit(sfBackground, (0,0)) 
    pygame.display.flip() 





























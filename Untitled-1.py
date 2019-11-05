'''
counter = input("podaj: ")
counter = int(counter)

for i in range(counter):
    print(i)
    '''
import time
import pygame
import random
pygame.init()
random.seed()

WINDOW_SIZE = (666,666)
screen = pygame.display.set_mode(WINDOW_SIZE) 
timer = pygame.time.Clock()
FPS = 120
x=50
y=300
speedy = 0
speedx = 0
balls = []

size_init = 100
def draw(x, y, size_init):
    pygame.draw.circle(screen,(233,0,0),(x,y),size_init,6)

class Ball:
    def __init__(self):

        self.size = 20
        self.color = (random.randint(0,225),random.randint(0,225),random.randint(0,225))

        self.x = random.randint(0,666)
        self.y = random.randint(0,666)

    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.size, 2)

while True:

    x += speedx
    y += speedy
    ball1 = Ball()

    

    for event in pygame.event.get():
        print(event)
        if event.type != pygame.KEYUP:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if x + 101 >= 666:
                    print("Dupa")
                    speedy = 0
                    speedx = 0
                else:
                    
                    speedx = 1
        

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if x - 101 <= 0:
                    print("Dupa")
                    speedy = 0
                    speedx = 0
                else:
                    
                    speedx = -1
               
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if y - 101 <= 0:
                    print("Dupa")
                    speedy = 0
                    speedx = 0
                else:
                    
                    speedy = -1
               
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if y + 101 >= 666:
                    print("Dupa")
                    speedy = 0
                    speedx = 0
                else:
                    
                    speedy = 1


        else:
            speedx = 0
            speedy = 0
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    screen.fill((0,0,255))
    draw(x,y, size_init)
    for i in range(100):
        new = Ball()
        balls.append(new)
    for ball in balls:
        ball.draw()

    pygame.display.update()
    timer.tick(FPS)


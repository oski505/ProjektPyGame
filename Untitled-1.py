'''
counter = input("podaj: ")
counter = int(counter)

for i in range(counter):
    print(i)
    '''
import time
import pygame

pygame.init()

WINDOW_SIZE = (666,666)
screen = pygame.display.set_mode(WINDOW_SIZE) 

def draw(x, y):
    pygame.draw.circle(screen,(233,0,0),(x,y),10,2)

while True:
    for event in pygame.event.get():
        print(event)

      
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0,0,255))
    draw(300,300)

    
pygame.display.update()


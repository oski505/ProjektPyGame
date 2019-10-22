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
x=50
y=300
size_init = 100
def draw(x, y, size_init):
    pygame.draw.circle(screen,(233,0,0),(x,y),size_init,6)

while True:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if x + 130 >= 666:
                print("Dupa")
            else:

                x = x+30
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if x + 130 >= 666:
                print("Dupa")
            else:

                x = x-30
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if x + 130 >= 666:
                print("Dupa")
            else:

                y = y+30
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if x + 130 >= 666:
                print("Dupa")
            else:

                y = y-30

      
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0,0,255))
    draw(x,y, size_init)

    pygame.display.update()


import pygame

from pygame.constants import K_DOWN, K_RIGHT

from snake_class import *
from food import *
from scoreboard import *

#init pygame
pygame.init()

#define some colours in RGB
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

#screen width and height
WIDTH = 800
HEIGHT = 600

#create screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("NE111 Game: Snake")

#refresh rate
clock = pygame.time.Clock() 
FPS = 60

#food class variable
fod = food(RED,(20,20),food_pos)

#scoreboard class variable
score_count = 0
score = scoreboard("Ariel", 24, score_count, BLACK, (0,0))

#snake class variable
player = snake(snake_direction, snake_length, BLUE, 5, snake_body)

#gameloop
running = True
while running: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = (0,-5)
            elif event.key == pygame.K_DOWN:
                snake_direction = (0,5)
            elif event.key == pygame.K_LEFT:
                snake_direction = (-5,0)
            elif event.key == pygame.K_RIGHT:
                snake_direction = (5,0)

    #fill screen
    screen.fill(WHITE)

    fod.food_draw(screen)

    score.draw_score(screen)

    player.draw(screen)


    
    head = snake_body[0]
    move = (head[0]+snake_direction[0], head[1]+snake_direction[1])
    snake_body.insert(0, move)

    while len(snake_body) > snake_length:
        snake_body.pop()

    #update screen
    pygame.display.flip()

    #refresh 60 times a second
    clock.tick(FPS)

pygame.quit()
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
fod = food(RED, (20,20), rnd_food)

#snake class variable
player = snake(snake_direction, BLUE, 20, snake_body)

#scoreboard class variable
score_count = 0
score = scoreboard("Ariel", 24, score_count, BLACK, (0,0))

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
                
    
    if snake_direction == (0,-5):
        curr_pos[1] -= 10
    if snake_direction == (0,5):
        curr_pos[1] += 10
    if snake_direction == (-5,0):
        curr_pos[0] -= 10
    if snake_direction == (5,0):
        curr_pos[0] += 10
    

    snake_body.insert(0, list(curr_pos))
    snake_body.pop()

    if (player.head).colliderect(fod.food_po):
        rnd_food = (random.randrange(790), random.randrange(590))

    #fill screen
    screen.fill(WHITE)

    fod.food_draw(screen)

    score.draw_score(screen)

    player.draw(screen)

    #update screen
    pygame.display.flip()

    #refresh 60 times a second
    clock.tick(FPS)

pygame.quit()
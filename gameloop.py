import pygame
from pygame.constants import K_DOWN, K_RIGHT

from snake_class import *
from food import *
from scoreboard import *
from gameover import *

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

#check if game is done
game_done = False

#gameloop
running = True
while running: 

    #define class variables
    fod = food(RED, 20, new_food)
    player = snake(BLUE, 20, snake_body)
    score = scoreboard("Ariel", 24, score_count, BLACK, (0,0))
    game_s = gamechange(WIDTH, HEIGHT)

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = -1
            elif event.key == pygame.K_DOWN:
                snake_direction = 1
            elif event.key == pygame.K_LEFT:
                snake_direction = -2
            elif event.key == pygame.K_RIGHT:
                snake_direction = 2
                
    #direction changes
    if snake_direction == -1 and direct != "DOWN":
        direct = "UP"
    if snake_direction == 1 and direct != "UP":
        direct = "DOWN"
    if snake_direction == -2 and direct != "RIGHT":
        direct = "LEFT"
    if snake_direction == 2 and direct != "LEFT":
        direct = "RIGHT"
    
    if direct == "UP":
        curr_pos[1] -= speed
    if direct == "DOWN":
        curr_pos[1] += speed
    if direct == "LEFT":
        curr_pos[0] -= speed
    if direct == "RIGHT":
        curr_pos[0] += speed
    
    #snake movement 
    snake_body.insert(0, list(curr_pos))
    snake_body.pop()

    #food collision
    if pygame.Rect.colliderect(player.segment, fod.food_po):
        snake_body.append(new_food)
        new_food_que = [random.randrange(780), random.randrange(580)]
        for pos in snake_body:
            if pos != new_food_que:
                new_food = new_food_que
        score_count += 10

    #border collision
    if curr_pos[0] > WIDTH-20 or curr_pos[0] < 0 or curr_pos[1] > HEIGHT-20 or curr_pos[1] < 0:
        game_done = True
        game_s.gameover(screen, score_count)

    #collision with itself
    if direct != None:
        starting_pos = None

    for snake_pos in snake_body[1:]:
        if snake_pos[0] == curr_pos[0] and snake_pos[1] == curr_pos[1]:
            if starting_pos == None:
                game_s.gameover(screen, score_count)

    #fill screen
    if game_done == False:
        screen.fill(WHITE)

        fod.food_draw(screen)

        score.draw_score(screen)

        player.draw(screen)

        #update screen
        pygame.display.flip()

    #refresh 60 times a second
    clock.tick(FPS)

pygame.quit()
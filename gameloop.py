import pygame
from pygame.constants import K_DOWN, K_RIGHT

from snake_class import *
from food import *
from scoreboard import *
from gameover import *
import menu

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

#user preference variables
#---------------------------------------------------
#choices for apple-count setting
apple_counts = [1,3,5]

#choices for speed setting
speeds = [3,6,9]

#global variable to be set in menu then used during gameplay
settings = {"apple_count_index":0, "speed_index": 0, "infinite_mode":False}
#----------------------------------------------------


def gameloop(settings):
    #check if game is done
    game_done = False

    #first food pos
    new_food = [random.randrange(790), random.randrange(590)]


    #snake variables
    snake_body = [[100, 50], [90, 50], [80, 50]]
    curr_pos = [snake_body[0][0], snake_body[0][1]]
    speed = speeds[settings["speed_index"]]

    starting_pos = [100, 50]
    #snake is stationary until first button press
    snake_direction = None
    change_dir = None
    direct = None

    #scoreboard counter
    score_count = 0

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
            #don't continue looping if quit button pressed
            if event.type == pygame.QUIT:
                running = False
                menu.terminate()

            #values assignments based on button pressed, value arbitrary as long as it's unique from others
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
        if settings["infinite_mode"]:
            #each wall connects to the opposite wall in infinite mode
            if curr_pos[0] > WIDTH-20:
                curr_pos[0] = 0
            elif curr_pos[0] < 0:
                curr_pos[0]=WIDTH-20
            elif curr_pos[1] > HEIGHT-20:
                curr_pos[1] = 0
            elif curr_pos[1] < 0:
                curr_pos[1] = HEIGHT-20

        #normal behavior, not in infinite mode
        elif curr_pos[0] > WIDTH-20 or curr_pos[0] < 0 or curr_pos[1] > HEIGHT-20 or curr_pos[1] < 0:
            running = False
            game_s.gameover(screen, score_count)

        #collision with itself
        if direct != None:
            starting_pos = None

        for snake_pos in snake_body[1:]:
            if snake_pos[0] == curr_pos[0] and snake_pos[1] == curr_pos[1]:
                if starting_pos == None:
                    print(snake_pos)
                    running = False
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


while True:
    settings = menu.show_menu(settings, apple_counts, speeds, screen, WIDTH, HEIGHT, clock)
    gameloop(settings)
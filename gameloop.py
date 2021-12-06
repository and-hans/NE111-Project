#This Module was made by Andrew Hanraj,
#Menu, inifite mode, new food location finding added by Sawyer Hossfeld, also changed control flow
#Comments done by Eugene Jang


#import pygame library, and all the other made libraries
import pygame
from pygame.constants import K_DOWN, K_RIGHT

from snake_class import *
from food import *
from scoreboard import *
from gameover import *
import menu

#initialize pygame
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

#user preference variables
#---------------------------------------------------
#choices for apple-count setting, this hasn't been implemented and probably won't be
apple_counts = [1,3,5]

#choices for speed setting, cooresponds to fps
speeds = [30,60,90]

#global variable to be set in menu then used during gameplay
settings = {"apple_count_index":0, "speed_index": 0, "infinite_mode":False}
#----------------------------------------------------


def gameloop(settings):
    #check if game is done
    game_done = False

    #foods first position
    new_food = [random.randrange(790), random.randrange(590)]


    #snake variables initialization
    snake_body = [[100, 50], [90, 50], [80, 50]]
    curr_pos = [snake_body[0][0], snake_body[0][1]]
    
    #set snakes movement per frame in pixels, should be less than body width
    speed =  6

    starting_pos = [100, 50]
    #snake is stationary until first button press
    snake_direction = None
    #used for telling which direction the snake cannot move
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
                if event.key == pygame.K_ESCAPE:
                    return

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
        #If the direct variable does not equal DOWN and the snake_direction variable equals -1 (from keyboard input), then it will move the snake up. 
        #But if the direct variable equals DOWN, then it won't work, as it looks at what the direct varibale equals to, before changing it to a new position.
        #If all conditions are met, then the snake will current position changes by the speed it should be moving
    
        #snake movement 
        snake_body.insert(0, list(curr_pos))    #insert the current position into the snake_body variable, so that it can be drawn onto the screen
        snake_body.pop()                        #deletes the last position of the snake (the tail)

        #food collision
        if pygame.Rect.colliderect(player.segment, fod.food_po):    #if the snake and food Rectangles/hitboxes collide with each other
            snake_body.append(new_food)
            new_food_que = [random.randrange(780), random.randrange(580)]
            for i in range(10):                                 #essentially a while True loop but if it fails 10 times just move on. In practice its very unlikely to run more than 3 times
                for pos in snake_body:                                  #checks if the new generated food position exists within the snakes body, if it does then it generates a new food queue. But if it does not, then it creates the new food position
                    if pygame.Rect.colliderect(pygame.Rect(pos,(player.size, player.size)), pygame.Rect(new_food_que, fod.size)):
                        new_food_que = [random.randrange(780), random.randrange(580)]
                        break
            new_food = new_food_que
                        
            score_count += 10                                       #increase the score count when the food is eaten

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
        #if the current position is less than 0, greater than width-snake size or height-snake size, then the loop stops and the gameover screen appears
        elif curr_pos[0] > WIDTH-20 or curr_pos[0] < 0 or curr_pos[1] > HEIGHT-20 or curr_pos[1] < 0:
            running = False
            game_s.gameover(screen, score_count)

        #collision with itself
        #makes the starting_pos None when the snake moves. This prevents a gameover from when the game starts and the snake is not moving
        #the direct variable is inital set to None, so when it does not equal None, the starting position changes from [100,50] to None
        if direct != None:  
            starting_pos = None

        #checks the snakes position, and if the position of the snakes body (hence why [1:]) equals the current position (essentially the head). 
        #Then the starting position is set to None (makes sure the game does not shutdown at startup), and displays the gameover screen
        for snake_pos in snake_body[1:]:
            if snake_pos[0] == curr_pos[0] and snake_pos[1] == curr_pos[1]:
                if starting_pos == None:
                    running = False
                    game_s.gameover(screen, score_count)

        #fill screen if the game_done variable is False (this prevents the screen from updating with the drawings while the gameover screen is also running)
        if game_done == False:
            screen.fill(WHITE)

            #draws food, score, and snake
            fod.food_draw(screen)

            score.draw_score(screen)

            player.draw(screen)

            #update screen
            pygame.display.flip()

        #refresh based on the speed (faster refresh rate for faster moving snake), but it should be high enough to avoid choppy looking movement
        clock.tick(speeds[settings["speed_index"]])

#menu settings
while True:
    settings = menu.show_menu(settings, apple_counts, speeds, screen, WIDTH, HEIGHT, clock)
    gameloop(settings)
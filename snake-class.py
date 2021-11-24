#import libraroes
import pygame, random

from pygame.constants import K_DOWN, K_RIGHT

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

#snake variables
snake_body = [[400,300]]
snake_direction = (0,0)
snake_length = 1

#snake class
class snake:
    def __init__(self, direction, length, colour, size, position):
        self.direction = direction 
        self.length = length
        self.colour = colour
        self.size = size
        self.position = position
    
    def draw(self, screen):
        for pos in self.position:
            pygame.draw.rect(screen, BLUE, (pos[0], pos[1], self.size, self.size))

#scoreboard class
class scoreboard:
    def __init__(self, font, size, score, colour, position):
        self.font = font
        self.size = size
        self.score = score
        self.colour = colour
        self.position = position
    
    def draw_score(self, screen):
        score_font = pygame.font.SysFont(self.font, self.size, True)
        text = score_font.render(f"Score: {self.score}", True, self.colour)
        screen.blit(text, self.position)

#food position
food_pos = [random.randrange(WIDTH-10), random.randrange(HEIGHT-10)]

class food:
    def __init__(self, colour, size, position):
        self.colour = colour
        self.size = size
        self.position = position

    def food_rect(self):
        return pygame.Rect(self.position,self.size)
    
    def food_draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.food_rect())

#food class variable
fod = food(RED,(20,20),food_pos)

#scoreboard class variable
score_count = 0
score = scoreboard("Ariel", 24, score_count, BLACK, (0,0))

#snake class variable
player = snake(snake_direction, snake_length, BLUE, 30, snake_body)

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

    for pos in snake_body:

        print(pos)
        print(food_pos)

        if food_pos[0] == pos[0] and food_pos[1] == pos[1]:
            print("hi")

    head = snake_body[0]
    tail = (head[0]+snake_direction[0], head[1]+snake_direction[1])
    snake_body.insert(0, tail)

    while len(snake_body) > snake_length:
        snake_body.pop()

    #update screen
    pygame.display.flip()

    #refresh 60 times a second
    clock.tick(FPS)

pygame.quit()
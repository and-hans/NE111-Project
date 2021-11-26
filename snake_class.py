#import libraroes
import pygame

BLUE = [0,0,255]

#snake variables
snake_body = [[100, 50], [900, 50], [80, 50]]
snake_direction = (0,0)
snake_length = 1
current_pos = None

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
            pygame.draw.rect(screen, BLUE, pygame.Rect(pos[0], pos[1], self.size, self.size))


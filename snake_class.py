import pygame

#snake variables
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = None
change_dir = None
direct = None
curr_pos = [snake_body[0][0], snake_body[0][1]]
starting_pos = [100, 50]
speed = 6
#snake class
class snake:

    def __init__(self, colour, size, position): 
        self.colour = colour
        self.size = size
        self.position = position
        self.segment = pygame.Rect((snake_body[0][0], snake_body[0][1]), (self.size, self.size))
    
    def draw(self, screen):
        for pos in self.position:
            self.segment = pygame.Rect(pos[0], pos[1], self.size, self.size)
            pygame.draw.rect(screen, self.colour, self.segment)


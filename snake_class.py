import pygame

#snake variables
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = (0,0)
change_dir = None
curr_pos = [100, 50]

#snake class
class snake:

    def __init__(self, direction, colour, size, position):
        self.direction = direction 
        self.colour = colour
        self.size = size
        self.position = position
        self.head = pygame.Rect(snake_body[0][0], snake_body[0][1], self.size, self.size)
    
    def draw(self, screen):
        for pos in self.position:
            segment = pygame.Rect(pos[0], pos[1], self.size, self.size)
            pygame.draw.rect(screen, self.colour, segment)


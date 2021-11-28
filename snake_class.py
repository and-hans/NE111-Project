import pygame

#snake class
class snake:

    def __init__(self, colour, size, position): 
        self.colour = colour
        self.size = size
        self.position = position
        self.segment = pygame.Rect((position[0][0], position[0][1]), (self.size, self.size))
    
    def draw(self, screen):
        for pos in self.position:
            self.segment = pygame.Rect(pos[0], pos[1], self.size, self.size)
            pygame.draw.rect(screen, self.colour, self.segment)


#import pygame library
import pygame

#snake class
class snake:

    #instances (variables that the class uses throughout)
    def __init__(self, colour, size, position): 
        self.colour = colour
        self.size = size
        self.position = position
        self.segment = pygame.Rect((position[0][0], position[0][1]), (self.size, self.size))
    
    #draw method, for drawing the snake onto the screen
    def draw(self, screen):
        #for each position in the position list given in self.position, create a Rectangle/hitbox, and draw it to the screen
        for pos in self.position:
            self.segment = pygame.Rect(pos[0], pos[1], self.size, self.size)    #updates the hitbox
            pygame.draw.rect(screen, self.colour, self.segment)


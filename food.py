import pygame, random

rnd_food = (random.randrange(790), random.randrange(590))

class food:

    def __init__(self, colour, size, position):
        self.colour = colour
        self.size = size
        self.position = position
        self.food_po = pygame.Rect(self.position,self.size)
    
    def food_draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.food_po)
    

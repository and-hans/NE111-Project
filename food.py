import pygame, random

#food position
food_pos = (random.randrange(790), random.randrange(590))

class food:
    def __init__(self, colour, size, position):
        self.colour = colour
        self.size = size
        self.position = position

    def food_rect(self):
        return pygame.Rect(self.position,self.size)
    
    def food_draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.food_rect())


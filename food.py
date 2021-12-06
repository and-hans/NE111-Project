#This Module was made by Andrew Hanraj

#imports pygame and random libraries 
import pygame, random

#Food position variables. Generates random positions within the range given. 
# Range is determined by the size of the screens width (800) or height (600), subtracted by the food size  (20)
new_food = [random.randrange(780), random.randrange(580)]

#food class
class food:
    #instances/initial variables that are needed to run the class, and that can be accessed throughout the class
    def __init__(self, colour, size, position):
        self.colour = colour    #food coolour
        self.size = [size,size] #food size
        self.position = position    #food starting position
        self.food_po = pygame.Rect(self.position,self.size) #foods rectangle/hitbox
    
    #draws the food onto the screen
    def food_draw(self, screen):
        #pygame function to draw images on the screen. Gets the screen it needs to put the image on, the colour of the food (already defined above), and the rectangle (position and size)
        pygame.draw.rect(screen, self.colour, self.food_po)

    
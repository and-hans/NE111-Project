#import pygame library
import pygame


#scoreboard class
class scoreboard:

    #instances 
    def __init__(self, font, size, score, colour, position):
        self.font = font
        self.size = size
        self.score = score
        self.colour = colour
        self.position = position
    
    #drawing the scoreboard to the screen
    def draw_score(self, screen):
        #makes the scoreboards font
        score_font = pygame.font.SysFont(self.font, self.size, True)
        #makes the scoreboard text and updates with the given score variable
        text = score_font.render(f"Score: {self.score}", True, self.colour)
        #draws the text to the screen on the position that was given 
        screen.blit(text, self.position)


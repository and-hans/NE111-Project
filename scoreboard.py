import pygame


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


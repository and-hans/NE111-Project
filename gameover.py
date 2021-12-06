#This Module was made by Andrew Hanraj


#import pygame,and path (from os library) libraries
import pygame
from os import path

#high score document file name
HS = "score.txt"

#game change class
class gamechange:

    #instances
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.highscore()

    #highscore method
    def highscore(self):
        self.dir = path.dirname(__file__)   #finds the current directory location
        with open(path.join(self.dir, HS), 'r') as f:   #opens the file in read mode, and sets it the the f variable
            try:
                #updates high score with what is given in the document (turns the string into an integer for later use)
                self.highscore = int(f.read())
            except:
                #if there is nothing, then sets the high score to 0
                self.highscore = 0

    #gameover method
    def gameover(self, screen, score):
        #font used throughoutmethod
        game_over_font = pygame.font.SysFont('Times New Roman', 30)

        #creates the text variable 
        game_over_text = game_over_font.render(f"Score", True, (255,0,0))
        gameover_score = game_over_font.render(f"{score}", True, (255,0,0))
        continue_text = game_over_font.render('Press any key to continue', True, (255,0,0))
        
        #if the score given in the method is higher than the current high score, updates the new high score and writes it to the document
        #if the score is less than the highscore, then it simply displays the "Score" instead of "High Score"
        #if the score is equal to high score, then it's considered as the high score too
        if score > self.highscore:
            self.highscore = score
            high_score_text = game_over_font.render(f'New High Score: {self.highscore}', True, (255,0,0))
            with open(path.join(self.dir, "score.txt"), 'w') as f:
                f.write(str(score))
        elif score < self.highscore:
            high_score_text = game_over_font.render(f'High Score: {self.highscore}', True, (255,0,0))
        else:
            high_score_text = game_over_font.render(f'New High Score: {self.highscore}', True, (255,0,0))
        
        #positions of where the text should be displayed
        #.get_rect is used to find the middle of the rectangle created, so that the text is centered 
        middle = game_over_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2-100))
        middle_mid = gameover_score.get_rect(center=(self.WIDTH/2, self.HEIGHT/2-50))
        middle_low = high_score_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        middle_bot = ((self.WIDTH/4)+50, (self.HEIGHT/2.5)+300)

        #fill the screen, to in make it seem like a new screen
        screen.fill((255,255,255))

        #draw the text to the given position
        screen.blit(game_over_text, middle)
        screen.blit(gameover_score, middle_mid)
        screen.blit(high_score_text, middle_low)
        screen.blit(continue_text, middle_bot)

        #updates display
        pygame.display.flip()

        #checks if quit was selected and quits the program. Or if a key was pressed, to return to the title screen
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #return to game loop if a key is pressed
                if event.type == pygame.KEYDOWN:
                    #ignore arrow keys though, so no instant exiting from game-over screen
                    if not (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                        return

        



import pygame, time
from os import path

HS = "score.txt"

class gamechange:

    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.highscore()

    def highscore(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def gameover(self, screen, score):
        game_over_font = pygame.font.SysFont('Times New Roman', 30)
        game_over_text = game_over_font.render(f"Score", True, (255,0,0))
        gameover_score = game_over_font.render(f"{score}", True, (255,0,0))
        middle = (self.WIDTH/2.5+20, self.HEIGHT/2.5)
        middle_mid = ((self.WIDTH/2.5)+50, (self.HEIGHT/2.5)+50)

        if score > self.highscore:
            self.highscore = score
            high_score_text = game_over_font.render(f'New High Score: {self.highscore}', True, (255,0,0))
            with open(path.join(self.dir, "score.txt"), 'w') as f:
                f.write(str(score))
        elif score < self.highscore:
            high_score_text = game_over_font.render(f'High Score: {self.highscore}', True, (255,0,0))
        else:
            high_score_text = game_over_font.render(f'New High Score: {self.highscore}', True, (255,0,0))
        
        middle_low = ((self.WIDTH/4)+100, (self.HEIGHT/2.5)+200)


        continue_text = game_over_font.render('Press any key to continue', True, (255,0,0))
        middle_bot = ((self.WIDTH/4)+50, (self.HEIGHT/2.5)+300)


        screen.fill((255,255,255))

        screen.blit(game_over_text, middle)
        screen.blit(gameover_score, middle_mid)
        screen.blit(high_score_text, middle_low)
        screen.blit(continue_text ,middle_bot)

        pygame.display.flip()

        time.sleep(0.5)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    return

        



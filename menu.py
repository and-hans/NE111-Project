import pygame, sys
from pygame.locals import *

#define some colours
WHITE = (255, 255, 255)
GREY = (155, 155, 155)
LIGHTGREY = (200, 200, 200)
DARKGREEN = (  0, 155,   0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKRED =(155, 0 ,0)

#background colour is black
BGCOLOR = (  0,   0,   0)

#somewhat arbitrary fps for menu, just keep it higher than 10
FPS = 15


# potentially to be added to Button:
#   option for bounding box graphic
#   options for image instead of text
class Button():
    def __init__(self, pos:(int,int), x_width:int, y_height:int, font:pygame.font.Font, text:str, color = WHITE, hover_color = GREY): 
        """ position tuple, x_width, y_height,pygame font, text (string) """ 
        self.font = font
        self.text = text
        self.pos = pos
        #initialize the bounds as the pos +- half the span of the button in that dimension
        self.bounds = ( (pos[0]-x_width/2, pos[0]+x_width/2), (pos[1]-y_height/2, pos[1]+y_height/2) )
        self.color = color
        self.render_color = color;
        self.hover_color = hover_color

    
    def mouseOver(self, mouse:(int,int), mousedown:bool):
        #check if the mouse is in the rectangle defined by the pos, width, and height by comparing each dimension of mouse position to bounds
        over = (self.bounds[0][0] <= mouse[0] <= self.bounds[0][1] and self.bounds[1][0] <= mouse[1] <= self.bounds[1][1])

        #if mouse is hovering over, change colour to hover_color, if mouse is down and hovering, change to mousedown_colour
        self.render_color =  self.hover_color if over else self.color

        #return true if the button was clicked
        return over and mousedown

    #put all the stuff required to create a text element then display it in one place
    def render(self, screen:pygame.Surface):
        txt = self.font.render(self.text, True, self.render_color)
        rect = txt.get_rect()
        rect.center = self.pos
        screen.blit(txt, rect)



def show_menu(settings:dict, apple_counts:list, speeds:list, display:pygame.Surface, window_width, window_height, clock):
    """takes as input settings dict, lists containing options for the settings, display object, screen dimensions, and clock. Returns changed settings dict based on user inputs on menu screen """
    #define fonts
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    menuFont = pygame.font.Font('freesansbold.ttf', 30)

    #define static text
    titleSurf1 = titleFont.render('Snake!', True, WHITE, DARKGREEN)
    rect1 = titleSurf1.get_rect()
    rect1.center = (window_width / 2, 60)

    speed_heading = menuFont.render("Speed:", True, WHITE)
    rect3 = speed_heading.get_rect()
    rect3.center = (window_width / 2, 140)

    #define buttons

    speed_buttons = []
    for i in range(0, len(speeds)):
        speed_buttons.append(Button((window_width / 2, 190+40*i), 50, 30,menuFont, str(i+1)+"cc"))

    infinite_mode = Button((window_width / 2, window_height-200), 200, 30, menuFont, "infinite_mode")

    #default to green and red, change to dark green and dark red when hovered over respectively
    start_button = Button((window_width / 2, window_height-60),70,45,menuFont, "Start", GREEN, DARKGREEN)
    exit_button = Button((window_width / 2, window_height-20),70,15,menuFont, "Quit", RED, DARKRED)


    while True:
        click = False
        for ev in pygame.event.get():
          
            if ev.type == pygame.QUIT:
                terminate()
             
            #if the mouse was clicked, set click variable true
            if ev.type == pygame.MOUSEBUTTONDOWN:
                click = True

        #get mouse pos (pixel space)
        mouse = pygame.mouse.get_pos()


        #check for press on speed button
        for i in range(len(speeds)):
            if speed_buttons[i].mouseOver(mouse, click):
                settings["speed_index"] = i

        if infinite_mode.mouseOver(mouse, click):
            #toggle binary option
            settings["infinite_mode"]=not settings["infinite_mode"]
                        
        #check for start button
        if start_button.mouseOver(mouse, click):
            return settings

        if exit_button.mouseOver(mouse, click):
            terminate()
                 
        #clear window
        display.fill(BGCOLOR)

        #render static text
        display.blit(titleSurf1, rect1)

        display.blit(speed_heading, rect3)

        start_button.render(display)

        exit_button.render(display)

        #display options for the settings
        #speeds with pointer for selected option
        for i in range(len(speeds)):
            speed_buttons[i].render(display)

            if settings["speed_index"]==i:
                txt = menuFont.render(">", True, WHITE)
                rect = txt.get_rect()
                rect.center =  (speed_buttons[i].pos[0]-50, speed_buttons[i].pos[1])
                display.blit(txt, rect)

        infinite_mode.render(display)

        #indicate whether infinite mode is on
        txt_inf = menuFont.render("ON" if settings["infinite_mode"] else "OFF", True, WHITE)
        rect_inf = txt.get_rect()
        rect_inf.center = (infinite_mode.pos[0]-200, infinite_mode.pos[1])
        display.blit(txt_inf, rect_inf)
        

        pygame.display.update()

        clock.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()

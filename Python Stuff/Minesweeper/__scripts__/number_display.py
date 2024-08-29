import pygame
from __scripts__.settings import *




class Display():
    def __init__(self, x, y, w, h, skin):
        
        # Loaciton
        self.x = x
        self.y = y

        # Size
        self.width = w
        self.height = h
        self.bg_color = SKINS[skin][4][0]
        self.border_col = SKINS[skin][4][2]
        self.border_rad = 5

        self.border_len = 2

        # Text variables
        self.font = "bahnschrift"

        self.text = "Test"
        self.font_size = 36
        self.font_color = SKINS[skin][4][1]

        # Making the text and getting it's size
        self.myfont = pygame.font.SysFont(self.font, self.font_size)


    def draw(self, screen, text):

        # Draw the background
        pygame.draw.rect(screen, self.border_col, (self.x-self.border_len, self.y-self.border_len, self.width+self.border_len*2, self.height+self.border_len*2), border_radius=self.border_rad)
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height), border_radius=self.border_rad)

        self.text = text
        self.make_text(screen)

        



    def make_text(self, screen):

        # Makes the text element
        self.text_element = self.myfont.render(self.text, 1, (self.font_color))
        self.text_width, self.text_height = self.text_element.get_width(), self.text_element.get_height()

        if self.text_width >= self.width:
            self.width += 50
            self.x -= 50
        
        #screen.blit(self.text_element, (self.x+self.width-self.text_width-5, self.y+self.height/2-self.text_height/2, self.width, self.height))
        screen.blit(self.text_element, (self.x+self.width/2-self.text_width/2+2, self.y+self.height/2-self.text_height/2+2, self.width, self.height))




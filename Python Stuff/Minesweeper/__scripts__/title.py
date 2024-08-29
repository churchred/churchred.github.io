


# Import pygame reletated things
import pygame

# Import other python scripts
from __scripts__.settings import *  
from __scripts__.button_class import Button 


class Title():
  def __init__(self, skin_index):

    # Which skin we are using
    self.skin_index = skin_index

    # Load background image
    self.logo_size = [248*1.2, 55]
    self.logo_image = pygame.image.load("assets/logo.png").convert_alpha()
    self.logo_image = pygame.transform.scale(self.logo_image, (self.logo_size[0], self.logo_size[1])) 
    self.img_center = (TITLE_WIDTH/2-self.logo_size[0]/2, 25)


    self.btn_width = 200
    self.btn_height = 50
    self.button_x = TITLE_WIDTH/2-self.btn_width/2

    self.reset()


  def reset(self):
    self.easy_btn = Button(
        self.button_x, 100+60*0, self.btn_width, self.btn_height,     # x, y, w, h, 
        0, 4, BLACK, False,                                           # border_radius, border_width, border_color, will_border_hover,
        SKINS[self.skin_index][2][0], SKINS[self.skin_index][2][1],   # color, hover_color, 
        "Arial", 28, BLACK, WHITE,                                    # font, font_size, font_color, font_color_hover
        "Beginner", ["Beginner"], "", SKINS[self.skin_index][1]       # name, id, special, Which skin
      )
    

    self.medium_btn = Button(
        self.button_x,  100+60*1, self.btn_width, self.btn_height,        # x, y, w, h, 
        0, 4, BLACK, False,                                               # border_radius, border_width, border_color, will_border_hover,
        SKINS[self.skin_index][2][0], SKINS[self.skin_index][2][1],       # color, hover_color, 
        "Arial", 28, BLACK, WHITE,                                        # font, font_size, font_color, font_color_hover
        "Intermidiate", ["Intermidiate"], "", SKINS[self.skin_index][1]   # name, id, special, Which skin
      )
  

    self.hard_btn = Button(
        self.button_x,  100+60*2, self.btn_width, self.btn_height,    # x, y, w, h, 
        0, 4, BLACK, False,                                           # border_radius, border_width, border_color, will_border_hover,
        SKINS[self.skin_index][2][0], SKINS[self.skin_index][2][1],   # color, hover_color, 
        "Arial", 28, BLACK, WHITE,                                    # font, font_size, font_color, font_color_hover
        "Expert", ["Expert"], "", SKINS[self.skin_index][1]           # name, id, special, Which skin
      )
    
    self.skins_btn = Button(
        self.button_x,  100+60*3, self.btn_width, self.btn_height,    # x, y, w, h, 
        0, 4, BLACK, False,                                           # border_radius, border_width, border_color, will_border_hover,
        SKINS[self.skin_index][2][0], SKINS[self.skin_index][2][1],   # color, hover_color, 
        "Arial", 28, BLACK, WHITE,                                    # font, font_size, font_color, font_color_hover
        "Skin: "+SKINS[self.skin_index][0], ["Skins"], "", SKINS[self.skin_index][2][0]             # name, id, special, Which skin
      )
    
    self.btn_list = [self.easy_btn, self.medium_btn, self.hard_btn, self.skins_btn]

  # Runs the app
  def draw(self, screen, mouse):
    
    # Information to send back to main app
    package_to_main = [False, ""]

    screen.blit(self.logo_image, self.img_center)

    for item in self.btn_list:
      package = item.draw(screen, mouse)
      if package[0] == True:
        package_to_main[0] = True
      if package[1] != None:
        package_to_main[1] = package[1]


    return package_to_main

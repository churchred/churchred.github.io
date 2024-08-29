import pygame
from __scripts__.settings import *

#self.button = Button(
#  10, 10, 140, 50,               # x, y, w, h, 
#  5, 2, WHITE, False,            # border_radius, border_width, border_color, will_border_hover,
#  ITEM_COLOR, ITEM_HOVER_COLOR,  # color, hover_color, 
#  FONT, 25, WHITE, WHITE,        # font, font_size, font_color, font_color_hover
#  "A Button", ["Hello"], ""      # name, id, special
#)


class Button():
  def __init__(self, x, y, w, h, 
               border_radius, border_width, border_color, will_border_hover,
               color, hover_color,
               font, font_size, font_color, font_color_hover,
               name, id, special, img):


    # Important info
    self.name = name                 # Text to show on button  
    self.id = id                     # Info that is sent back when clicked
    self.type = "Button"             # What is this? Its a "Button"
    self.special_features = special  # Do we need any special features, which ones?

    # Size of button elements
    self.width = w
    self.height = h
    self.sink = 0
    self.max_sink = 1             # How far down the button sinks when clicked
    self.cut_off_width_top = 0    # How much of the button top we CANT click on 
    self.cut_off_width_bottom = 0 # How much of the button buttom we CANT click on

    # Coordinates
    self.x = x
    self.y = y
    self.scroll_index_y = 0 # How far has it scrolled in Y-direction
    self.scroll_index_x = 0 # How far has it scrolled in X-direction


    # Colors of button elements
    self.color = color
    self.hover_col = hover_color
    self.border_col = border_color
    self.border_radius = border_radius
    self.border_width = border_width
    self.will_border_hover = will_border_hover
    self.color_backup = [color, border_color, hover_color]


    # Text variabels
    self.font = font
    self.font_size = font_size
    self.font_color = font_color
    self.font_color_hover = font_color_hover
    

    # Makes the text
    self.make_text()

    # Activation checks
    self.test_hover = False
    self.test_click = False

    if self.special_features == "Image":
      self.image = pygame.image.load(img + "reset.png").convert_alpha()
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
  
  
  def draw(self, screen, mouse):
    
    # Information sent back to main app
    # Do we hover the button, have we clicked the button
    packet = [False, None]

    # Checks if the cursor goes within the button 
    # AND is not already clicked; Hover test is then True
    if self.check_cursor(mouse) == True:

      # If the mouse is NOT clicked when we begin hovering
      if mouse[1][0] == False:
        self.test_hover = True
        packet[0] = True

    else:
      # Reset tests
      self.test_hover = False
      self.test_click = False


    # If we are within the button and click the mouse
    # Click test is now true
    if self.test_hover == True and mouse[1][0] == True:
      self.test_click = True

    # Adds a "sinking" effect when button is clicked
    if self.test_click == True:
      self.sink = self.max_sink
    else:
      self.sink = 0


    # Once we are within a button and release AFTER having clicked
    # we run the logic and reset the tests
    if self.test_click == True and mouse[1][0] == False:
      self.test_hover = False
      self.test_click = False
      packet[1] = self.id[0]

    # Draw the button
    if self.test_hover == False:
      self.draw_rect(screen, self.color, self.border_col)
    else:
      self.draw_rect(screen, self.hover_col, self.border_col)
      
    # Prints the text ontop of the button
    self.text(screen)

    if self.special_features == "Image":
      screen.blit(self.image, (self.x, self.y+self.sink))

    return packet


  def check_cursor(self, mouse):
    if mouse[0][0] > self.x+self.scroll_index_x and mouse[0][0] < self.x+self.scroll_index_x + self.width:
      if mouse[0][1] > self.y+self.scroll_index_y+self.cut_off_width_top and mouse[0][1] < self.y+self.height+self.scroll_index_y-self.cut_off_width_bottom:
        return True

  def text(self, screen):
    if self.test_hover == True:
      screen.blit(self.text_element_hover, (self.x+self.scroll_index_x+self.width/2-self.text_width/2, self.sink+self.y+self.scroll_index_y+(self.height/2)-(self.text_height)/2))
    else:
      screen.blit(self.text_element, (self.x+self.scroll_index_x+self.width/2-self.text_width/2, self.sink+self.y+self.scroll_index_y+(self.height/2)-(self.text_height)/2))

  def draw_rect(self, screen, color, bord_col):
    pygame.draw.rect(screen, bord_col, (self.x+self.scroll_index_x, self.y+self.sink+self.scroll_index_y, 
                                          self.width, self.height), border_radius=self.border_radius)

    pygame.draw.rect(screen, color, (self.x+self.scroll_index_x+self.border_width, self.y+self.border_width+self.sink+self.scroll_index_y, 
																				self.width-self.border_width*2, self.height-self.border_width*2), border_radius=self.border_radius)
  
  def make_text(self):

    # Making the text and getting it's size
    self.myfont = pygame.font.SysFont(self.font, self.font_size)
    
    # Makes the text element
    self.text_element = self.myfont.render(self.name, 1, (self.font_color))
    self.text_element_hover = self.myfont.render(self.name, 1, (self.font_color_hover))
    self.text_width, self.text_height = self.text_element.get_width(), self.text_element.get_height()
    self.text_centered = (self.x + self.scroll_index_x + (self.width)/2 - self.text_width/2, 
                          self.y + self.sink + self.scroll_index_y + (self.height/2)-(self.text_height)/2)
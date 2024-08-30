import pygame
from __scripts__.settings import *



class Tiles():
  def __init__(self, x, y, w, h, 
               color,
               font, font_size, font_color, font_color_hover,
               id, index, images, skin
               ):

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
    self.image_list = images
    self.skin_index = skin
    self.safe_click = False

    # Load Tile image
    self.tile_image = self.image_list[0]

    # Load Bomb image
    self.bomb_image = self.image_list[1]

    # Load Tile image
    self.flag_image = self.image_list[2]

    self.safe_img = self.image_list[3]
  

    # Text variabels
    self.font = font
    self.font_size = font_size
    self.font_color = font_color
    self.font_color_hover = font_color_hover

    # Game variables:
    self.flagged = False  # Is it flagged and now unclickable?
    self.hidden = True    # Has this button been clicked? 
    self.id = id          # Text on the button
    self.index = index    # Row/colum number of button

    # Activation checks
    self.test_hover = False
    self.test_click = [False, False]

    # Makes the text
    self.make_text()

    
  
  # Runs the button logic
  def draw(self, screen, mouse, gameover):
    
    
    # Information sent back to main app
    # Do we hover the button, have we clicked the button, right/left mouse button
    packet = [False, None, None]

    # Checks if the cursor goes within the button 
    # AND is not already clicked; Hover test is then True
    if self.check_cursor(mouse) == True and self.hidden == True and gameover == False:
      
      packet[0] = True

      # If the mouse is NOT clicked when we begin hovering
      if mouse[1][0] == False:
        self.test_hover = True

    else:
      # Reset tests
      self.test_hover = False
      self.test_click = [False, False]


    # If we are within the button and left-click the mouse
    # Click test is now true
    if self.test_hover == True and mouse[1][0] == True:
      self.test_click[0] = True

    # If we are within the button and right-click the mouse
    # Click test is now true
    if self.test_hover == True and mouse[1][2] == True:
      self.test_click[1] = True

    # Adds a "sinking" effect when button is clicked
    if self.test_click[0] == True:
      self.sink = self.max_sink
    else:
      self.sink = 0


    # Once we are within a button and release AFTER having clicked
    # we run the logic and reset the tests
    if self.test_click[0] == True and mouse[1][0] == False:
      self.test_hover = False
      self.test_click[0] = False
      packet[1] = self.id
      packet[2] = "Left"

    # Once we are within a button and release AFTER having clicked
    # we run the logic and reset the tests
    if self.test_click[1] == True and mouse[1][2] == False:
      self.test_hover = False
      self.test_click[1] = False
      packet[1] = self.id
      packet[2] = "Right"
      

    # Draw the Tile
    if self.hidden == False:

      # Draw clicked tile
      self.draw_rect(screen, self.color)

      # If the tile has a bomb, draw bomb
      if self.id == "X":
        self.draw_bomb(screen)
      else:
        # Write the number on the tile if it has one
        self.text(screen)

    else:
      # Draw the unclicked button
      screen.blit(self.tile_image, (self.x, self.y+self.sink))
      if self.safe_click == True and self.hidden == True:
        screen.blit(self.safe_img, (self.x, self.y))

      # Draw the flag if button is flagged
      if self.flagged == True:
        self.draw_flag(screen)

    return packet

  # Checks if mouse cursor is within the button
  def check_cursor(self, mouse):
    if mouse[0][0] > self.x+self.scroll_index_x and mouse[0][0] < self.x+self.scroll_index_x + self.width:
      if mouse[0][1] > self.y+self.scroll_index_y+self.cut_off_width_top and mouse[0][1] < self.y+self.height+self.scroll_index_y-self.cut_off_width_bottom:
        return True

  # Prints the text onto the screen
  def text(self, screen):
    if self.test_hover == True:
      screen.blit(self.text_element_hover, (self.x+self.scroll_index_x+self.width/2-self.text_width/2, self.sink+self.y+self.scroll_index_y+(self.height/2)-(self.text_height)/2))
    else:
      screen.blit(self.text_element, (self.x+self.scroll_index_x+self.width/2-self.text_width/2, self.sink+self.y+self.scroll_index_y+(self.height/2)-(self.text_height)/2))

  # Draws the button onto the screen
  def draw_rect(self, screen, color):
    pygame.draw.rect(screen, color, (self.x+self.scroll_index_x, self.y+self.sink+self.scroll_index_y, 
                                          self.width, self.height))

  # Draws the bomb ontop of the Tile if clicked or revealed
  def draw_bomb(self, screen):

    # Draw the bomb
    screen.blit(self.bomb_image, (self.x, self.y+self.sink))

  # Draws the flag onto the button if it is flagged
  def draw_flag(self, screen):
    screen.blit(self.flag_image, (self.x, self.y+self.sink))

  # Creates the text variables
  def make_text(self):

    # Making the text and getting it's size
    self.myfont = pygame.font.SysFont(self.font, self.font_size, bold=True)
    
    # Makes the text element
    self.text_element = self.myfont.render(self.id, 1, (self.font_color))
    self.text_element_hover = self.myfont.render(self.id, 1, (self.font_color_hover))
    self.text_width, self.text_height = self.text_element.get_width(), self.text_element.get_height()
    self.text_centered = (self.x + self.scroll_index_x + (self.width)/2 - self.text_width/2, 
                          self.y + self.sink + self.scroll_index_y + (self.height/2)-(self.text_height)/2)
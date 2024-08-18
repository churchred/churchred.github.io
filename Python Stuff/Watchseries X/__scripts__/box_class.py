import pygame
import math
from __scripts__.settings import *
from __scripts__.general import *
from __scripts__.scrolling import Scroll



class Box():
  def __init__(self,
        x, y, w, h, border_radius, background_color,
        colums, space_row, space_col, max_rows,
        item_list, 
        centered_vertical, centered_horizon,
        title_scroll, title, 
        font, font_size, font_color, text_x, text_y,
        scrollbar_possible,
        special, current_series=[]
               ):
    
    # Basic variables from settings.py
    self.x = x
    self.y = y
    self.width = w
    self.height = h
    self.effective_height = h 
    self.border_radius = border_radius

    # How many rows and colums we have, and a list with buttons to fill them.
    self.colums = colums
    self.space_between_row = space_row
    self.space_between_col = space_col
    self.item_list = item_list
    self.rows = int(math.ceil(len(self.item_list) / self.colums))
    self.max_rows = max_rows

    # Wether or not things are centered x and y.
    self.centered_vertical = centered_vertical
    self.centered_horizon = centered_horizon

    # Color of box
    self.background_color = background_color

    # Title
    self.title_scrollable = title_scroll
    self.title = title
    self.curr_series = current_series

    # Text stuff
    self.font = font
    self.font_size = font_size
    self.font_color = font_color

    #Title coordinates
    self.text_x = text_x
    self.text_y = text_y
    self.scroll_index_y = 0
    self.txt_h = 0

    # Keeps track of last places x,y of buttons. Used in Change episode to write "Season X"
    self.last_coordinates = [0, 0]

    # Do we need to do anything special? Usually no, which is False
    self.special_feature = special
    self.type = "box"

    # Scrollbar
    self.has_scrollbar = scrollbar_possible
    self.scrollbar_activated = False
    self.mouse_scrolled = False

    # If scrollbar is enabled
    if self.has_scrollbar == True:
 
      # Do we need a scrollbar right now? Change episode does this in Center def
      if self.special_feature != "Change":
        self.check_if_scrollbar_needed()

    # Makes the text if we have any to make
    if self.title != "" and self.special_feature != "title":
      self.make_text()
    if self.special_feature == "title":
      self.make_title_texts(self.curr_series)


  def center(self, curr_series):
    
    # Sets x, y for all things in the change-card
    if self.special_feature == "Change":
      
      # Get x-posisition for each colum in a row
      pos_x = get_equadistant_positions([[self.width-70, self.x], 40, CHANGE_EP_COLUMS])
      row_count = 0
      count_x = 0
      for index, element in enumerate(self.item_list):
        
        if isinstance(element, str) == True:
          row_count += 1
          count_x = 0
        else:

          if element.name == "1" and index != 1:
            count_x = 0
            row_count += 1
          if count_x == CHANGE_EP_COLUMS:
            row_count += 1
            count_x = 0

          element.x = pos_x[count_x] + 15
          element.y = self.y + 35 + (50*row_count)

          count_x += 1
    

      self.rows = row_count+1
      self.effective_height = self.height - 35

      # Do we need a scrollbar right now?
      self.check_if_scrollbar_needed()

      self.special_feature = "change_post"

    # Sets x, y for all things in the bookmarks-card
    if self.special_feature == "Bookmarks":
      row_count = 0
      for element in self.item_list:
        if element.id[0] == curr_series[0][0]:
          element.x = self.x + 30
          element.y = self.y + 60 + (element.height+10)*row_count
          row_count +=1
      self.rows = row_count+1
      self.effective_height = self.height - 60

      # Do we need a scrollbar right now?
      if self.scrollbar_activated == False:
        self.check_if_scrollbar_needed()

    # If we need to center the objects, it happens here.
    if self.centered_horizon == True and len(self.item_list) > 0:
      if self.special_feature != "banner":
        self.positions_horizon = get_equadistant_positions([[self.width, self.x], self.item_list[0].width, self.colums])
        count = 0
        for index, element in enumerate(self.item_list):
          element.x = self.positions_horizon[count]
          count += 1
          if count == self.colums:
            count = 0
      else:
        temp_list = [[self.width, self.x]]
        for i in self.item_list:
          temp_list.append(i.width)
        self.positions_horizon = get_equadistant_positisjon_set_number_of_elements(temp_list)
        for index, element in enumerate(self.item_list):
          element.x = self.positions_horizon[index]
      self.centered_horizon = False

    if self.centered_vertical == True and len(self.item_list) > 0:
      if self.special_feature != "card":
        self.positions_vertical = get_equadistant_positions([[self.height, self.y], self.item_list[0].height, self.rows])
        count_x = 0
        count_y = 0
        for index, element in enumerate(self.item_list):
          
          element.y = self.positions_vertical[count_y]
          count_x += 1
          if count_x == self.colums:
            count_y += 1
            count_x = 0
      else:
        temp_list = [[self.height, self.y]]
        for i in self.item_list:
          temp_list.append(i.height)
        self.positions_horizon = get_equadistant_positisjon_set_number_of_elements(temp_list)
        for index, element in enumerate(self.item_list):
          element.y = self.positions_horizon[index]

      self.centered_vertical = False
    

  def draw(self, screen, mouse, dt, current_series, scroll):

    self.center(current_series)

    # This is to keep track of hovering anything 
    # and need to change cursor, and if we clicked anything
    packet = [False, ""]

    # Making the card on which to place the buttons
    pygame.draw.rect(screen, self.background_color, (self.x, self.y, self.width, self.height), border_radius=self.border_radius)  



    if self.has_scrollbar == True and self.scrollbar_activated == True:
      # Runs the scrollbar logic if we have one
      packet[0] = self.scrollbar_logic(screen, mouse)


    # This loop is where we draw every button and handle the logic
    for index, element in enumerate(self.item_list):
      
      # Makes it so we dont create bookmarks for another series than current
      if self.special_feature == "Bookmarks" and element.id[0] != current_series[0][0]:
        pass

      else:

        # If string
        if isinstance(element, str):
          # If we can scroll and are holding the bar, or if we have just activated the bar
          if (self.scrollbar_activated == True and self.scrollbar.active == True) or (self.mouse_scrolled == True and self.scrollbar_activated == True):
            self.scroll_index_y = self.scrollbar.calculate_move_distance(50, self.effective_height)
            

          self.text_element_season = self.myfont_season.render(element, 1, (self.font_color))
          screen.blit(self.text_element_season, (self.text_x+10, self.item_list[index+1].y+self.scroll_index_y-35))

        # Things we do only to a button element
        elif element.type == "Button":

          self.last_coordinates = [element.x, element.y]

          # If we can scroll and are holding the bar, or if we have just activated the bar
          if (self.scrollbar_activated == True and self.scrollbar.active == True) or (element.scroll_index_x == 0 and self.scrollbar_activated == True) or (self.mouse_scrolled == True and self.scrollbar_activated == True):
            element.scroll_index_y = self.scrollbar.calculate_move_distance(element.height+10, self.effective_height)
            element.scroll_index_x = -10
            self.scroll_index_y = element.scroll_index_y
            
          # Check if the button is within the box
          if within_bounds([self.x, self.y, self.width, self.height], element) == True:

            # Check if there are parts outside the box
            element.cut_off_width_top, element.cut_off_width_bottom = check_partial_overlap([self.x, self.y, self.width, self.height], element)


            # Checks if button is current button or not
            if self.special_feature == "change_post":
              if element.id == current_series[1]:
                element.disabled = True
                element.check_disabled(2)
              else:
                if element.disabled == True:
                  element.disabled = False
                  element.check_disabled(2)

            # Checks if button is current button or not
            if self.special_feature == "series":
              if element.id[0] == current_series[1][0]:
                element.disabled = True
                element.check_disabled(1)
              else:
                if element.disabled == True:
                  element.disabled = False
                  element.check_disabled(1)

            if self.special_feature == "Bookmarks":
              if element.id == current_series[1]:
                element.disabled = True
                element.check_disabled(2)
              else:
                if element.disabled == True:
                  element.disabled = False
                  element.check_disabled(2)

            # Draw the button 
            info_from_button = element.draw(screen, mouse) 

            # Checks if we hover the button
            if element.check_cursor(mouse) == True:
              packet[0] = True
          
            if info_from_button != "":
              packet[1] = info_from_button

        elif element.type == "box":
          packet_temp = element.draw(screen, mouse, dt, current_series, scroll)
          if packet_temp[0] == True:
            packet = packet_temp

        elif element.type == "loadbar":
          element.draw(screen, dt)


    if self.title != "":
      self.text(screen)
    if self.special_feature == "title":
      self.text_title(screen)

    self.mouse_scrolled = False

    return packet
  



  # Do we need a scrollbar?
  def check_if_scrollbar_needed(self):

    # We make the scrollbar we use when we have many series buttons (w, h, x, y)
    self.scrollbar = Scroll(10, self.height-20, self.x+self.width-15, self.y+10)
    if self.special_feature == "Bookmarks" or self.special_feature == "Change":
      self.scrollbar = Scroll(20, self.height-20, self.x+self.width-35, self.y+10)

    if self.rows > self.max_rows:
      self.scrollbar_activated = True                   # Sets scrollbar to True for Left side menu 
      self.scrollbar.rows = (self.rows)                 # How many button we have is used to calculate the height of all the buttons later
      self.scrollbar.calculate_size(50, self.effective_height) # Calculates the size of the draggable item within the scrollbar. 
                                                        # (Size of a button(with spaces), effective screen size)

  # Make the text elements if we have them
  def make_text(self):

    # Making the text and getting it's size
    self.myfont = pygame.font.SysFont(self.font, self.font_size)

    # For the change series tab
    self.myfont_season = pygame.font.SysFont(self.font, SEASON_FONT_SIZE)
    
    # Makes the text element
    self.text_element = self.myfont.render(self.title, 1, (self.font_color))
    self.text_width, self.text_height = self.text_element.get_width(), self.text_element.get_height()
    self.txt_h = self.text_height+30

  # Print the text elements if we have them
  def text(self, screen):
    if self.title_scrollable == True:
      screen.blit(self.text_element, (self.text_x, self.text_y+self.scroll_index_y))
      pygame.draw.rect(screen, self.font_color, (self.text_x+2, self.text_y+self.scroll_index_y+self.text_height-5, 
                                          self.text_width-4, 1))
    else:
      screen.blit(self.text_element, (self.text_x, self.text_y))
      pygame.draw.rect(screen, self.font_color, (self.text_x+2, self.text_y+self.text_height-5, 
                                          self.text_width-4, 1))

  # Make title texts, only for title-cards
  def make_title_texts(self, series):

    name = series[0]

    # Making the title and getting it's size
    self.myfont = pygame.font.SysFont(self.font, TITLE_FONTS[0])
    if len(name) > 30:
      name = name[:27] + "..."
      

    self.text_element = self.myfont.render(name, 1, (self.font_color))
    
    # Making the current episode text
    self.myfont2 = pygame.font.SysFont(self.font, TITLE_FONTS[1])
    text = "Season " + series[1] + "   Episode " + series[2]
    self.text_element2 = self.myfont2.render(text, 1, (self.font_color))
    self.text_width = self.text_element2.get_width()
    self.text_height = self.text_element.get_height()
  
  # Print title texts, only for title-cards
  def text_title(self, screen):
    screen.blit(self.text_element, (self.x+8, self.y))
    screen.blit(self.text_element2, (self.x+15, self.y+self.text_height))
    self.item_list[0].x = self.x+self.text_width+25
    self.item_list[0].y = self.y+self.text_height+5

  # Logic for the scrollbars
  def scrollbar_logic(self, screen, mouse):

    is_hover = False

    # This will only run if we can scroll
    if self.scrollbar_activated == True:  

      # We draw the scrollbar
      self.scrollbar.draw(screen, mouse)  

      # If we have our cursor within the scrollbar, then change the cursor to a finger, 
      # and remain so while dragging it
      if self.scrollbar.check_cursor(mouse) == True or self.scrollbar.active == True:
        is_hover = True

      # If we are dragging the scrollbar, then calculate where it is.  
      if self.scrollbar.active == True:
        self.scrollbar.get_percent()

    return is_hover
  
  def reset(self, fav_list, curr_list):

    self.scroll_index_y = 0
    self.scrollbar_activated = False
    

    if self.special_feature == "Bookmarks":
      self.item_list = make_bookmark_buttons(fav_list)
      
    
    if self.special_feature == "Change" or self.special_feature == "change_post":
      self.item_list = make_change_buttons(curr_list)
      self.special_feature = "Change"
      
  def scroll_scrollbar(self, scroll):
      
    # This is the logic for scrolling with a mousewheel.
    # If mousewheel-scroll is true, and mouse cursor is within the bounds, then scroll.
    if self.special_feature == "series":                               
      self.scrollbar.drag_y += int((10/100)*self.scrollbar.h) * scroll[1] # Each mouse wheel scroll moves the scrollbar 5%
    else:                              
      self.scrollbar.drag_y += int((5/100)*self.scrollbar.h) * scroll[1] # Each mouse wheel scroll moves the scrollbar 5%

    self.scrollbar.check_bounds()                                                   # Checks if we moved the bar outside the scrollbar
    self.scrollbar.get_percent()                                                    # Calculates where the bar is within the scrollbar
    self.mouse_scrolled = True

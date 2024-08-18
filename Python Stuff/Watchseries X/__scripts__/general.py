
# Imported Classes
from __scripts__.settings import *
from __scripts__.button_class import Button   # Button class for all buttons

import pygame


# Figures out the correct scroll direction
def which_way_scroll(y):

  # This variable is the same as the Scroll variable in Main
  scroll = [False, 1]   

  # We check which way we are scrolling.
  if y> 0:                       
    scroll[0] = True
    scroll[1] = -1
  if y < 0:                       
    scroll[0] = True
    scroll[1] = 1

  # Then we return the correct List.
  return scroll

# Check if an element is within a box or outside it
def within_bounds(box, item):
   
   if item.y+item.scroll_index_y > box[1] + box[3] or item.y+item.scroll_index_y + item.height < box[1]:
      return False
   else:
      return True

# Check how much of an element is outside the box
def check_partial_overlap(box, item):
  package = [0, 0]

  # Checks if we see the top of the button
  if item.y + item.scroll_index_y < box[1]:
    package[0] = box[1]-item.y-item.scroll_index_y
  else:
    package[0] = 0
  
  # Checks if we see the bottom of the button
  if item.y + item.scroll_index_y + item.height > box[1]+box[3]:
    package[1] = item.y+item.scroll_index_y+item.height - box[1]-box[3]
  else:
    package[1] = 0

  return package

def mouse_check(mouse, element):
  if mouse[0][0] > element.x and mouse[0][0] < element.x + element.width:
    if mouse[0][1] > element.y and mouse[0][1] < element.y+element.height:
      return True


# Makes a list of series-buttons
def make_series_buttons(data ,pos_y):

  new_list = []

  # Makes it so the name in the button isnt too long
  for index, element in enumerate(data):
    if len(element[0]) > 12:
       title = (element[0])[:12] + ".."
    else:
       title = element[0]

    button = Button(
      150, pos_y+12 + 38*index, 135, 30,                # x, y, w, h, 
      0, 3, ITEM_COLOR, False,          # border_radius, border_width, border_color, will_border_hover,
      CARD_COLOR, ITEM_COLOR,           # color, hover_color, 
      FONT, 18, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
      title, element,                   # name, id, 
      "Button"                          # sepcial
    )
    new_list.append(button)
  return new_list

# Makes the banner menu buttons
def make_banner_buttons():
  new_list = []

  button1 = Button(
    0, 0, 50, 30,                     # x, y, w, h, 
    0, 0, WHITE, False,               # border_radius, border_width, border_color, will_border_hover,
    CARD_COLOR, ITEM_HOVER_COLOR,     # color, hover_color, 
    FONT, 20, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
    str("Home"), ["Home"],            # name, id, 
    "banner"                          # sepcial
    )
  
  button2 = Button(
    0, 0, 90, 30,                     # x, y, w, h, 
    0, 0, WHITE, False,               # border_radius, border_width, border_color, will_border_hover,
    CARD_COLOR, ITEM_HOVER_COLOR,     # color, hover_color, 
    FONT, 20, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
    str("Bookmarks"), ["Bookmarks"],  # name, id, 
    "banner"                          # sepcial
    )
  
  button3 = Button(
  0, 0, 120, 30,                    # x, y, w, h, 
  0, 0, WHITE, False,               # border_radius, border_width, border_color, will_border_hover,
  CARD_COLOR, ITEM_HOVER_COLOR,     # color, hover_color, 
  FONT, 20, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
  str("Change episode"), ["Change"],# name, id, 
  "banner"                          # sepcial
  )

  button4 = Button(
  0, 0, 65, 30,                     # x, y, w, h, 
  0, 0, WHITE, False,               # border_radius, border_width, border_color, will_border_hover,
  CARD_COLOR, ITEM_HOVER_COLOR,     # color, hover_color, 
  FONT, 20, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
  str("Refresh"), ["Refresh"],      # name, id, 
  "banner"                          # sepcial
  )

  new_list.append(button1)
  new_list.append(button2)
  new_list.append(button3)
  new_list.append(button4)


  return new_list

# Makes the buttons for changing episode
def make_change_buttons(list):
  temp_list = []


  for nr in range (0, int(list[0][1])):
    temp_list.append("Season " + str(nr+1))
    for i in range(0, int(list[0][2+nr])):
      btn = Button(
        0, 0, 40, 40,                    # x, y, w, h, 
        0, 0, ITEM_COLOR, False,          # border_radius, border_width, border_color, will_border_hover,
        ITEM_COLOR, ITEM_HOVER_COLOR,     # color, hover_color, 
        FONT, 20, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
        str(i+1), [list[0][0], str(nr+1), str(i+1)],  # name, id, 
        "Button"                          # sepcial
      )
      temp_list.append(btn)
    
  return temp_list

# Makes the buttons for changing episode
def make_bookmark_buttons(list):
  temp = []
  for element in list:
    # Checks if need to shorten series name to fit in button
    name_temp = element[0]
    if len(element[0]) > 15:
       name_temp = (element[0])[:15] + ".."
       
    name = name_temp + " season " + str(element[1]) + " episode " + str(element[2])
    btn = Button(
      0, 100, 340, 40,                                # x, y, w, h, 
      0, 0, ITEM_COLOR, False,                      # border_radius, border_width, border_color, will_border_hover,
      ITEM_COLOR, ITEM_HOVER_COLOR,                 # color, hover_color, 
      FONT, 20, WHITE, WHITE,                       # font, font_size, font_color, font_color_hover
      name, element,                                # name, id, 
      "Button"                                      # sepcial
    )
    temp.append(btn)
  return temp






# Calculates the space between all elements given.
# so they are equadistant from each other. Written with AI.
# data = [[100, 10], 20, 3]  [box_width, box_x], item_width, number_of_items.
def get_equadistant_positions(data):
    
    # First we get the width and x position of the box
    box_width, box_start_x = data[0]

    # Then get the width of the objects within and how many there are.
    object_width = data[1]
    num_objects = data[2]
    
    # We fint the total width of all objects and how many gaps there are (always one more than the number of objects)
    total_object_width = object_width * num_objects
    num_gaps = num_objects + 1
    
    # Calculate the total spacing that needs to be distributed
    total_gap_space = box_width - total_object_width
    
    # Calculate the size of each gap
    gap_size = total_gap_space / num_gaps
    
    # Calculate positions
    positions = []
    current_x = box_start_x + gap_size  # Start from the first gap
    
    for _ in range(num_objects):
        positions.append(current_x)
        current_x += object_width + gap_size
    return positions


# Calculates the space between all elements in the banner
# so they are equadistant from each other.
# data = [[100, 10], 20, 10, 15]  # Box of width 100 starting at x=10, with objects of width 20, 10, and 15
def get_equadistant_positisjon_set_number_of_elements(data):
    screen_width, screen_x = data[0]
    element_widths = data[1:]

    num_elements = len(element_widths)

    # Calculate total space occupied by elements
    total_elements_width = sum(element_widths)

    # Calculate the remaining space to be divided into gaps
    total_gaps_width = screen_width - total_elements_width

    # Calculate the number of gaps (between elements and at the ends)
    num_gaps = num_elements + 1

    # Calculate the size of each gap
    gap_size = total_gaps_width / num_gaps

    # Calculate the new x coordinates
    new_x_coordinates = []
    current_x = screen_x + gap_size

    for width in element_widths:
        new_x_coordinates.append(current_x)
        current_x += width + gap_size

    return new_x_coordinates
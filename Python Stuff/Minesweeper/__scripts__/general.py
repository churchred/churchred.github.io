from __scripts__.settings import *
from __scripts__.button_class import Button

def center_gameboard(size_data, diff):

  
  # Find how much space we have leftover on screen
  space_left_over = DIFFICULTY[diff][5][0] - DIFFICULTY[diff][4][0]

  # Find how much space we need on either side
  space_on_each_side = space_left_over / 2

  # We place the gameboard a few pixels over the bottom of the screen
  new_y_location = 100

  # Make the new list to return
  data_to_return = [space_on_each_side, new_y_location]

  return data_to_return 



def make_reset_btn(diff, skin):

  # Size and location of button
  w = 60
  h = 60
  x = DIFFICULTY[diff][5][0] / 2 - w/2
  y = 100/2 - h/2
  
  # Make the button
  btn = Button(
        x, y, w, h,                            # x, y, w, h, 
        0, 2, BLACK, False,                    # border_radius, border_width, border_color, will_border_hover,
        GRAY, GRAY_LIGHT,                      # color, hover_color, 
        "Arial", 25, WHITE, WHITE,             # font, font_size, font_color, font_color_hover
        "", ["Reset"], "Image", SKINS[skin][1] # name, id, special, Which skin
      )

  return btn
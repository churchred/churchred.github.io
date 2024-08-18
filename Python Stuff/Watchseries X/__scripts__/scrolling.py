import pygame
from __scripts__.settings import *    # Basic, unchangeable variabels

class Scroll():
  def __init__(self, w, h, x, y):
   
   # Stats
   self.w = w
   self.h = h
   self.x = x
   self.y = y

   self.rows = 0

   self.drag_h = 30 # Height of draggable item inside scrollbar
   self.drag_y = y  # Location of draggable item inside scrollbar

   self.color = SCROLLBAR_BG
   self.drag_color = SCROLLBAR

   # This is true if we are currently using the scrollbar
   self.active = False
  
   # How far the draggable item has moved down the scrollbar
   self.percent = 0
   


   self.start_pos_mouse = 0


  # Check if the cursor is within the bar
  def check_cursor(self, mouse):
    if mouse[0][0] > self.x and mouse[0][0] < self.x + self.w:
      if mouse[0][1] > self.drag_y and mouse[0][1] < self.drag_y+self.drag_h:
        return True
               
  # Keeps the draggable item from moving too far down and up (out of bounds of the scrollbar)
  def check_bounds(self):
    if self.drag_y+self.drag_h > self.y+self.h:
      self.drag_y = self.y+self.h-self.drag_h+1
    if self.drag_y < self.y:
      self.drag_y = self.y

  # How far too move the screen at any self.percent
  def calculate_move_distance(self, row_size, s_h):
    item_height = self.rows * row_size
    effective_screen_height = s_h

    self.temp_y = ((self.percent)/100) * (item_height - effective_screen_height)
    return (self.temp_y) * -1

  # Caluclate how far down the draggable item has moved on the scrollbar
  def get_percent(self):
    self.percent = ((self.drag_y-self.y)*100) / (self.h-self.drag_h)
    #print((self.percent))

  # Draw the scrollbar and run the logic
  def draw(self, SCREEN, mouse):
    pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.w, self.h))
    pygame.draw.rect(SCREEN, self.drag_color, (self.x, self.drag_y, self.w, self.drag_h))

    # If we hover over the scrollbar AND click down the mouse
    if mouse[1][0] == True and self.check_cursor(mouse) == True and self.active == False:
      self.active = True
      self.start_pos_mouse = mouse[0][1] - self.drag_y
    
    # If we then at anypoint let go of the mouse
    if mouse[1][0] == False:
      self.active = False
    
    # As long as active is True then the draggable item will follow the mouse.y coordiates
    if self.active == True:
      self.drag_y = mouse[0][1] - self.start_pos_mouse

    # Keeps the draggable item from moving too far down and up (out of bounds of the scrollbar)
    self.check_bounds()

  # Calculates the size of the draggable item within the scrollbar. 
  # The size is proposional to how big percentage of the possible conent
  # we can view in the viewable portion of the screen.
  def calculate_size(self, row_size, s_h):
    temp = (((s_h) * 100) / (self.rows*row_size))
    self.drag_h = (temp/100) * self.h
    self.get_percent()

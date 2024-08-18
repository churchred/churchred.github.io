import pygame
from __scripts__.settings import *    # Basic, unchangeable variabels



# Loadingbar 
class Loadingbar():
  def __init__(self, x, y, w, h, border_size, txt, list, type):

    # Season loadbar or total episode loadbar?
    self.loadtype = type
    self.type = "loadbar"
    
    # Size
    self.width = w          # The bars total width
    self.w_percent = 0  # How much of the bar is filled
    self.height = h          # Height of the bar, not including border'

    # Position
    self.x = x
    self.y = y

    # Text variabels
    self.font_size = 16
    self.font_color = WHITE
    self.font = 'Arial'

    self.text_name = ""
    self.ending_text = txt
    self.text_width = 0
    self.text_height = 0

    self.myfont = pygame.font.SysFont(self.font, self.font_size)
    self.text_element = ""

    # Color
    self.color = ITEM_COLOR
    self.border_color = ITEM_COLOR
    self.color2 = CARD_COLOR
    self.border_size = border_size

    # Info about current series
    self.current_series = list

    # Variabels and info for making percentages
    self.make_percent(0)

    # Filling info
    self.speed = 500

  
  def draw(self, SCREEN, dt):

    if self.old_percent != self.percentages:
      self.move_bar(dt)

    # Border    
    pygame.draw.rect(SCREEN, self.border_color, (self.x, self.y, self.width, self.height))
    pygame.draw.rect(SCREEN, self.color2, (self.x+self.border_size, self.y+self.border_size, self.width-self.border_size*2, self.height-self.border_size*2))
    

    # Fill
    pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.w_percent, self.height))

    # Text
    SCREEN.blit(self.text_element, (self.x + self.width/2 - self.text_width/2, self.y + self.height/2 - (self.text_height)/2))

  def reset(self, nr):

    # Reset to empty
    if nr == 0:
      self.w_percent = 0
      self.old_percent = 0
      self.percentages = 0
    # Reset to full
    if nr == 1:
      self.w_percent = self.width
      self.old_percent = 100
      self.percentages = 100

  def move_bar(self, dt):
    # Checks if the bar needs to grow bigger
    if self.percentages > self.old_percent:
      self.w_percent += self.speed * dt
      if self.w_percent*100/self.width >= self.percentages:
        self.w_percent = self.width*self.percentages/100
        self.old_percent = self.percentages
    
    # Checks if the bar need to grow smaller
    if self.percentages < self.old_percent:
      self.w_percent -= self.speed * dt
      if self.w_percent*100/self.width <= self.percentages:
        self.w_percent = self.width*self.percentages/100
        self.old_percent = self.percentages

  def make_text(self):
    self.text_name = str(self.seen_episodes) + " / " + str(self.total_episodes) + " " + self.ending_text
    self.text_element = self.myfont.render(self.text_name, 1, self.font_color)
    self.text_width, self.text_height =  self.text_element.get_width(), self.text_element.get_height()
 
  def make_percent(self, nr):
    
    if nr == 0:
      self.old_percent = 0  # Old percent decides move direction

    self.percentages = 0    # Percent completion
    self.total_episodes = 0 # total episodes avaliable
    self.seen_episodes = 0  # Total episodes seen

    # If this bar is for total episodes
    if self.loadtype == "total":
      # How many episodes the series has in total
      for i in range(2, len(self.current_series[0])):
        self.total_episodes += int(self.current_series[0][i])

      # How many we have seen
      for i in range(0, int(self.current_series[1][1])-1):
        self.seen_episodes += int(self.current_series[0][i+2])
      self.seen_episodes += int(self.current_series[1][2])

      # Get the current percent
      if self.seen_episodes == self.total_episodes:
        self.percentages = int(((self.seen_episodes) * 100) / self.total_episodes)
      else:
        self.percentages = int(((self.seen_episodes-1) * 100) / self.total_episodes)
      print("\n", "Progressbar info(total):")
      print("   " + self.current_series[0][0] + ": " + str(self.seen_episodes) + " / " + str(self.total_episodes) + " episodes seen in total  -  " + str(self.percentages) + "%")

    # Is this bar is for episodes this season
    if self.loadtype == "season":
       # Gets the percentage of current season
      self.total_episodes = int(self.current_series[0][int(self.current_series[1][1])+1])
      self.seen_episodes = int(self.current_series[1][2])
      if self.seen_episodes == 1:
        self.percentages = int(((self.seen_episodes-1) * 100) / self.total_episodes)
      else:
        self.percentages = int(((self.seen_episodes) * 100) / self.total_episodes)
      print("\n", "Progressbar info(season):")
      print("   " + self.current_series[0][0] + ": " + str(self.seen_episodes) + " / " + str(self.total_episodes) + " episodes this season  -  " + str(self.percentages) + "%")

    self.make_text()
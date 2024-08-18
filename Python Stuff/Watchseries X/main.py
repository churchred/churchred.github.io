
# Import pygame reletated things
import pygame, sys, os
pygame.init()
pygame.font.init()

# Import other python scripts
from __scripts__.settings import *            # Basic, unchangeable variabels
from __scripts__.general import *             # General functions
from __scripts__.load import LoadData         # A Class about loading/saving data
from __scripts__.button_class import Button   # Button class for all buttons
from __scripts__.box_class import Box         # Button class for all buttons
from __scripts__.loadbar import Loadingbar    # Button class for all buttons


class App():
  def __init__(self):

    # Pygame stuff
    pygame.init()
    pygame.display.set_caption(VERSION)
    self.app_running = True

    # If testing, and we dont want a video to open, 
    # and we show FPS in title
    self.testing = False

    # Makes the app screen and internal clock
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    self.clock = pygame.time.Clock()

    # Important variables
    self.window = "Home"  # Which layer is open   (home, bookmark, change)
    self.cursor = False   # When to change the cursor to a pointer (False=Arrow)

    # Storage variabels
    self.Name_List = []      # List with the names and number of episodes/seasons of all series
    self.Save_list = []      # List with all info on which episode/season we are at
    self.Fav_List = []       # List with bookmarks
    self.current_series = [] # This list contains information about the current series.

    # Scrolling variabels
    self.scroll = [False, 1, ""] # False means we are not scrolling, and the second spot is either 1 or -1, last is target
                                 # based on the direction we want to scroll
    self.scroll_target = ""      # Where we hover the mouse

    # Load all data 
    self.start_up()
        
    # Exception Variabels
    # The possible videoformats we use.
    self.video_formats = [ 
      "mp4", "mov", "wmv",
      "avi", "mkv", "m4p",
      "m4v"
      ] 
    

    # Makes the rest of the boxes
    self.make_boxes()

    # Check if current episode is bookmarked
    self.check_if_bookmarked()

    # Update banner disabled state
    self.banner.item_list[0].disabled = True
    self.banner.item_list[1].disabled = False
    self.banner.item_list[2].disabled = False




  # This runs once at launch.
  def start_up(self):

    # First we use load.py to gather information about
    # the folders in our directiory and/or read save data.
    # It then returns two lists, the data from Names.txt and Stats.txt
    self.Load_Data = LoadData()                                            # Makes an element from the class LoadData in load.py
    self.Name_List, self.Save_list, self.Fav_List = self.Load_Data.load()  # Gets all info from the Loaddata class
    self.current_series = [self.Name_List[0], self.Save_list[0]]           # Sets which series we are currently focusing on
    
    # Prints info about the current series
    print("\nWelcome to WatchSeries 2.0")
    print("\n Info about current series:")
    print("   General info: ", self.current_series[0])
    print("   Saved info:   ", self.current_series[1])





  #
  # Runs the app
  #
  #
  def run(self):
    while self.app_running:
      
      # This loop runs everytime pygame catches
      # an event. Such as, keypress, exit, mousewheel.
      for event in pygame.event.get(): 

        # What happens if we exit the app
        if event.type == pygame.QUIT:   
          pygame.quit()
          sys.exit()

        # What happens if we scroll the mousewheel
        # [True, 1/-1], name 
        if event.type == pygame.MOUSEWHEEL:
          self.scroll = which_way_scroll(event.y)
          #print("Mouse-scroll detected: ", self.scroll)

      # Gather basic data
      self.dt = self.clock.tick(FPS) / 1000  # Delta time. Used for smooth animations
      self.mouse = [pygame.mouse.get_pos(),  # Mouse position and pressed-state.
               pygame.mouse.get_pressed()]
               
      # Turns pointer cursor back to arrow
      # All clickable elements will, if hovered over,
      # make the cursor True. Which later will change
      # the cursor into a finger(the 'its clickable' icon)
      self.cursor = False

      # Where the mouse is (for scrolling)
      self.target = None

      # Background color of app
      self.screen.fill(BACKGROUND_COLOR)

      if self.window == "Change":
        self.change_ep_logic()

      if self.window == "Bookmarks":
        self.bookmarks_logic()
                         
      # Draws the screen banner
      self.serie_logic()
      #pygame.draw.rect(self.screen, CARD_COLOR, (self.positions_x[1], self.positions_y[0], RIGHT_CARD[0], RIGHT_CARD[1]), border_radius=5) 
      self.banner_logic()
      

      # The things we see when at Home-screen                   
      if self.window == "Home":
        self.home_logic()

      # Checks where the mouse is for scrolling purposes
      self.check_mouse_location()

      self.scroll = [False, 1]


      # Draw two rects. One above and one below the card, to hide scrolling elements out of bounds
      pygame.draw.rect(self.screen, BACKGROUND_COLOR, (0, self.banner.y+self.banner.height, SCREEN_WIDTH, 15), border_radius=0)  
      pygame.draw.rect(self.screen, BACKGROUND_COLOR, (0, self.series_box.y+self.series_box.height, SCREEN_WIDTH, 15), border_radius=0)  


      # This code decides which mouse cursor we will display,
      # an arrow or pointer. Cursor is true if we are hovering something.
      if self.cursor == True:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
      elif self.cursor == False:	
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

      # Update screen and clock
      self.clock.tick(FPS) # Default FPS Limit: 60

      # Checks which caption to set it the window-banner
      # If testing is true we want to display FPS.
      if self.testing == True:
        pygame.display.set_caption(VERSION + "     -     FPS (" + str(int(self.clock.get_fps())) + ")")
      if self.testing == False:
        pygame.display.set_caption(VERSION)

      # Updates the app window
      pygame.display.update()


  # Draw the banner and run its logic
  def banner_logic(self):

    # Draw the banner and its elements and return a list of
    # info about clicks and hover. 
    package = self.banner.draw(self.screen, self.mouse, self.dt, self.current_series, self.scroll) 

    # Checks if we are hovering element in banner
    if package[0] == True:
      self.cursor = True

    if package[1] != "":

      # If we clicked an element, what do we do?
      if package[1][0] == "Home":
        print("\nClicked: ", package[1])
        self.window = "Home"
        self.banner.item_list[0].disabled = True
        self.banner.item_list[1].disabled = False
        self.banner.item_list[2].disabled = False

      # If we clicked an element, what do we do?
      if package[1][0] == "Bookmarks":
        print("\nClicked: ", package[1])
        self.window = "Bookmarks"
        self.banner.item_list[0].disabled = False
        self.banner.item_list[1].disabled = True
        self.banner.item_list[2].disabled = False

      # If we clicked an element, what do we do?
      if package[1][0] == "Change":
        print("\nClicked: ", package[1])
        self.window = "Change"
        self.banner.item_list[0].disabled = False
        self.banner.item_list[1].disabled = False
        self.banner.item_list[2].disabled = True

      # If we clicked an element, what do we do?
      if package[1][0] == "Refresh":
        print("\nClicked: ", package[1])
        self.app_running = False

  # Draw the series-card and run its logic
  def serie_logic(self):
    
    # Draw the banner and its elements and return a list of
    # info about clicks and hover. 
    package = self.series_box.draw(self.screen, self.mouse, self.dt, self.current_series, self.scroll)  

    # Checks if we are hovering element in banner
    if package[0] == True:
      self.cursor = True

    if package[1] != "":
      print("Clicked: ", package[1])
      if package[1][0] != self.current_series[0][0]:
       self.change_series(package[1][0])
  
  # Draw the home-screen and run its logic
  def home_logic(self):
    package = self.right_box.draw(self.screen, self.mouse, self.dt, self.current_series, self.scroll)  
    
    # Checks if we are hovering element in banner
    if package[0] == True:
      self.cursor = True

    if package[1] != "":
      print("Clicked: ", package[1])
      if package[1][0] == "bookmark":
        self.add_bookmark() # Adds or removes bookmarks
        self.reset_tabs()   # Resets change and bookmark pages

      if package[1][0] == "next":
        self.next_ep()
      if package[1][0] == "prev":
        self.prev_ep()
      if package[1][0] == "watch":
        self.play_episode()

  # Draw the Change-series tab and run its logic
  def change_ep_logic(self):
    package = self.change_box.draw(self.screen, self.mouse, self.dt, self.current_series, self.scroll)  
    
    # Checks if we are hovering element in banner
    if package[0] == True:
      self.cursor = True

    if package[1] != "":
      print("Clicked: ", package[1])

      # Sets new place as current
      self.current_series[1][0] = package[1][0]
      self.current_series[1][1] = package[1][1]
      self.current_series[1][2] = package[1][2]
      
      # Do all the things we need to do upon changing ep
      self.logic_after_switching_episode()

      self.banner.item_list[0].disabled = True
      self.banner.item_list[1].disabled = False
      self.banner.item_list[2].disabled = False

      self.window = "Home"

  # Draw the bookmarks tab and run its logic
  def bookmarks_logic(self):
    package = self.bookmarks_box.draw(self.screen, self.mouse, self.dt, self.current_series, self.scroll) 
    
    # Checks if we are hovering element in banner
    if package[0] == True:
      self.cursor = True

    if package[1] != "":
      print("Clicked: ", package[1])

      # Sets new place as current
      self.current_series[1][0] = package[1][0]
      self.current_series[1][1] = package[1][1]
      self.current_series[1][2] = package[1][2]
      
      # Do all the things we need to do upon changing ep
      self.logic_after_switching_episode()

      self.banner.item_list[0].disabled = True
      self.banner.item_list[1].disabled = False
      self.banner.item_list[2].disabled = False

      self.window = "Home"
      




 # When changing to a new series
  def change_series(self, name):
    # Goes trough the list of series untill it finds a series with
    # a name matching the name given from the series button we clicked
    # then it changes current series and completly resets the stat_page
    for index, sublist in enumerate(self.Save_list):
        if sublist[0] == name:
            self.current_series = [self.Name_List[index], self.Save_list[index]]
            self.title_box.make_title_texts(self.current_series[1])
    for element in self.progress_box.item_list:
      element.current_series = self.current_series
      element.reset(0)
      element.make_percent(0)

    self.check_if_bookmarked()

    # Resets change and bookmark pages
    self.reset_tabs()

  # When changing to the NEXT episode
  def next_ep(self):
    print("\n")
    print("Next episode!")

    if self.current_series[1][2] == self.current_series[0][int(self.current_series[1][1])+1]:
      print("   No more episodes this season")
      if self.current_series[1][1] == self.current_series[0][1]:
        print("   No more seasons")
      else:
        print("   There are more seasons")
        self.progress_box.item_list[1].reset(0)
        self.current_series[1][1] = str(int(self.current_series[1][1])+1) # Episode total count for the new season
        self.current_series[1][2] = str(1)
        
    else:
      print("   There are more episodes in this season")
      self.current_series[1][2] = str(int(self.current_series[1][2])+1)

    self.logic_after_switching_episode()

  # When pressing "prev" button
  def prev_ep(self):
    print("\n")
    print("Prevoius episode...")
    if self.current_series[1][2] == '1':
      print("    Cant go more back this season")
      if self.current_series[1][1] == '1':
        print("    No prev seasons")
      else:
        print("   There are previous seasons")
        self.progress_box.item_list[1].reset(1)
        self.current_series[1][1] = str(int(self.current_series[1][1])-1)
        self.current_series[1][2] = self.current_series[0][int(self.current_series[1][1])+1]
        
    else:
      print("   There are prev episodes in this season")
      self.current_series[1][2] = str(int(self.current_series[1][2])-1)

    self.logic_after_switching_episode()

  # The logic for starting the episode
  def play_episode(self):
    if self.testing == True:
      print("\nVideo launch blocked! Testing active!")
    else:
      print("\nLaunching video..")

      # First we read the path to the folder
      path = self.Load_Data.ReadPath()
      found = False

      # Then we see if we find a match
      for i in self.video_formats:
          openfile = str(path + "\\" + self.current_series[1][0] + "\\Season " + self.current_series[1][1] + "\\Episode " + self.current_series[1][2] + "." + i)
          try:
            print("Video found! Playing: ", openfile)
            os.startfile(openfile)
          except Exception as e:
            print("Error: ", e)


  # What happens when clicking "Add Bookmark" button. Adds or removes bookmarks
  def add_bookmark(self):
    # First we check if it already is bookmarked
    duplicate = False
    for i in self.Fav_List:
      if i == self.current_series[1]:
        duplicate = True

    # If it is already added we do this    
    if duplicate == True:
        print("\nRemoving bookmark!")
        to_add = [self.current_series[1][0], self.current_series[1][1], self.current_series[1][2]]
        self.Fav_List.remove(to_add)
        self.bookmark_btn.disabled = False

    # Otherwise we do this
    else: 
        print("Adding bookmark!")
        to_add = [self.current_series[1][0], self.current_series[1][1], self.current_series[1][2]]
        self.Fav_List.append(to_add)
        self.bookmark_btn.disabled = True

    self.Fav_List = sorted(self.Fav_List, key=lambda x: (x[0], int(x[1]), int(x[2])))
    self.Load_Data.save_bookmarks(self.Fav_List)
    self.bookmark_btn.check_disabled(0)

  # What happens when we switch episodes or series. Check if current ep is bookmarked or not
  def check_if_bookmarked(self):
    # First we check if it already is bookmarked
    duplicate = False
    for i in self.Fav_List:
      if i == self.current_series[1]:
        duplicate = True

    if duplicate == True:
      self.bookmark_btn.disabled = True
    else:
      self.bookmark_btn.disabled = False

    self.bookmark_btn.check_disabled(0)
    
  # This runs after we switch epiosdes. Resets and updates progressbars and titles, save data etc.
  def logic_after_switching_episode(self):

    # Saves the new location
    self.Load_Data.save_stats(self.Save_list)

    # Updates loadingbars
    self.progress_box.item_list[1].make_percent(1)
    self.progress_box.item_list[0].make_percent(1)

    # Check if new episode is bookmarked
    self.check_if_bookmarked()

    # Updates text title
    self.title_box.make_title_texts(self.current_series[1])

    # Acutally opens the episode
    #self.play_episode()

  # Resets bookmark and change episode tabs when switching series
  def reset_tabs(self):
    self.bookmarks_box.reset(self.Fav_List, self.current_series)
    self.change_box.reset(self.Fav_List, self.current_series)

  # Checks were the mouse is for scrolling purposes
  def check_mouse_location(self):
    # Check series box
    if self.scroll[0] == True:
      if mouse_check(self.mouse, self.series_box):
        self.series_box.scroll_scrollbar(self.scroll)
      elif mouse_check(self.mouse, self.right_box):
        if self.window == "Bookmarks":
          self.bookmarks_box.scroll_scrollbar(self.scroll)
        if self.window == "Change":
          self.change_box.scroll_scrollbar(self.scroll)
    

    





  # Makes all the elements we see on screen
  def make_boxes(self):

    # Makes the buttons used in the banner, 
    # and the banner box itself
    self.banner_buttons = make_banner_buttons()
    self.banner = Box(
      0, 0, BANNER_CARD[2], BANNER_CARD[3], 0, CARD_COLOR,   # x, y, w, h, border_radius, background_color
      4, 0, 0, 1,                              # colums, space_row, space_col, max_rows_before_scroll
      self.banner_buttons,                     # item_list, 
      True, True,                              # centered_vertical, centered_horizon,
      False, "",                               # title_scroll, title, 
      FONT, 15, WHITE, 0, 0,                   # font, font_size, font_color, text_x, text_y
      False,                                   # scrollbar_possible,
      "banner"                                 # special
    )

    # First we calculate the coordinates for the right and left side    
    self.positions_x = get_equadistant_positisjon_set_number_of_elements([[BG_CARD[2], BG_CARD[0]], SERIES_CARD[0], RIGHT_CARD[0]])
    self.positions_y = get_equadistant_positisjon_set_number_of_elements([[BG_CARD[3], BG_CARD[1]], SERIES_CARD[1]])

    # Make all the needed series buttons and put them in a list
    series_list = make_series_buttons(self.Save_list, self.positions_y[0])

    # Make series box
    self.series_box = Box(
      self.positions_x[0], self.positions_y[0], SERIES_CARD[0], SERIES_CARD[1], 5, CARD_COLOR,     # x, y, w, h, border_radius, background_color
      1, 0, 0, 5,                     # colums, space_row, space_col, max_rows_before_scroll
      series_list,                  # item_list, 
      False, True,                    # centered_vertical, centered_horizon,
      False, "",                      # title_scroll, title, 
      FONT, 15, WHITE, 0, 0,          # font, font_size, font_color, text_x, text_y
      True,                          # scrollbar_possible,
      "series"                              # special
    )

    # Makes loadingbars (x, y, w, h, col, col2, border_size):
    self.loadbar_total = Loadingbar(0,  0, 400, 25, 3, " watched in total", self.current_series, "total")
    self.loadbar_season = Loadingbar(0, 0, 400, 25, 3, " watched this season", self.current_series, "season")
    loadingbar_list = [self.loadbar_total , self.loadbar_season]

    # Make player buttons
    self.next_button = Button(
      0, 0, 120, 40,                    # x, y, w, h, 
      0, 0, ITEM_COLOR, False,          # border_radius, border_width, border_color, will_border_hover,
      ITEM_COLOR, ITEM_HOVER_COLOR,     # color, hover_color, 
      FONT, 20, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
      "Next", ["next"],                   # name, id, 
      "Button"                          # sepcial
    )

    self.prev_button = Button(
      0, 0, 120, 40,                    # x, y, w, h, 
      0, 0, ITEM_COLOR, False,          # border_radius, border_width, border_color, will_border_hover,
      ITEM_COLOR, ITEM_HOVER_COLOR,     # color, hover_color, 
      FONT, 20, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
      "Prev", ["prev"],                   # name, id, 
      "Button"                          # sepcial
    )

    self.watch_button = Button(
      0, 0, 120, 40,                    # x, y, w, h, 
      0, 0, ITEM_COLOR, False,          # border_radius, border_width, border_color, will_border_hover,
      ITEM_COLOR, ITEM_HOVER_COLOR,     # color, hover_color, 
      FONT, 20, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
      "Watch", ["watch"],                   # name, id, 
      "Button"                          # sepcial
    )

    # Makes the list to but all player buttons into
    player_btns = [self.prev_button, self.watch_button, self.next_button]

    # Makes the add bookmark button
    self.bookmark_btn = Button(
      0, 0, 85, 16,                     # x, y, w, h, 
      0, 0, ITEM_COLOR, False,          # border_radius, border_width, border_color, will_border_hover,
      ITEM_COLOR, ITEM_HOVER_COLOR,     # color, hover_color, 
      FONT, 14, WHITE, WHITE,           # font, font_size, font_color, font_color_hover
      "Add bookmark", ["bookmark"],            # name, id, 
      "Button"                          # sepcial
    )
    bm_list = [self.bookmark_btn]

    # Make title_card
    self.title_box = Box(
      self.positions_x[0], 0, RIGHT_CARD[0], RIGHT_ELEMENT_SIZES[0], 5, CARD_COLOR,     # x, y, w, h, border_radius, background_color
      1, 0, 0, 6,                    # colums, space_row, space_col, max_rows_before_scroll
      bm_list,                            # item_list, 
      True, True,                   # centered_vertical, centered_horizon,
      False, "",                     # title_scroll, title, 
      FONT, 15, WHITE, 0, 0,         # font, font_size, font_color, text_x, text_y
      False,                          # scrollbar_possible,
      "title", current_series=self.current_series[1]                        # special
    )

    # Make progress_card
    self.progress_box = Box(
      self.positions_x[1], 0, RIGHT_CARD[0], RIGHT_ELEMENT_SIZES[1], 0, CARD_COLOR,     # x, y, w, h, border_radius, background_color
      1, 0, 0, 3,                 # colums, space_row, space_col, max_rows_before_scroll
      loadingbar_list,            # item_list, 
      True, True,                 # centered_vertical, centered_horizon,
      False, "",                  # title_scroll, title, 
      FONT, 15, WHITE, 0, 0,      # font, font_size, font_color, text_x, text_y
      False,                       # scrollbar_possible,
      "loadbar"                   # special
    )

    # Make player_card
    self.player_box = Box(
      self.positions_x[0], 0, RIGHT_CARD[0], RIGHT_ELEMENT_SIZES[2], 5, CARD_COLOR,     # x, y, w, h, border_radius, background_color
      3, 0, 0, 6,                     # colums, space_row, space_col, max_rows_before_scroll
      player_btns,                    # item_list, 
      True, True,                     # centered_vertical, centered_horizon,
      False, "",                      # title_scroll, title, 
      FONT, 15, WHITE, 0, 0,          # font, font_size, font_color, text_x, text_y
      False,                          # scrollbar_possible,
      ""                              # special
    )

    # List of all the cards going into the right-side home screen
    card_list = [self.title_box, self.progress_box, self.player_box]

    # Make right_card
    self.right_box = Box(
      self.positions_x[1], self.positions_y[0], RIGHT_CARD[0], RIGHT_CARD[1], 5, CARD_COLOR,     # x, y, w, h, border_radius, background_color
      1, 0, 0, 6,                                                                                # colums, space_row, space_col, max_rows_before_scroll
      card_list,                                                                                # item_list, 
      True, True,                                                                                # centered_vertical, centered_horizon,
      False, "",                                                                                 # title_scroll, title, 
      FONT, 1, WHITE, 0, 0,                                                                      # font, font_size, font_color, text_x, text_y
      False,                                                                                     # scrollbar_possible,
      "card"                                                                                     # special
    )

    change_list = make_change_buttons(self.current_series)

    # Make change_ep card
    self.change_box = Box(
      self.positions_x[1], self.positions_y[0], RIGHT_CARD[0], RIGHT_CARD[1], 5, CARD_COLOR,    # x, y, w, h, border_radius, background_color
      6, 0, 0, 3,                                                                               # colums, space_row, space_col, max_rows_before_scroll
      change_list,                                                                              # item_list, 
      False, False,                                                                             # centered_vertical, centered_horizon,
      True, "Change episode",                                                                  # title_scroll, title, 
      FONT, 35, WHITE, self.positions_x[1]+5, self.positions_y[0],                              # font, font_size, font_color, text_x, text_y
      True,                                                                                     # scrollbar_possible,
      "Change", current_series=self.current_series                                              # special
    )


    bookmark_list = make_bookmark_buttons(self.Fav_List)

    # Make bookmarks card
    self.bookmarks_box = Box(
      self.positions_x[1], self.positions_y[0], RIGHT_CARD[0], RIGHT_CARD[1], 5, CARD_COLOR,    # x, y, w, h, border_radius, background_color
      1, 0, 0, 4,                                                                               # colums, space_row, space_col, max_rows_before_scroll
      bookmark_list,                                                                              # item_list, 
      False, False,                                                                             # centered_vertical, centered_horizon,
      True, "Bookmarks",                                                                  # title_scroll, title, 
      FONT, 35, WHITE, self.positions_x[1]+5, self.positions_y[0],                              # font, font_size, font_color, text_x, text_y
      True,                                                                                     # scrollbar_possible,
      "Bookmarks", current_series=self.current_series                                              # special
    )

# App-logic
if __name__ == '__main__':
  while True:
    app = App()
    app.run()

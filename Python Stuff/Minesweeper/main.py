
# Import pygame reletated things
import pygame, sys, time
pygame.init()
pygame.font.init()

# Import other python scripts
from __scripts__.settings import *  
from __scripts__.general import center_gameboard, make_reset_btn
from __scripts__.game import Game
from __scripts__.number_display import Display
from __scripts__.colors import *
from __scripts__.title import Title

class App():
  def __init__(self):

    # Pygame stuff
    pygame.init()
    pygame.display.set_caption(VERSION)
    self.app_running = True # App runs as long as this is True
    self.testing = True     # Shows FPS and other info if we are testing
    self.cursor = False     # When to change the cursor to a pointer (False=Arrow)
    self.window = "Title"    # Which window we view

    # Current skin
    self.skin_index = 0

    # Current difficulty
    self.difficulty = 0

    # Makes the app screen and internal clock
    self.change_screen_size(TITLE_WIDTH, TITLE_HEIGHT) #DIFFICULTY[self.difficulty][5][0], DIFFICULTY[self.difficulty][5][1])
    self.clock = pygame.time.Clock()

    # If this is true, then a game is in progress
    # Stops the clocks if False
    self.game_in_progress = True

    # Loads all assets
    self.load_images()

    # Makes all the game items, also used to reset them
    self.reset()



    # Makes the title screen
    self.title_screen = Title(self.skin_index)

  

  # Runs the app
  def run(self):
    while self.app_running:
      
      # This loop runs everytime pygame catches
      # an event. Such as, keypress, exit, mousewheel.
      for event in pygame.event.get(): 

        # What happens if we exit the app
        if event.type == pygame.QUIT:   
          pygame.quit()
          sys.exit()

      # Gather basic data
      self.dt = self.clock.tick(FPS) / 1000  # Delta time. Used for smooth animations
      self.mouse = [pygame.mouse.get_pos(),  # Mouse position and pressed-state.
               pygame.mouse.get_pressed()]
      
               
      # Turns pointer cursor back to arrow
      # All clickable elements will, if hovered over,
      # make the cursor True. Which later will change
      # the cursor into a finger(the 'its clickable' icon)
      self.cursor = False

      # Background color of app
      self.screen.fill(SKINS[self.skin_index][2][0])
      

      if self.window == "Title":
        self.title_logic()

      if self.window == "Game":
        self.game_logic()

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


  # This is where the game is run
  def game_logic(self):
      
      self.screen.blit(self.bg_image, (0, 0))
      
      # Runs the gameboard logic
      package = self.game.run(self.screen, self.mouse)
      if package[2] == True:          # If we have clicked a Tile on the board
        self.game_in_progress = False # The game is in progress(used to control timer)

      # Flag display and logic
      self.flag_display.draw(self.screen, str(package[1]))

      # If we have started the game AND the clock is not already counting
      # then get the start time and current time 
      # (which right now are equal, and means 'current-start=0' --> 0 seconds have passed)
      if self.game.started == True and self.start_time == 0:
        self.start_time = time.time()
        self.current_time = time.time()

      # Time display and logic
      if self.game_in_progress == True and self.game.started == True:
        self.current_time = time.time()
      
      # Elapsed time is calculated by finding difference between start time and current time
      self.elapsed_time = round(self.current_time - self.start_time)

      # Draw the timer display
      self.timer_display.draw(self.screen, str(self.elapsed_time))

      # Reset button
      package = self.reset_btn.draw(self.screen, self.mouse)
      if package[0] == True:    # If we hover it
        self.cursor = True      # Change cursor
      if package[1] == "Reset": # If we clicked it
        self.window = "Title"
        self.change_screen_size(TITLE_WIDTH, TITLE_HEIGHT)


  # This is where main screen logic happens
  def title_logic(self):

    self.screen.blit(self.bg_image2, (0, 0))
    
    package = self.title_screen.draw(self.screen, self.mouse)

    if package[0] == True:
      self.cursor = True

    if package[1] == "Beginner":
      self.window = "Game"
      self.difficulty = 0
      self.change_screen_size(DIFFICULTY[self.difficulty][5][0], DIFFICULTY[self.difficulty][5][1])
      self.load_images()
      self.reset()

    if package[1] == "Intermidiate":
      self.window = "Game"
      self.difficulty = 1
      self.change_screen_size(DIFFICULTY[self.difficulty][5][0], DIFFICULTY[self.difficulty][5][1])
      self.load_images()
      self.reset()

    if package[1] == "Expert":
      self.window = "Game"
      self.difficulty = 2
      self.change_screen_size(DIFFICULTY[self.difficulty][5][0], DIFFICULTY[self.difficulty][5][1])
      self.load_images()
      self.reset()

    if package[1] == "Skins":
      print("New skin")
      self.skin_index += 1
      if self.skin_index >= len(SKINS):
        self.skin_index = 0
      self.load_images()
      self.reset()
      self.title_screen.skin_index = self.skin_index
      self.title_screen.reset()


  # Loads all the images we need
  def load_images(self):

    # Load background image
    self.bg_image = pygame.image.load(SKINS[self.skin_index][1] + "bg.png").convert_alpha()
    self.bg_image = pygame.transform.scale(self.bg_image, (DIFFICULTY[self.difficulty][5][0], DIFFICULTY[self.difficulty][5][1])) 
    self.bg_image2 = pygame.transform.scale(self.bg_image, (TITLE_WIDTH, TITLE_HEIGHT))  


    # Load Tile image
    self.tile_image = pygame.image.load(SKINS[self.skin_index][1] + "tile.png").convert_alpha()
    self.tile_image = pygame.transform.scale(self.tile_image, (DIFFICULTY[self.difficulty][3][0], DIFFICULTY[self.difficulty][3][1]))

    # Load Bomb image
    self.bomb_image = pygame.image.load(SKINS[self.skin_index][1] + "bomb.png").convert_alpha()
    self.bomb_image = pygame.transform.scale(self.bomb_image, (DIFFICULTY[self.difficulty][3][0], DIFFICULTY[self.difficulty][3][1]))

    # Load Tile image
    self.flag_image = pygame.image.load(SKINS[self.skin_index][1] + "flag.png").convert_alpha()
    self.flag_image = pygame.transform.scale(self.flag_image, (DIFFICULTY[self.difficulty][3][0], DIFFICULTY[self.difficulty][3][1]))

    # A list to send to tile class
    self.tile_image_list = [self.tile_image, self.bomb_image, self.flag_image]

  # What happens when we reset the game      
  def reset(self):
    # Timer logic
    self.start_time = 0
    self.current_time = 0
    self.elapsed_time = 0

    # If this is true, then a game is in progress
    # Stops the clocks if False
    self.game_in_progress = True

    # Makes the Game Class, which runs the game
    # rows, colums, bombs, [start x/y for gameboard]
    self.size = [DIFFICULTY[self.difficulty][0], DIFFICULTY[self.difficulty][1]]
    self.start_position = center_gameboard(self.size, self.difficulty)
    self.game = Game(self.size, DIFFICULTY[self.difficulty][2], self.start_position, self.tile_image_list, self.difficulty, self.skin_index)

    # Makes the two counter boxes at the top
    self.flag_y = (self.start_position[1]-40) / 2
    self.flag_display = Display(self.start_position[0], self.flag_y, 75, 40, self.skin_index)
    self.timer_display = Display(DIFFICULTY[self.difficulty][5][0]-self.start_position[0]-75, self.flag_y, 75, 40, self.skin_index)

    # Makes reset btn
    self.reset_btn = make_reset_btn(self.difficulty, self.skin_index)

  # Changes size of Screen
  def change_screen_size(self, w, h):
    self.screen = pygame.display.set_mode((w, h)) 






# App-logic
if __name__ == '__main__':
  while True:
    app = App()
    app.run()

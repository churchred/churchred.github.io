
# Import pygame reletated things
import pygame, time, random
pygame.init()
pygame.font.init()

# Import other python scripts
from __scripts__.settings import *  
from __scripts__.tiles import Tiles

class Game():
  def __init__(self, size, bombs, placement, images, diff, skin):

    # Game variables
    self.game_board = []              # The game board we use (will be built later)
    self.rows = size[0]               # How many rows in the game
    self.colums = size[1]             # How many colums in each row
    self.bombs = bombs                # How many bombs
    self.flags = 0                    # How many flags have been placed
    self.game_over = False            # Wether or not we can still play
    self.start_xy = placement         # x/y where the board starts
    self.tiles_left = size[0]*size[1] # If this is the same as number of bombs, you WIN
    self.started = False
    self.lost = False

    self.image_list = images   # A list of images we need for Tiles
    self.difficulty = diff     # Current difficulty
    self.skin_index = skin     # Which skin we are using

    # Making the victory text and getting it's size
    self.myfont = pygame.font.SysFont("Arial", 40)
    self.text_element = self.myfont.render("Congratulations!", 1, (BLACK))
    self.text_width, self.text_height = self.text_element.get_width(), self.text_element.get_height()

    # Makes the game board
    self.make_board()

    # Places the bombs randomly onto the board
    self.place_bombs()

    # Find the numbers around each bomb
    self.find_numbers()

    # Prints the board onto the consol with colors
    self.print_board()

    # Makes the buttons to print on screen
    self.make_buttons()


  # Makes the the right number of rows and colums in the game_board
  def make_board(self):

    # Makes a list with a value(bomb or empty(0)) and colum index. (form 0 to rows*colums)
    counter = 1
    for rows in range(self.rows):
      temp_cols = []
      for colums in range(self.colums):
        temp_cols.append([0, counter])
        counter += 1
      self.game_board.append(temp_cols)
    
  # Places the bombs
  def place_bombs(self):

    # Size of the gameboard
    game_board_size = self.rows*self.colums

    # List we will fill with bomb locations
    temp_bomb_list = []

    # Makes a list with bombs and their index location on the gameboard
    for i in range(self.bombs):
      random_location = random.choice([i for i in range(0, game_board_size) if i not in temp_bomb_list])
      temp_bomb_list.append(random_location)
      
    # Adds the bombs from the list onto the gameboard
    for row in self.game_board:
      for colum in row:
        if colum[1] in temp_bomb_list:
          colum[0] = "X"

  # Makes the numbers on the screen, around the bombs    
  def find_numbers(self):
    for r_index, row in enumerate(self.game_board):
      for c_index, colum in enumerate(row):
        if colum[0] == "X":

          # Check the tiles above the bomb
          if r_index != 0:

            # check directly above
            if self.game_board[r_index-1][c_index][0] != "X": 
              self.game_board[r_index-1][c_index][0] += 1
            
            # Check to the top-left
            if c_index != 0:
              if self.game_board[r_index-1][c_index-1][0] != "X": 
                self.game_board[r_index-1][c_index-1][0] += 1

            # Check to the top-right
            if c_index != self.colums-1:
              if self.game_board[r_index-1][c_index+1][0] != "X": 
                self.game_board[r_index-1][c_index+1][0] += 1
              
          # Check on either side of bomb
          if c_index != 0:
            if self.game_board[r_index][c_index-1][0] != "X": 
              self.game_board[r_index][c_index-1][0] += 1
          if c_index != self.colums-1:
            if self.game_board[r_index][c_index+1][0] != "X": 
              self.game_board[r_index][c_index+1][0] += 1

          # Check the tiles below the bomb
          if r_index != self.rows-1:

            # check directly below
            if self.game_board[r_index+1][c_index][0] != "X": 
              self.game_board[r_index+1][c_index][0] += 1
            
            # Check to the bottom-left
            if c_index != 0:
              if self.game_board[r_index+1][c_index-1][0] != "X": 
                self.game_board[r_index+1][c_index-1][0] += 1

            # Check to the bottom-right
            if c_index != self.colums-1:
              if self.game_board[r_index+1][c_index+1][0] != "X": 
                self.game_board[r_index+1][c_index+1][0] += 1

  # Makes the buttons we are going to print onto the screen      
  def make_buttons(self):

    # Get button size, different difficulties have different sizes
    btn_size = DIFFICULTY[self.difficulty][3][0]

    # Space between buttons, in other words, width of a line in the grid between buttons
    btn_space = BTN_SPACE
    
    for r_index, row in enumerate(self.game_board):
      for c_index, colum in enumerate(row):

        # Checks if it is a bomb or not
        if colum[0] == "X":
          txt_col = RED
        else:
          txt_col = NUMB_COLORS[0][colum[0]-1]
        
        # Checks if it is blank space or not
        if colum[0] == 0:
          txt = ""
        else:
          txt = str(colum[0])

        # Makes the Tile-button
        btn = Tiles(
          (btn_size+btn_space)*c_index+self.start_xy[0],  # x, 
          (btn_size+btn_space)*r_index+self.start_xy[1],  # y,
          btn_size, btn_size,                             # w, h,
          SKINS[self.skin_index][3],                      # color, 
          "Arial", 30, txt_col, txt_col,                  # font, font_size, font_color, font_color_hover,
          txt, colum[1], self.image_list, self.skin_index # id(name_txt), index, skin, skin_index
        )
        colum.append(btn)     
               
  # Runs the app
  def run(self, screen, mouse):

    # A package with info to send back to main file. 
    # Hovering, clicked, gameover
    package_to_main = [False, None, False]

    # Draws the background behind all the buttons, and is slightly bigger to make it seem like a frame
    pygame.draw.rect(screen, SKINS[self.skin_index][5], (self.start_xy[0]-2, self.start_xy[1]-2, DIFFICULTY[self.difficulty][4][0]+4, DIFFICULTY[self.difficulty][4][1]+4))

    # If the number of tiles left is equal to number of bombs, then we win.
    if self.tiles_left <= self.bombs:
      self.game_over = True
    
    # Goes through the entire game board and draws the buttons and their logic
    for r_index, row in enumerate(self.game_board):
      for c_index, colum in enumerate(row):
        packet_from_btn = colum[2].draw(screen, mouse, self.game_over)
        
        # This only happens as long as we are still playing the game(wont happen when we win/lose)
        if self.game_over == False:

          # Do we hover the cursor?
          if packet_from_btn[0] == True:
            package_to_main[0] = True

          # Do we flag it/right click?
          if packet_from_btn[2] == "Right" and colum[2].hidden == True:
            if colum[2].flagged == False and self.flags < self.bombs:
              colum[2].flagged = True
              self.flags += 1
            elif colum[2].flagged == True:
              colum[2].flagged = False
              self.flags -= 1
    
          elif packet_from_btn[1] != None and colum[2].flagged == False:
            colum[2].hidden = False
            self.started = True
            self.tiles_left -= 1
            if colum[0] == "X":
              colum[2].color = SKINS[self.skin_index][6]
              self.game_over = True
              self.lost = True
              self.show_bombs()
          
            elif packet_from_btn[1] == "":
              self.clear_empty_spaces(r_index, c_index)
            print("Tiles: " + str(self.tiles_left) + "/" + str(self.bombs))


    # If we win, print text
    if self.tiles_left <= self.bombs and self.lost == False:
      self.victory(screen)


    package_to_main[1] = self.bombs - self.flags
    package_to_main[2] = self.game_over

    return package_to_main

  # Prints the board onto consol in an easy to read fashion
  def print_board(self):
    print("\n Game Board:")
    for row in self.game_board:
      temp_row = ""
      for colum in row:
        if colum[0] == "X":
          txt_col = RED_TXT
        else:
          if colum[0] == 0:
            txt_col = BLUE_TXT
          if colum[0] >= 1:
            txt_col = GREEN_TXT

        temp_row += txt_col + "[" + str(colum[0]) + "] " + RESET_TXT
      print(temp_row)
  

  # Checks all squares around a clicked button
  def clear_empty_spaces_checker(self, row, col):
    if self.game_board[row][col][2].hidden == True and self.game_board[row][col][0] != "X":
      self.game_board[row][col][2].hidden = False
      self.tiles_left -= 1

      if self.game_board[row][col][2].flagged == True:
        self.flags -= 1
      if self.game_board[row][col][0] == 0: 
        self.clear_empty_spaces(row, col)

  # Checks the area around the clicked item if we click empty tile.
  # Recursive algorithm
  def clear_empty_spaces(self, row, col):
    
    # Check top
    if row != 0:
      self.clear_empty_spaces_checker(row-1, col)
      if col != self.colums-1:
        self.clear_empty_spaces_checker(row-1, col+1)
      if col != 0:
        self.clear_empty_spaces_checker(row-1, col-1)

    # Check under
    if row != self.rows-1:
      self.clear_empty_spaces_checker(row+1, col)
      if col != self.colums-1:
        self.clear_empty_spaces_checker(row+1, col+1)
      if col != 0:
        self.clear_empty_spaces_checker(row+1, col-1)
    
    # Check right
    if  col != self.colums-1:
      self.clear_empty_spaces_checker(row, col+1)

    # Check left
    if col != 0:
      self.clear_empty_spaces_checker(row, col-1)

  # Runs if we click a bomb. Reveals all other bombs
  def show_bombs(self):
    for r_index, row in enumerate(self.game_board):
      for c_index, colum in enumerate(row):
        if colum[0] == "X":
          colum[2].hidden = False

  # What happen when you win    
  def victory(self, screen):
    return
    rect_w = 250
    rect_h = 75
    border_w = 5
    pygame.draw.rect(screen, BLACK, ((DIFFICULTY[self.difficulty][5][0]/2-rect_w/2)-border_w, (DIFFICULTY[self.difficulty][5][1]/2-rect_h/2)-border_w, rect_w+border_w*2, rect_h+border_w*2))
    pygame.draw.rect(screen, SKINS[self.skin_index][2][0], (DIFFICULTY[self.difficulty][5][0]/2-rect_w/2, DIFFICULTY[self.difficulty][5][1]/2-rect_h/2, rect_w, rect_h))
    screen.blit(self.text_element, (DIFFICULTY[self.difficulty][5][0]/2-self.text_width/2, DIFFICULTY[self.difficulty][5][1]/2-self.text_height/2))


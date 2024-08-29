from __scripts__.colors import *


#     ||||||  ||||||  ||||||  ||||||  ||   |||   ||  |||||||   ||||||
#     ||      ||        ||      ||    ||  || ||  ||  ||        ||
#     ||||||  ||||||    ||      ||    ||  ||  || ||  ||  |||   ||||||
#         ||  ||        ||      ||    ||  ||  || ||  ||   ||       ||
#     ||||||  ||||||    ||      ||    ||  ||   |||   |||||||   ||||||
#---------------------------------------------------------------------



# Difficulty info:
DIFFICULTY = [

# Rows, Colums, bombs, size of tiles, size of board, size of screen
  [9,     9,      10,   [40, 40],      [376, 376],    [430, 500]],
  [13,    13,     40,   [35, 35],      [479, 479],    [540, 600]],
  [16,    30,     99,   [30, 30],      [958, 510],    [1000, 630]],

]

# Basic info
FPS = 60
VERSION = "LastTech: Minesweeper    v0.9"

TITLE_WIDTH = 325
TITLE_HEIGHT = 350

# Space between buttons, which becomes the width of the lines in the grid
BTN_SPACE = 2


# Skins:
SKINS = [
  # Name,       Tile_img,         BG/MAIN BUTTONS,    Tile click,    Clock, BG, TEXT, BORDER,    TILE_BG,     BOMB_CLICK
  ['Normal',  'assets/skin_1/', [GRAY_LIGHT, GRAY],   GRAY_LIGHT,    [BLACK, RED, GRAY],          GRAY,       RED_LIGHT],
  ['Frozen',  'assets/skin_2/', [BLUE_LIGHT, BLUE],   GRAY_LIGHT,    [BLUE_LIGHT, BLACK, GRAY],   GRAY,       RED_LIGHT]
]

# Color of the numbers
NUMB_COLORS = [
  [(1,0,251,255), (1,127,1,255), (253,1,0,255), (1,0,127,255), (126,2,4,255), (6,126,124,255), (0,0,0,255), (128,128,128,255)]
]









"""
Global constants
"""

# Colors
BLACK    = (   0,   0,   0) 
GRAY     = ( 185, 185, 185)
WHITE    = ( 255, 255, 255) 
BLUE     = (   0,   0, 155)
PINK	 = ( 255,   0, 255)
RED      = ( 155,   0,   0)
L_RED    = ( 175,  20,  20)
GREEN    = (   0, 155,   0)
L_GREEN  = (  20, 175,  20)
L_BLUE   = (  20,  20, 175)
L_YELLOW = ( 175, 175,  20)
YELLOW   = ( 155, 155,   0)

O_SPEED = 2
PLAYER_SPEED = 9

# Character sheets
# Skunk
SKUNK_FOL = "../res/Sprite/Skunk"
SKUNK = "../res/Sprite/Skunk/spritesheet.png"
SKUNK_SELECT = (SKUNK, 30, 0, 30, 47)

# Beanie
BEANIE_FOL = "../res/Sprite/Beanie"
BEANIE = "../res/Sprite/Beanie/spritesheet.png"
BEANIE_SELECT = (BEANIE, 30, 0, 30, 47)

# Screen dimensions
SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480

# Phone pieces
PHONE_SCREEN = (188, 462, 18, 452, 274, 434)   # x left, x right, y top, y bottom, width, height
PHONE_BG = "../res/Phone/background.png"
PHONE_BACK = ("../res/Phone/return.png", 0, 20, 48, 20)
PHONE_FONT = "../res/Phone/nokiafc22.ttf"

# Buffer edges
RIGHT_BUFF = 500
LEFT_BUFF = -500

# Font letters

# Menu item dimensions
A1 = ARROW1 = ("../res/arrowknife.png", 0, 0, 7, 11)
A2 = KNIFE1 = ("../res/arrowknife.png", 7, 0, 18, 6)
A3 = KNIFE2 = ("../res/arrowknife.png", 7, 6, 22, 5)
TB1 = TEXTBOX1 = ("../res/textbox.png", 0, 0, 384, 46)
TB2 = TEXTBOX2 = ("../res/textbox.png", 0, 46, 384, 46)
TB3 = TEXTBOX3 = ("../res/textbox.png", 0, 92, 384, 46)

# Tile dimensions
T1 = CONCRETE = ("../res/fence.png", 144, 31, 40, 20)

# Wall dimensions
W1 = FENCE_LEFT = ("../res/fence.png", 0, 96, 15, 64)
W2 = FENCE_RIGHT = ("../res/fence.png", 81, 96, 15, 64)
W3 = FENCE_MIDDLE = ("../res/fence.png", 15, 96, 40, 64)
W4 = BARRIER_L = ("../res/fence.png", 195, 1, 15, 29)
W5 = BARRIER_R = ("../res/fence.png", 283, 1, 15, 29)
W6 = BARRIER_M = ("../res/fence.png", 211, 1, 71, 29)

# Object dimensions
O1 = VEND1 = ("../res/fence.png", 96, 0, 32, 55)
O2 = VEND2 = ("../res/fence.png", 96, 55, 24, 48)
O3 = CAT = ("../res/fence.png", 144, 51, 21, 11)
O4 = FLOWER1 = ("../res/fence.png", 129, 0, 30, 31)
O5 = FLOWER2 = ("../res/fence.png", 165, 8, 25, 22)
O6 = FLOWER3 = ("../res/fence.png", 159, 64, 31, 32)
O7 = TREE1 = ("../res/fence.png", 128, 31, 16, 44)
O8 = TREE2 = ("../res/fence.png", 204, 36, 21, 50)
O9 = TREE3 = ("../res/fence.png", 234, 36, 25, 50)
O10 = TREE4 = ("../res/fence.png", 263, 36, 25, 50)
O11 = BOX1 = ("../res/fence.png", 120, 75, 32, 32)
O12 = BOX2 = ("../res/fence.png", 126, 107, 30, 28)
O13 = BOX3 = ("../res/fence.png", 126, 135, 30, 32)
O14 = BOX4 = ("../res/fence.png", 190, 107, 30, 25)
O15 = BOX5 = ("../res/fence.png", 190, 139, 30, 25)
O16 = BASKET1 = ("../res/fence.png", 96, 107, 29, 25)
O17 = BASKET2 = ("../res/fence.png", 96, 139, 29, 25)
O18 = BASKET3 = ("../res/fence.png", 159, 103, 28, 32)
O19 = BASKET4 = ("../res/fence.png", 160, 135, 29, 32)
O20 = BASKET5 = ("../res/fence.png", 222, 106, 30, 26)
O21 = BASKET6 = ("../res/fence.png", 222, 138, 30, 26)
O22 = BASKET7 = ("../res/fence.png", 257, 107, 28, 25)
O23 = BASKET8 = ("../res/fence.png", 257, 139, 28, 25)

OBJ_RAND_LIST = [ O1, O2, O3, O4, O5, O6, O7, O8, O9,
				O10, O11, O12, O13, O14, O15, O16, O17,
				O18, O19, O20, O21, O22, O23 ]
				
# Music locations
M1 = Music1 = "../res/Phone/Tetris/tetrisb.mid"
M2 = Music2 = "../res/Phone/Tetris/tetrisc.mid"
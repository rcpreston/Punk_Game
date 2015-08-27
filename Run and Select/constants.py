"""
Global constants
"""

# Colors
BLACK    = (   0,   0,   0) 
WHITE    = ( 255, 255, 255) 
BLUE     = (   0,   0, 255)
PINK	 = ( 255,   0, 255)

O_SPEED = 2
PLAYER_SPEED = 9

# Character sheets
SKUNK = "skunksprite.png"
SKUNK_SELECT = ("skunksprite.png", 30, 0, 30, 47)
BEANIE = "beaniesprite.png"
BEANIE_SELECT = ("beaniesprite.png", 30, 0, 30, 47)

# Screen dimensions
SCREEN_WIDTH  = 384
SCREEN_HEIGHT = 148+45
FENCE_HEIGHT = 128
STUFF_HEIGHT = 135

# Buffer edges
RIGHT_BUFF = 500
LEFT_BUFF = -500

# Font letters

# Menu item dimensions
A1 = ARROW1 = ("arrowknife.png", 0, 0, 7, 11)
A2 = KNIFE1 = ("arrowknife.png", 7, 0, 18, 6)
A3 = KNIFE2 = ("arrowknife.png", 7, 6, 22, 5)
TB1 = TEXTBOX1 = ("textbox.png", 0, 0, 384, 46)
TB2 = TEXTBOX2 = ("textbox.png", 0, 46, 384, 46)
TB3 = TEXTBOX3 = ("textbox.png", 0, 92, 384, 46)

# Tile dimensions
T1 = CONCRETE = ("fence.png", 144, 31, 40, 20)

# Wall dimensions
W1 = FENCE_LEFT = ("fence.png", 0, 96, 15, 64)
W2 = FENCE_RIGHT = ("fence.png", 81, 96, 15, 64)
W3 = FENCE_MIDDLE = ("fence.png", 15, 96, 40, 64)
W4 = BARRIER_L = ("fence.png", 195, 1, 15, 29)
W5 = BARRIER_R = ("fence.png", 283, 1, 15, 29)
W6 = BARRIER_M = ("fence.png", 211, 1, 71, 29)

# Object dimensions
O1 = VEND1 = ("fence.png", 96, 0, 32, 55)
O2 = VEND2 = ("fence.png", 96, 55, 24, 48)
O3 = CAT = ("fence.png", 144, 51, 21, 11)
O4 = FLOWER1 = ("fence.png", 129, 0, 30, 31)
O5 = FLOWER2 = ("fence.png", 165, 8, 25, 22)
O6 = FLOWER3 = ("fence.png", 159, 64, 31, 32)
O7 = TREE1 = ("fence.png", 128, 31, 16, 44)
O8 = TREE2 = ("fence.png", 204, 36, 21, 50)
O9 = TREE3 = ("fence.png", 234, 36, 25, 50)
O10 = TREE4 = ("fence.png", 263, 36, 25, 50)
O11 = BOX1 = ("fence.png", 120, 75, 32, 32)
O12 = BOX2 = ("fence.png", 126, 107, 30, 28)
O13 = BOX3 = ("fence.png", 126, 135, 30, 32)
O14 = BOX4 = ("fence.png", 190, 107, 30, 25)
O15 = BOX5 = ("fence.png", 190, 139, 30, 25)
O16 = BASKET1 = ("fence.png", 96, 107, 29, 25)
O17 = BASKET2 = ("fence.png", 96, 139, 29, 25)
O18 = BASKET3 = ("fence.png", 159, 103, 28, 32)
O19 = BASKET4 = ("fence.png", 160, 135, 29, 32)
O20 = BASKET5 = ("fence.png", 222, 106, 30, 26)
O21 = BASKET6 = ("fence.png", 222, 138, 30, 26)
O22 = BASKET7 = ("fence.png", 257, 107, 28, 25)
O23 = BASKET8 = ("fence.png", 257, 139, 28, 25)

OBJ_RAND_LIST = [ O1, O2, O3, O4, O5, O6, O7, O8, O9,
				O10, O11, O12, O13, O14, O15, O16, O17,
				O18, O19, O20, O21, O22, O23 ]
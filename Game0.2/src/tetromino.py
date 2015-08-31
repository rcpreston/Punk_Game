# Tetromino (a Tetris clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, time, pygame, sys, constants
from pygame.locals import *

FPS = 25
BOXSIZE = 15
BOARDWIDTH = 10
BOARDHEIGHT = 28
BLANK = '.'

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

XMARGIN = constants.PHONE_SCREEN[0]+ 5
TOPMARGIN = constants.PHONE_SCREEN[2] + 10


BORDERCOLOR = constants.GRAY
BGCOLOR = constants.BLACK
TEXTCOLOR = constants.GRAY
TEXTSHADOWCOLOR = constants.GRAY
COLORS      = (     constants.BLUE,      constants.GREEN,      constants.RED,      constants.YELLOW)
LIGHTCOLORS = (constants.L_BLUE, constants.L_GREEN, constants.L_RED, constants.L_YELLOW)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

S_SHAPE_TEMPLATE = [['.....',
					 '.....',
					 '..OO.',
					 '.OO..',
					 '.....'],
					['.....',
					 '..O..',
					 '..OO.',
					 '...O.',
					 '.....']]

Z_SHAPE_TEMPLATE = [['.....',
					 '.....',
					 '.OO..',
					 '..OO.',
					 '.....'],
					['.....',
					 '..O..',
					 '.OO..',
					 '.O...',
					 '.....']]

I_SHAPE_TEMPLATE = [['..O..',
					 '..O..',
					 '..O..',
					 '..O..',
					 '.....'],
					['.....',
					 '.....',
					 'OOOO.',
					 '.....',
					 '.....']]

O_SHAPE_TEMPLATE = [['.....',
					 '.....',
					 '.OO..',
					 '.OO..',
					 '.....']]

J_SHAPE_TEMPLATE = [['.....',
					 '.O...',
					 '.OOO.',
					 '.....',
					 '.....'],
					['.....',
					 '..OO.',
					 '..O..',
					 '..O..',
					 '.....'],
					['.....',
					 '.....',
					 '.OOO.',
					 '...O.',
					 '.....'],
					['.....',
					 '..O..',
					 '..O..',
					 '.OO..',
					 '.....']]

L_SHAPE_TEMPLATE = [['.....',
					 '...O.',
					 '.OOO.',
					 '.....',
					 '.....'],
					['.....',
					 '..O..',
					 '..O..',
					 '..OO.',
					 '.....'],
					['.....',
					 '.....',
					 '.OOO.',
					 '.O...',
					 '.....'],
					['.....',
					 '.OO..',
					 '..O..',
					 '..O..',
					 '.....']]

T_SHAPE_TEMPLATE = [['.....',
					 '..O..',
					 '.OOO.',
					 '.....',
					 '.....'],
					['.....',
					 '..O..',
					 '..OO.',
					 '..O..',
					 '.....'],
					['.....',
					 '.....',
					 '.OOO.',
					 '..O..',
					 '.....'],
					['.....',
					 '..O..',
					 '.OO..',
					 '..O..',
					 '.....']]

PIECES = {'S': S_SHAPE_TEMPLATE,
		  'Z': Z_SHAPE_TEMPLATE,
		  'J': J_SHAPE_TEMPLATE,
		  'L': L_SHAPE_TEMPLATE,
		  'I': I_SHAPE_TEMPLATE,
		  'O': O_SHAPE_TEMPLATE,
		  'T': T_SHAPE_TEMPLATE}


def runTetris():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	BASICFONT = pygame.font.Font(constants.PHONE_FONT, 18)
	BIGFONT = pygame.font.Font(constants.PHONE_FONT, 100)

	showTextScreen('Tetromino')
	done = False
	# game loop
	if random.randint(0, 1) == 0:
		pygame.mixer.music.load(constants.M1)
	else:
		pygame.mixer.music.load(constants.M2)
	pygame.mixer.music.play(-1, 0.0)
	# setup variables for the start of the game
	board = getBlankBoard()
	lastMoveDownTime = time.time()
	lastMoveSidewaysTime = time.time()
	lastFallTime = time.time()
	movingDown = False # note: there is no movingUp variable
	movingLeft = False
	movingRight = False
	score = 0
	level, fallFreq = calculateLevelAndFallFreq(score)

	fallingPiece = getNewPiece()
	nextPiece = getNewPiece()

	while not done: # game loop
		if fallingPiece == None:
			# No falling piece in play, so start a new piece at the top
			fallingPiece = nextPiece
			nextPiece = getNewPiece()
			lastFallTime = time.time() # reset lastFallTime

			if not isValidPosition(board, fallingPiece):
				return # can't fit a new piece on the board, so game over

		checkForQuit()
		for event in pygame.event.get(): # event handling loop
			if event.type == KEYUP:
				if (event.key == K_p):
					# Pausing the game
					DISPLAYSURF.fill(BGCOLOR)
					pygame.mixer.music.stop()
					showTextScreen('Paused') # pause until a key press
					pygame.mixer.music.play(-1, 0.0)
					lastFallTime = time.time()
					lastMoveDownTime = time.time()
					lastMoveSidewaysTime = time.time()
				elif (event.key == K_LEFT or event.key == K_a):
					movingLeft = False
				elif (event.key == K_RIGHT or event.key == K_d):
					movingRight = False
				elif (event.key == K_DOWN or event.key == K_s):
					movingDown = False

			elif event.type == KEYDOWN:
				# moving the piece sideways
				if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, fallingPiece, adjX=-1):
					fallingPiece['x'] -= 1
					movingLeft = True
					movingRight = False
					lastMoveSidewaysTime = time.time()

				elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=1):
					fallingPiece['x'] += 1
					movingRight = True
					movingLeft = False
					lastMoveSidewaysTime = time.time()

				# rotating the piece (if there is room to rotate)
				elif (event.key == K_UP or event.key == K_w):
					fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
					if not isValidPosition(board, fallingPiece):
						fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
				elif (event.key == K_q): # rotate the other direction
					fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
					if not isValidPosition(board, fallingPiece):
						fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])

				# making the piece fall faster with the down key
				elif (event.key == K_DOWN or event.key == K_s):
					movingDown = True
					if isValidPosition(board, fallingPiece, adjY=1):
						fallingPiece['y'] += 1
					lastMoveDownTime = time.time()

				# move the current piece all the way down
				elif event.key == K_SPACE:
					movingDown = False
					movingLeft = False
					movingRight = False
					for i in range(1, BOARDHEIGHT):
						if not isValidPosition(board, fallingPiece, adjY=i):
							break
					fallingPiece['y'] += i - 1

		# handle moving the piece because of user input
		if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
			if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
				fallingPiece['x'] -= 1
			elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
				fallingPiece['x'] += 1
			lastMoveSidewaysTime = time.time()

		if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
			fallingPiece['y'] += 1
			lastMoveDownTime = time.time()

		# let the piece fall if it is time to fall
		if time.time() - lastFallTime > fallFreq:
			# see if the piece has landed
			if not isValidPosition(board, fallingPiece, adjY=1):
				# falling piece has landed, set it on the board
				addToBoard(board, fallingPiece)
				score += removeCompleteLines(board)
				level, fallFreq = calculateLevelAndFallFreq(score)
				fallingPiece = None
			else:
				# piece did not land, just move the piece down
				fallingPiece['y'] += 1
				lastFallTime = time.time()

		# drawing everything on the screen
		DISPLAYSURF.fill(BGCOLOR)
		DISPLAYSURF.blit(pygame.image.load(constants.PHONE_BG),(0,0))
		drawBoard(board)
		drawStatus(score, level)
		drawNextPiece(nextPiece)
		if fallingPiece != None:
			drawPiece(fallingPiece)

		pygame.display.update()
		FPSCLOCK.tick(FPS)
	pygame.mixer.music.stop()
	showTextScreen('Game Over')


def makeTextObjs(text, font, color):
	surf = font.render(text, True, color)
	return surf, surf.get_rect()


def terminate():
	pygame.quit()
	sys.exit()


def checkForKeyPress():
	# Go through event queue looking for a KEYUP event.
	# Grab KEYDOWN events to remove them from the event queue.
	checkForQuit()

	for event in pygame.event.get([KEYDOWN, KEYUP]):
		if event.type == KEYDOWN:
			continue
		return event.key
	return None


def showTextScreen(text):
	# This function displays large text in the
	# center of the screen until a key is pressed.
	# Draw the text drop shadow
	titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
	titleRect.center = (int(constants.SCREEN_WIDTH / 2), int(constants.SCREEN_HEIGHT / 2))
	DISPLAYSURF.blit(titleSurf, titleRect)

	# Draw the text
	titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
	titleRect.center = (int(constants.SCREEN_WIDTH / 2) - 3, int(constants.SCREEN_HEIGHT / 2) - 3)
	DISPLAYSURF.blit(titleSurf, titleRect)

	# Draw the additional "Press a key to play." text.
	pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
	pressKeyRect.center = (int(constants.SCREEN_WIDTH / 2), int(constants.SCREEN_HEIGHT / 2) + 100)
	DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

	while checkForKeyPress() == None:
		pygame.display.update()
		FPSCLOCK.tick()


def checkForQuit():
	for event in pygame.event.get(QUIT): # get all the QUIT events
		terminate() # terminate if any QUIT events are present
	for event in pygame.event.get(KEYUP): # get all the KEYUP events
		if event.key == K_ESCAPE:
			terminate() # terminate if the KEYUP event was for the Esc key
		pygame.event.post(event) # put the other KEYUP event objects back


def calculateLevelAndFallFreq(score):
	# Based on the score, return the level the player is on and
	# how many seconds pass until a falling piece falls one space.
	level = int(score / 10) + 1
	fallFreq = 0.27 - (level * 0.02)
	return level, fallFreq

def getNewPiece():
	# return a random new piece in a random rotation and color
	shape = random.choice(list(PIECES.keys()))
	newPiece = {'shape': shape,
				'rotation': random.randint(0, len(PIECES[shape]) - 1),
				'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
				'y': -2, # start it above the board (i.e. less than 0)
				'color': random.randint(0, len(COLORS)-1)}
	return newPiece


def addToBoard(board, piece):
	# fill in the board based on piece's location, shape, and rotation
	for x in range(TEMPLATEWIDTH):
		for y in range(TEMPLATEHEIGHT):
			if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
				board[x + piece['x']][y + piece['y']] = piece['color']


def getBlankBoard():
	# create and return a new blank board data structure
	board = []
	for i in range(BOARDWIDTH):
		board.append([BLANK] * BOARDHEIGHT)
	return board


def isOnBoard(x, y):
	return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT


def isValidPosition(board, piece, adjX=0, adjY=0):
	# Return True if the piece is within the board and not colliding
	for x in range(TEMPLATEWIDTH):
		for y in range(TEMPLATEHEIGHT):
			isAboveBoard = y + piece['y'] + adjY < 0
			if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
				continue
			if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
				return False
			if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
				return False
	return True

def isCompleteLine(board, y):
	# Return True if the line filled with boxes with no gaps.
	for x in range(BOARDWIDTH):
		if board[x][y] == BLANK:
			return False
	return True


def removeCompleteLines(board):
	# Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
	numLinesRemoved = 0
	y = BOARDHEIGHT - 1 # start y at the bottom of the board
	while y >= 0:
		if isCompleteLine(board, y):
			# Remove the line and pull boxes down by one line.
			for pullDownY in range(y, 0, -1):
				for x in range(BOARDWIDTH):
					board[x][pullDownY] = board[x][pullDownY-1]
			# Set very top line to blank.
			for x in range(BOARDWIDTH):
				board[x][0] = BLANK
			numLinesRemoved += 1
			# Note on the next iteration of the loop, y is the same.
			# This is so that if the line that was pulled down is also
			# complete, it will be removed.
		else:
			y -= 1 # move on to check next row up
	return numLinesRemoved


def convertToPixelCoords(boxx, boxy):
	# Convert the given xy coordinates of the board to xy
	# coordinates of the location on the screen.
	return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))


def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
	# draw a single box (each tetromino piece has four boxes)
	# at xy coordinates on the board. Or, if pixelx & pixely
	# are specified, draw to the pixel coordinates stored in
	# pixelx & pixely (this is used for the "Next" piece).
	if color == BLANK:
		return
	if pixelx == None and pixely == None:
		pixelx, pixely = convertToPixelCoords(boxx, boxy)
	pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
	pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))


def drawBoard(board):
	# draw the border around the board
	pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 2, TOPMARGIN - 5, (BOARDWIDTH * BOXSIZE) + 6, (BOARDHEIGHT * BOXSIZE) + 6), 5)

	# fill the background of the board
	pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
	# draw the individual boxes on the board
	for x in range(BOARDWIDTH):
		for y in range(BOARDHEIGHT):
			drawBox(x, y, board[x][y])


def drawStatus(score, level):
	# draw the score text
	scoreSurf = BASICFONT.render('Score: %s' % score, True, TEXTCOLOR)
	scoreRect = scoreSurf.get_rect()
	scoreRect.topleft = (constants.PHONE_SCREEN[0] + 180, 20)
	DISPLAYSURF.blit(scoreSurf, scoreRect)

	# draw the level text
	levelSurf = BASICFONT.render('Level: %s' % level, True, TEXTCOLOR)
	levelRect = levelSurf.get_rect()
	levelRect.topleft = (constants.PHONE_SCREEN[0] + 180, 50)
	DISPLAYSURF.blit(levelSurf, levelRect)


def drawPiece(piece, pixelx=None, pixely=None):
	shapeToDraw = PIECES[piece['shape']][piece['rotation']]
	if pixelx == None and pixely == None:
		# if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
		pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])

	# draw each of the boxes that make up the piece
	for x in range(TEMPLATEWIDTH):
		for y in range(TEMPLATEHEIGHT):
			if shapeToDraw[y][x] != BLANK:
				drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))


def drawNextPiece(piece):
	# draw the "next" text
	nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
	nextRect = nextSurf.get_rect()
	nextRect.topleft = (constants.PHONE_SCREEN[0] + 180, 80)
	DISPLAYSURF.blit(nextSurf, nextRect)
	# draw the "next" piece
	drawPiece(piece, pixelx=constants.PHONE_SCREEN[0]+180, pixely=100)

def restart(game_surface):
	"""
	Display a GAME OVER screen and return True if a new game should be
	started or False if the user wants to quit.
	"""
	# Clear the background.
	game_surface.fill(BACKGROUND_COLOR)
	game_surface.blit(pygame.image.load(constants.PHONE_BG),(0,0))

	# Draw the game over message.
	text = 'GAME OVER'
	font = pygame.font.Font(constants.PHONE_FONT, 30)
	line = font.render(text, True, constants.BLACK)

	x_center = constants.PHONE_SCREEN[1] - (constants.PHONE_SCREEN[1]-constants.PHONE_SCREEN[0])/2
	x_center += -(line.get_width() / 2)
	y_center = constants.PHONE_SCREEN[3] - (constants.PHONE_SCREEN[3]-constants.PHONE_SCREEN[2])/2
	y_center+= -(line.get_height() / 2)
	
	game_surface.blit(line, line.get_rect().move((x_center, y_center)))
	
	y_center += line.get_height()/2
	
	text = 'Press SPACE to restart'
	font = pygame.font.Font(constants.PHONE_FONT,12)
	line = font.render(text,True,constants.BLACK)
	
	x_center = constants.PHONE_SCREEN[1] - (constants.PHONE_SCREEN[1]-constants.PHONE_SCREEN[0])/2
	x_center += -(line.get_width() / 2)
	y_center = y_center + line.get_height()
	
	game_surface.blit(line, line.get_rect().move((x_center, y_center)))
	text = 'Press Q to quit'
	font = pygame.font.Font(constants.PHONE_FONT,12)
	line = font.render(text,True,constants.BLACK)
	
	x_center = constants.PHONE_SCREEN[1] - (constants.PHONE_SCREEN[1]-constants.PHONE_SCREEN[0])/2
	x_center += -(line.get_width() / 2)
	y_center = y_center + line.get_height()
	
	game_surface.blit(line, line.get_rect().move((x_center, y_center)))
	
	
	pygame.display.update()

	# Wait for the user to either restart or quit.
	while True:
		####
		# TODO:
		# Handle the 3 key presses we care about for determining
		# whether to restart or quite the game:
		# 1. QUIT (quit, caused by closing the game window)
		# 2. ESCAPE (quit)
		# 3. SPACE (restart)
		####
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				# The user closed the window.
				pygame.key.set_repeat()
				return False
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_q:
					pygame.key.set_repeat()
					return False
				elif e.key == pygame.K_SPACE:
					runTetris()

if __name__ == '__main__':
	runTetris()
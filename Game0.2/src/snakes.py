import pygame
import random
import constants

BACKGROUND_COLOR = (constants.BLACK)
FRAMERATE = 60
ARROW_KEYS = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

class Food(object):
	FOOD_UNIT = 5

	def __init__(self, game_surface):
		"""
		A piece of snake food.
		"""
		game_rect = game_surface.get_rect()
		self.surface = pygame.Surface((self.FOOD_UNIT, self.FOOD_UNIT))

		# Give the food piece a random, solid RGB color.
		r = random.randint(0x00, 0xFF)
		g = random.randint(0x00, 0xFF)
		b = random.randint(0x00, 0xFF)
		self.surface.fill((r, g, b))

		# Place the food piece randomly on the screen.
		self.pos = [random.randint(constants.PHONE_SCREEN[0], constants.PHONE_SCREEN[1]-6),
					random.randint(constants.PHONE_SCREEN[2], constants.PHONE_SCREEN[3]-6)]
		self.surface.scroll(self.pos[0], self.pos[1])
		game_surface.blit(self.surface, self.surface.get_rect())


	def update(self, game_surface):
		"""
		Redraw the food.
		"""
		rect = self.surface.get_rect().move(self.pos)
		game_surface.blit(self.surface, rect)


	def get_rect(self):
		return self.surface.get_rect().move(self.pos)


class Snake(object):
	SNAKE_UNIT = 10
	SEGMENT_SIZE = (SNAKE_UNIT, SNAKE_UNIT)

	def __init__(self, color, pos=[0, 0]):
		"""
		A snake. It has a head and body and can move.
		"""
		# create the head
		head_surface = pygame.Surface(self.SEGMENT_SIZE)
		head_surface.fill(color)
		self._head = {'surface': head_surface,'pos': pos}
		self._segments = []

		# The body color is the inverse of the head color.
		self.color = 255- color[0], 255 - color[1], 255 - color[2]


	def _add_segment(self, pos):
		"""
		Add a segment to the body of the snake.
		"""
		segment = pygame.Surface(self.SEGMENT_SIZE)
		segment.fill(self.color)
		segment.scroll(pos[0], pos[1])
		self._segments.append({'surface': segment,'pos': pos})


	def _get_rect(self, segment):
		rect = segment['surface'].get_rect()
		rect.move_ip(segment['pos'])
		return rect


	def _redraw_segment(self, segment, game_surface):
		rect = self._get_rect(segment)
		game_surface.blit(segment['surface'], rect)


	def get_rects(self):
		"""
		Return the rectangles that make up the head and body of the
		snake.
		"""
		for segment in [self._head] + self._segments:
			rect = self._get_rect(segment)
			yield rect


	def head_hit_body(self):
		"""
		Return True if the head hit the body.
		"""
		head_rect = self._get_rect(self._head)
		for segment in self._segments:
			segment_rect = self._get_rect(segment)
			if (head_rect.colliderect(segment_rect)):
				return True

		return False


	def update(self, game_surface):
		"""
		Draw the snake onto the game surface.
		"""
		self._redraw_segment(self._head, game_surface)

		for segment in self._segments:
			self._redraw_segment(segment, game_surface)


	def move(self, key, game_surface):
		"""
		Move the snake.
		"""

		# Move the position of the head based on the provided keypress.
		old_head_pos = self._head['pos'][:]
		head_x, head_y = old_head_pos
		if (key == pygame.K_UP):
			head_y = head_y - self.SNAKE_UNIT
		elif (key == pygame.K_DOWN):
			head_y = head_y + self.SNAKE_UNIT
		###
		# TODO:
		# Handle the remaining movement keys (as defined in ARROW_KEYS
		# in snakes.py).
		###
		elif key == pygame.K_LEFT:
			head_x = head_x - self.SNAKE_UNIT
		elif key == pygame.K_RIGHT:
			head_x = head_x + self.SNAKE_UNIT
		else:
			return

		# Don't actually move if that would put the head outside the
		# bounds of the screen.
		head_rect = self._head['surface'].get_rect()
		max_x = constants.PHONE_SCREEN[1] - head_rect.width
		min_x = constants.PHONE_SCREEN[0]
		max_y = constants.PHONE_SCREEN[3] - head_rect.height
		min_y = constants.PHONE_SCREEN[2]
		if (head_x < min_x or head_x > max_x or
			head_y < min_y or head_y > max_y):
			return

		# Don't actually move if the head would be moving backwards
		# into the body.
		if len(self._segments) > 0:
			first_segment = self._segments[0]['surface'].get_rect().move(
				self._segments[0]['pos'])
			if head_rect.move(old_head_pos).colliderect(first_segment):
				return

		# Update the head on the screen.
		self._head['pos'] = (head_x, head_y)
		self._redraw_segment(self._head, game_surface)

		# Update the body segments on the screen.
		old_segment_pos = old_head_pos
		for segment in self._segments:
			saved_pos = segment['pos'][:]
			segment['pos'] = old_segment_pos
			self._redraw_segment(segment, game_surface)
			old_segment_pos = saved_pos

		return True


	def try_to_eat(self, food_items):
		"""
		Grow the snack by a segment for every food item it consumed.
		"""
		# Only the head can eat snacks.
		head_rect = self._get_rect(self._head)

		for f in food_items[:]:
			if head_rect.colliderect(f.get_rect()):
				food_items.remove(f)

				if self._segments:
					tail = self._segments[-1]
				else:
					tail = self._head

				x = tail['pos'][0]
				y = tail['pos'][1] + self.SNAKE_UNIT
				self._add_segment([x, y])

				

def initialize_screen():
	# Initialize the screen and game objects.
	pygame.init()
	pygame.display.set_caption('SNAKES - Press <Esc> to Quit, <Space> to Restart')
	####
	# TODO:
	# Set the key repeat speed (so that holding down an arrow key will
	# continue to move the snake).
	####
	pygame.key.set_repeat(10,10)

	return pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))


def move_bad_snake(bad_snake, game_surface, current_direction):
	bad_snake.move(current_direction, game_surface)

	if random.random() > .75:
		current_direction = random.choice(ARROW_KEYS)

	return current_direction


def detect_collisions(good_snake, bad_snake):
	"""
	Detect collisions between the Good Snake and the Bad Snake, and
	between the Good Snake and itself.

	Returns True if there's been a collision and False otherwise.
	"""
	for python_area in good_snake.get_rects():
		for bad_snake_area in bad_snake.get_rects():
			if python_area.colliderect(bad_snake_area):
				return True

	# detect collisions with ourself
	if good_snake.head_hit_body():
		return True

	return False


def create_food(food, game_surface):
	while len(food) < 5:
		food.append(Food(game_surface))

	return food


def play_snake():
	game_surface = initialize_screen()

	# Create our snake.
	good_snake = Snake(constants.WHITE,
					   [constants.PHONE_SCREEN[0]+5,
						constants.PHONE_SCREEN[2]+5])
	good_snake.update(game_surface)

	# Create the bad snake.
	bad_snake = Snake(constants.RED,
					  [constants.PHONE_SCREEN[1]-15,
					   constants.PHONE_SCREEN[3]-15])
	bad_snake.update(game_surface)
	bad_snake_direction = random.choice(ARROW_KEYS)

	snake_food = create_food([], game_surface)

	game_clock = pygame.time.Clock()
	while True:
		game_clock.tick(FRAMERATE)
		

		# Detect and respond to user keypresses.
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				return False
			elif e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					pygame.quit()
					return False
				elif e.key in ARROW_KEYS:
					good_snake.move(e.key, game_surface)

		# Move the bad snake.
		bad_snake_direction = move_bad_snake(bad_snake, game_surface,
											 bad_snake_direction)

		# Detect any collisions.
		if detect_collisions(good_snake, bad_snake):
			return restart(game_surface)

		# Have both snakes eat any available food.
		good_snake.try_to_eat(snake_food)
		bad_snake.try_to_eat(snake_food)

		# Refresh the food supply.
		snake_food = create_food(snake_food, game_surface)
		
		game_surface.fill(BACKGROUND_COLOR)
		game_surface.blit(pygame.image.load("../res/Phone/background.png"),(0,0))
		# Update the snake and food pixels.
		good_snake.update(game_surface)
		bad_snake.update(game_surface)
		for f in snake_food:
			f.update(game_surface)

		pygame.display.update()


def restart(game_surface):
	"""
	Display a GAME OVER screen and return True if a new game should be
	started or False if the user wants to quit.
	"""
	# Clear the background.
	game_surface.fill(BACKGROUND_COLOR)
	game_surface.blit(pygame.image.load("../res/Phone/background.png"),(0,0))

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
					play_snake()


if __name__ == '__main__':
	still_playing = True
	while still_playing:
		still_playing = play_snake()
	pygame.quit()
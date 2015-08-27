import pygame
import snakes
import tetromino
import constants
from object_class import Thing

"""
Open up the phone with a listing of options
Messages->
	Get text messages?
Notes->
	People
	Places
	Events
	Things
Personal->
	Stats
	Inventory
	IDK
Games->
	Tetris
	Snake
	Pong
"""

def open_phone():
	pygame.init()
	
	size= [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Punks R Us")
	
	
	choice = 1
	menu = PhoneMenu()
	done = False
	
	clock = pygame.time.Clock()
	
	while not done:
		
		# Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop
				return True
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if choice == 1:
						choice = menu.length()
					else:
						choice += -1
						
				if event.key == pygame.K_DOWN:
					if choice == menu.length():
						choice = 1
					else:
						choice += 1
						
				if event.key == pygame.K_RETURN:
					done = menu.selected(choice)
					choice = 1
		
		# Updates
		#menu.update(choice)
		
		# Draw call
		menu.draw(screen,choice)
		
		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
		
	
class PhoneMenu():

	options_list = None
	#font = pygame.font.Font(None,12)
	main_list = ("Personal", "Messages", "Notes", "Games")
	game_list = ("Tetris", "Snake", "Pong")
	stat_list = ("Strengths", "Items", "Preferences")
	note_list = ("People", "Places", "Terms", "Things")
	list_num = 0    # 0 = main, 1 = game, 2 = stat, 3 = note
	sprite_list = None
	
	
	def __init__(self):
	
		self.back_sprite = Thing(constants.PHONE_BACK)
		self.back_sprite.rect.x = constants.PHONE_SCREEN[0] + constants.PHONE_SCREEN[4]/2 - self.back_sprite.rect.width/2
		self.back_sprite.rect.y = constants.PHONE_SCREEN[3] - self.back_sprite.rect.height
		self.options_list = self.main_list
		self.sprite_list = pygame.sprite.Group()
		self.sprite_list.add(self.back_sprite)
	
	def draw_options(self,options,screen):
	
		item_height = round((constants.PHONE_SCREEN[5]-self.back_sprite.rect.height)/len(options))
		y_point = constants.PHONE_SCREEN[2] + 4
		
		font = pygame.font.Font(constants.PHONE_FONT,24)
		for option in options:
			text = str(option)
			line = font.render(text,True,constants.GRAY)
			x_point = constants.PHONE_SCREEN[1] - (constants.PHONE_SCREEN[1]-constants.PHONE_SCREEN[0])/2
			x_point += -(line.get_width() / 2)
			screen.blit(line, line.get_rect().move(x_point, y_point))
			y_point +=26 + 4
			pygame.draw.line(screen, constants.BLACK, (constants.PHONE_SCREEN[0],y_point), (constants.PHONE_SCREEN[1],y_point), 4)
			y_point += 4
		self.sprite_list.draw(screen)
	
	#def update(self, choice):
		# update the location of the selection rectangle
	
	def draw(self,screen,choice):
		# Draw the phone background
		screen.fill(constants.BLACK)
		screen.blit(pygame.image.load(constants.PHONE_BG),(0,0))
		
		# Draw the selection rectangle
		
		
		if choice != len(self.options_list)+1:
			rect_y = constants.PHONE_SCREEN[2]+35*(choice-1)
			size = (constants.PHONE_SCREEN[4],34)
		
		else:
			size = (constants.PHONE_SCREEN[4],22)
			rect_y = constants.PHONE_SCREEN[3]-22
		select_rec = pygame.Surface(size)
		select_rec.fill(constants.L_BLUE)
		screen.blit(select_rec,(constants.PHONE_SCREEN[0],rect_y))
		
		# Draw the text + back button
		self.draw_options(self.options_list,screen)
		
		
	def length(self):
		return len(self.options_list)+1
	
	def selected(self, choice):
		
		# Main Menu
		if self.list_num == 0:
			if choice == 1:
				# Call statistics list
				self.options_list = self.stat_list
				self.list_num = 2
				return False
			elif choice == 2:
				# Call messages screen
				return False
			elif choice == 3:
				# Call database list
				self.options_list = self.note_list
				self.list_num = 3
				return False
			elif choice == 4:
				# Call game list
				self.options_list = self.game_list
				self.list_num = 1
				return False
			elif choice == 5:
				# Quit phone menu
				return True
		
		# Game Menu
		elif self.list_num == 1:
			if choice == 1:
				# Run tetris game
				tetromino.runTetris()
				return False
			elif choice == 2:
				# Run snake game
				snakes.play_snake()
				return False
			elif choice == 3:
				# Run pong
				return False
			elif choice == 4:
				# Return to main menu
				self.options_list = self.main_list
				self.list_num = 0
				return False
				
		# Statistics Menu
		elif self.list_num == 2:
			if choice == 1:
				# Open stat page
				return False
			elif choice == 2:
				# Open inventory
				return False
			elif choice == 3:
				# Open preferences
				return False
			elif choice == 4:
				# Return to main menu
				self.options_list = self.main_list
				self.list_num = 0
				return False
		
		# Notes Menu
		elif self.list_num == 3:
			if choice == 1:
				# Open people database
				return False
			elif choice == 2:
				# Open place database
				return False
			elif choice == 3:
				# Open glossary
				return False
			elif choice == 4:
				# Open item database
				return False
			elif choice == 5:
				# Return to main menu
				self.options_list = self.main_list
				self.list_num = 0
				return False
				
if __name__ == "__main__":
	open_phone()
	pygame.quit()
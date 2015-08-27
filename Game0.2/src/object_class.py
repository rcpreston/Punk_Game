import pygame
import constants
from spritesheet_functions import SpriteSheet

class Thing(pygame.sprite.Sprite):
	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in
			an array of 5 numbers like what's defined at the top of this
			code. """
		pygame.sprite.Sprite.__init__(self)

		sprite_sheet = SpriteSheet(sprite_sheet_data[0])
		# Grab the image for this platform
		self.image = sprite_sheet.get_image(sprite_sheet_data[1],
											sprite_sheet_data[2],
											sprite_sheet_data[3],
											sprite_sheet_data[4])

		self.rect = self.image.get_rect()
		
	
		

class TextBox(pygame.sprite.Sprite):

	def __init__(self):
	
		pygame.sprite.Sprite.__init__(self)
	
		# Make an NPC text box
		self.npc_box = Thing(constants.TB3)
		npc_box.rect.x = constants.SCREEN_WIDTH/2+30
		npc_box.rect.y = constants.SCREEN_HEIGHT/2 - npc_box.rect.height/2
		
		# Make a Beanie text box
		self.beanie_box = Thing(constants.TB2)
		beanie_box.rect.x = constants.SCREEN_WIDTH/2-60
		beanie_box.rect.y = constants.SCREEN_HEIGHT/2 - beanie_box.rect.height/2
		
		# Make a Skunk text box
		self.skunk_box = Thing(constants.TB1)
		skunk_box.rect.x = constants.SCREEN_WIDTH/2+30
		skunk_box.rect.y = constants.SCREEN_HEIGHT/2 - skunk_box.rect.height/2
		
	def draw(self, screen, who):
		if who == 1:
			beanie_box.draw(screen)
		elif who == 2:
			skunk_box.draw(screen)
		elif who == 3:
			npc_box.draw(screen)
	
class NPC(pygame.sprite.Sprite):
	
	text_box = 0
	text_line = 0
	current_text = ""
	is_talk = False
	walk_l = []
	walk_r = []
	walk_u = []
	walk_d = []
	change_x = 0
	change_y = 0
	frame = 0
	pos = 0
	
	direction = "R"
	
	def __init__(self,folder_num):
		
		pygame.sprite.Sprite.__init__(self)
		
		self.folder = "../res/Sprite/Sprite"+str(folder_num)
		
		# Get spritesheet stuff
		sprite_sheet = SpriteSheet(self.folder+"spritesheet.png")
		# Down facing walk sequence
		image = sprite_sheet.get_image(0, 0, 30, 47)
		self.walk_d.append(image)
		image = sprite_sheet.get_image(30, 0, 30, 47)
		self.walk_d.append(image)
		image = sprite_sheet.get_image(60, 0, 30, 47)
		self.walk_d.append(image)
		image = sprite_sheet.get_image(90, 0, 30, 47)
		self.walk_d.append(image)
		
		# Left facing walk sequence
		image = sprite_sheet.get_image(0, 47, 30, 47)
		self.walk_l.append(image)
		image = sprite_sheet.get_image(30, 47, 30, 47)
		self.walk_l.append(image)
		image = sprite_sheet.get_image(60, 47, 30, 47)
		self.walk_l.append(image)
		image = sprite_sheet.get_image(90, 47, 30, 47)
		self.walk_l.append(image)
		
		# Right facing walk sequence
		image = sprite_sheet.get_image(0, 47, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.walk_r.append(image)
		image = sprite_sheet.get_image(30, 47, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.walk_r.append(image)
		image = sprite_sheet.get_image(60, 47, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.walk_r.append(image)
		image = sprite_sheet.get_image(90, 47, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.walk_r.append(image)
		
		# Up facing walk sequence
		image = sprite_sheet.get_image(0, 94, 30, 47)
		self.walk_u.append(image)
		image = sprite_sheet.get_image(30, 94, 30, 47)
		self.walk_u.append(image)
		image = sprite_sheet.get_image(60, 94, 30, 47)
		self.walk_u.append(image)
		image = sprite_sheet.get_image(90, 94, 30, 47)
		self.walk_u.append(image)
		
		# Set the image the player starts with
		self.image = self.walk_r[1]

		# Set a referance to the image rect.
		self.rect = self.image.get_rect()
		
		self.pos = self.rect.x
		
		
	def update(self):
		# Figure out walking and things???
		self.pos += self.change_x
		if self.direction == "R" and self.change_y == 0:
			if self.change_x == 1:
				frame = (self.pos // constants.PLAYER_SPEED) % len(walk.run_r)
				self.image = self.walk_r[frame]
			else:
				self.image = self.walk_r[1]
		elif self.direction == "L" and self.change_y == 0:
			if self.change_x == -1:
				frame = (self.pos // constants.PLAYER_SPEED) % len(self.walk_l)
				self.image = self.walk_l[frame]
			else:
				self.image = self.walk_l[1]
			
	# Player-controlled movement:
	def go_left(self):
		""" Called when the user hits the left arrow. """
		self.change_x = -1
		self.direction = "L"

	def go_right(self):
		""" Called when the user hits the right arrow. """
		self.change_x = 1
		self.direction = "R"

	def stop(self):
		self.change_x = 0
		self.change_y = 0

	def is_talk(self):
		return self.is_talk
		
	def current_text(self,player):
		return self.current_text
		
	def what_box(self):
		return self.text_box
	
	
class Item(pygame.sprite.Sprite):
	def __init__(self, sprite_sheet_data):
		pygame.sprite.Sprite.__init__(self)
		
		sprite_sheet = SpriteSheet(sprite_sheet_data[0])
		# Grab the image for this platform
		self.image = sprite_sheet.get_image(sprite_sheet_data[1],
											sprite_sheet_data[2],
											sprite_sheet_data[3],
											sprite_sheet_data[4])

		self.rect = self.image.get_rect()
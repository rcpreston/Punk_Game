import pygame
import constants
from spritesheet_functions import SpriteSheet,get_frames,animate_frame

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
	pos_x = 0
	pos_y = 0
	
	direction = "R"
	
	def __init__(self,folder_num):
		
		pygame.sprite.Sprite.__init__(self)
		
		self.folder = "../res/Sprite/Sprite"+str(folder_num)
		self.coll_box = Thing((self.folder+"/coll_box.png",0,0,30,5))
		
		# Get spritesheet stuff
		sprite_sheet = SpriteSheet(self.folder+"/spritesheet.png")
		# Down facing walk sequence
		self.walk_d = get_frames(self.folder+"/spritesheet.png",30,47,0,4,0)
		
		# Left facing walk sequence
		self.walk_l = get_frames(self.folder+"/spritesheet.png",30,47,0,4,47)
		
		# Right facing walk sequence
		self.walk_r = get_frames(self.folder+"/spritesheet.png",30,47,0,4,47,True)
		
		# Up facing walk sequence
		self.walk_u = get_frames(self.folder+"/spritesheet.png",30,47,0,4,94)
		
		# Set the image the player starts with
		self.image = self.walk_r[1]

		# Set a referance to the image rect.
		self.rect = self.image.get_rect()
		
		self.pos_x = self.rect.x
		self.pos_y = self.rect.y
		
		
	def update(self):
		# Figure out walking and things???
		self.pos_x += self.change_x
		self.pos_y += self.change_y
		if self.pos_y > 264-self.rect.height:
			if self.pos_y < 434-self.rect.height:
				self.rect.y += self.change_y
				self.coll_box.rect.y += self.change_y
				
		if self.direction == "R" and self.change_y == 0:
			if self.change_x == 1:
				frame = (self.pos_x // constants.PLAYER_SPEED) % len(self.walk_r)
				self.image = self.walk_r[frame]
			else:
				self.image = self.walk_r[1]
		elif self.direction == "L" and self.change_y == 0:
			if self.change_x == -1:
				frame = (self.pos_x // constants.PLAYER_SPEED) % len(self.walk_l)
				self.image = self.walk_l[frame]
			else:
				self.image = self.walk_l[1]
		elif self.direction == "U" and self.change_x == 0:
			if self.change_y != 0:
				frame = (self.pos_y // constants.PLAYER_SPEED) % len(self.walk_u)
				self.image = self.walk_u[frame]
			else:
				self.image = self.walk_u[1]
		elif self.direction == "D" and self.change_x == 0:
			if self.change_y != 0:
				frame = (self.pos_y // constants.PLAYER_SPEED) % len(self.walk_d)
				self.image = self.walk_d[frame]
			else:
				self.image = self.walk_d[1]
			
	# Player-controlled movement:
	def go_left(self):
		""" Called when the user hits the left arrow. """
		self.change_x = -1
		self.direction = "L"

	def go_right(self):
		""" Called when the user hits the right arrow. """
		self.change_x = 1
		self.direction = "R"

	def stop(self,dir):
		if dir == "R" or dir == "L":
			self.change_x = 0
		elif dir == "U" or dir == "D":
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
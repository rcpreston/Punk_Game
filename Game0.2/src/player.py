import pygame
import constants

from spritesheet_functions import SpriteSheet,get_frames
from object_class import Thing

class Player(pygame.sprite.Sprite):

	run_l = []
	run_r = []
	jump_l = []
	jump_r = []
	walk_d = []
	walk_r = []
	walk_l = []
	walk_u = []
	frame = 0
	pos_x = 0
	pos_y = 0
	change_x = 0
	change_y = 0
	
	direction = "R"
	

	def __init__(self, char_folder):

		pygame.sprite.Sprite.__init__(self)
		
		'''
		if character == constants.BEANIE:
			self.protagonist = 1
			self.coll_box = Thing((constants.BEANIE_FOL+"/coll_box.png",0,0,30,5))
		elif character == constants.SKUNK:
			self.protagonist = 2
			self.coll_box = Thing((constants.SKUNK_FOL+"/coll_box.png",0,0,30,5))
		'''
		self.protag_folder = char_folder
		self.coll_box = Thing((char_folder+"/coll_box.png",0,0,30,5))
		character = char_folder+"/spritesheet.png"
		
		# Down facing walk sequence
		self.walk_d = get_frames(character,30,47,0,4,0)
		
		# Left facing walk sequence
		self.walk_l = get_frames(character,30,47,0,4,47)
		
		# Right facing walk sequence
		self.walk_r = get_frames(character,30,47,0,4,47,True)
		
		# Up facing walk sequence
		self.walk_u = get_frames(character,30,47,0,4,94)
		
		# Left facing run sequence
		self.run_l = get_frames(character,30,47,0,6,141,False,True)
		'''
		image = sprite_sheet.get_image(150, 141, 30, 47)
		self.run_l.append(image)
		image = sprite_sheet.get_image(120, 141, 30, 47)
		self.run_l.append(image)
		image = sprite_sheet.get_image(90, 141, 30, 47)
		self.run_l.append(image)
		image = sprite_sheet.get_image(60, 141, 30, 47)
		self.run_l.append(image)
		image = sprite_sheet.get_image(30, 141, 30, 47)
		self.run_l.append(image)
		image = sprite_sheet.get_image(0, 141, 30, 47)
		self.run_l.append(image)
		'''

		# Right facing run sequence
		self.run_r = get_frames(character,30,47,0,6,141,True,True)
		'''
		image = sprite_sheet.get_image(0, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.run_r.append(image)
		image = sprite_sheet.get_image(30, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.run_r.append(image)
		image = sprite_sheet.get_image(60, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.run_r.append(image)
		image = sprite_sheet.get_image(90, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.run_r.append(image)
		image = sprite_sheet.get_image(120, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.run_r.append(image)
		image = sprite_sheet.get_image(150, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.run_r.append(image)
		'''
		
		
		# Left facing jump sequence
		self.jump_l = get_frames(character,30,47,180,3,141)
		'''
		image = sprite_sheet.get_image(180, 141, 30, 47)
		self.jump_l.append(image)
		image = sprite_sheet.get_image(210, 141, 30, 47)
		self.jump_l.append(image)
		image = sprite_sheet.get_image(240, 141, 30, 47)
		self.jump_l.append(image)
		'''
		
		# Right facing jump sequence
		self.jump_r = get_frames(character,30,47,180,3,141,True)
		'''
		image = sprite_sheet.get_image(180, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.jump_r.append(image)
		image = sprite_sheet.get_image(210, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.jump_r.append(image)
		image = sprite_sheet.get_image(240, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.jump_r.append(image)
		'''
		
		# Set the image the player starts with
		self.image = self.walk_r[1]

		# Set a referance to the image rect.
		self.rect = self.image.get_rect()
		self.rect.x = 320-self.rect.width/2
		self.rect.y = 240-self.rect.height/2
		
		self.pos_x = self.rect.x
		self.pos_y = self.rect.y
		self.coll_box.rect.x = self.pos_x
		self.coll_box.rect.y = self.pos_y+self.rect.height-5
		
	def update(self):
		
		self.pos_x += self.change_x
		self.pos_y += self.change_y
		if self.pos_y > 264-self.rect.height:
			if self.pos_y < 434-self.rect.height:
				self.rect.y += self.change_y
				self.coll_box.rect.y += self.change_y
				
		if self.direction == "R" and self.change_y == 0:
			if self.change_x == 1:
				frame = (self.pos_x // constants.PLAYER_SPEED) % len(self.run_r)
				self.image = self.run_r[frame]
			else:
				self.image = self.walk_r[1]
		elif self.direction == "L" and self.change_y == 0:
			if self.change_x == -1:
				frame = (self.pos_x // constants.PLAYER_SPEED) % len(self.run_l)
				self.image = self.run_l[frame]
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
		'''
			#do the diagonal movement with sprites
		elif self.change_x > 0 and self.change_y > 0:
			#We're going right and down
		elif self.change_x > 0 and self.change_y < 0:
			# We're going right and up
		elif self.change_x < 0 and self.change_y < 0:
			# We're going left and up
		elif self.change_x < 0 and self.change_y > 0:
			# We're going left and down
		'''
			
	# Player-controlled movement:
	def go_left(self):
		""" Called when the user hits the left arrow. """
		self.change_x = -1
		self.change_y = 0
		self.direction = "L"

	def go_right(self):
		""" Called when the user hits the right arrow. """
		self.change_x = 1
		self.change_y = 0
		self.direction = "R"
	
	def go_up(self):
		""" Called when user hits the up arrow. """
		self.change_y = -1
		self.change_x = 0
		self.direction = "U"
	
	def go_down(self):
		""" Called when user hits the down arrow. """
		self.change_y = 1
		self.change_x = 0
		self.direction = "D"
	
	def stop(self,dir):
		if dir == "R" or dir == "L":
			self.change_x = 0
		elif dir == "U" or dir == "D":
			self.change_y = 0
		
	def jump(self):
		""" Called when user hits the jump button. """
		self.change_y = 1
		
	def set_y(self,y):
		""" Set the player y position """
		self.rect.y = y
		self.pos_y = y
		self.coll_box.rect.y = self.pos_y+self.rect.height-5
		
	def set_x(self,x):
		""" Set the player x position """
		self.rect.x = x
		self.pos_x = x
		self.coll_box.rect.x = self.rect.x
	
	def who(self):
		return self.protagonist
	
	def facing(self):
		return self.direction
		
	def collide_up(self,wall):
		if self.direction == "U" and self.coll_box.rect.colliderect(wall.rect):
			self.coll_box.rect.top = wall.rect.bottom
			self.rect.top = self.coll_box.rect.top - self.rect.height +5
	def collide_down(self,wall):
		if self.direction == "D" and self.coll_box.rect.colliderect(wall.rect):
			self.coll_box.rect.bottom = wall.rect.top
			self.rect.bottom = self.coll_box.rect.bottom
	def collide_right(self,wall):
		if self.direction !="R":
			return (False,0)
		elif self.coll_box.rect.colliderect(wall.rect):
			x_shift = (self.coll_box.rect.right - wall.rect.left)
			return (True,x_shift)
		else:
			return (False,0)
	def collide_left(self,wall):
		if self.direction != "L":
			return (False,0)
		elif self.coll_box.rect.colliderect(wall.rect):
			x_shift = (self.coll_box.rect.left - wall.rect.right)
			return (True,x_shift)
		else:
			return (False,0)
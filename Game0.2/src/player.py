import pygame
import constants

from spritesheet_functions import SpriteSheet
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
	
	protagonist = 0
	

	def __init__(self, character):

		pygame.sprite.Sprite.__init__(self)
		
		# Load in the proper character
		sprite_sheet = SpriteSheet(character)
		
		if character == constants.BEANIE:
			self.protagonist = 1
			self.coll_box = Thing((constants.BEANIE_FOL+"/coll_box.png",0,0,30,5))
		elif character == constants.SKUNK:
			self.protagonist = 2
			self.coll_box = Thing((constants.SKUNK_FOL+"/coll_box.png",0,0,30,5))
		
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
		
		# Left facing run sequence
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

		# Right facing run sequence
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
		
		
		# Left facing jump sequence
		image = sprite_sheet.get_image(180, 141, 30, 47)
		self.jump_l.append(image)
		image = sprite_sheet.get_image(210, 141, 30, 47)
		self.jump_l.append(image)
		image = sprite_sheet.get_image(240, 141, 30, 47)
		self.jump_l.append(image)
		
		# Right facing jump sequence
		image = sprite_sheet.get_image(180, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.jump_r.append(image)
		image = sprite_sheet.get_image(210, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.jump_r.append(image)
		image = sprite_sheet.get_image(240, 141, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.jump_r.append(image)
		
		# Set the image the player starts with
		self.image = self.walk_r[1]

		# Set a referance to the image rect.
		self.rect = self.image.get_rect()
		
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
				
			
	# Player-controlled movement:
	def go_left(self):
		""" Called when the user hits the left arrow. """
		self.change_x = -1
		self.direction = "L"

	def go_right(self):
		""" Called when the user hits the right arrow. """
		self.change_x = 1
		self.direction = "R"
	
	def go_up(self):
		""" Called when user hits the up arrow. """
		self.change_y = -1
		self.direction = "U"
	
	def go_down(self):
		""" Called when user hits the down arrow. """
		self.change_y = 1
		self.direction = "D"
	
	def stop(self):
		self.change_x = 0
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
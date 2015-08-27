import pygame
import constants

from spritesheet_functions import SpriteSheet

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
	pos = 0
	change_x = 0
	change_y = 0
	
	direction = "R"
	
	level = None

	def __init__(self, character):

		pygame.sprite.Sprite.__init__(self)
		
		# Load in the proper character
		sprite_sheet = SpriteSheet(character)
		
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
		
		self.pos = self.rect.x
		
	def update(self):
		
		self.pos += self.change_x
		if self.direction == "R" and self.change_y == 0:
			if self.change_x == 1:
				frame = (self.pos // constants.PLAYER_SPEED) % len(self.run_r)
				self.image = self.run_r[frame]
			else:
				self.image = self.walk_r[1]
		elif self.direction == "L" and self.change_y == 0:
			if self.change_x == -1:
				frame = (self.pos // constants.PLAYER_SPEED) % len(self.run_l)
				self.image = self.run_l[frame]
			else:
				self.image = self.walk_l[1]
			"""
		elif self.change_y == 1:
			if self.direction == "R":
				self.image = self.jump_r[0]
			elif self.direction == "L":
				self.image = self.jump_l[0]
				"""
			
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
		
	def jump(self):
		""" Called when user hits the jump button. """
		self.change_y = 1
	

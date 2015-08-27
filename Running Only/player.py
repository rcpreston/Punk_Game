import pygame
import constants

from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):

	frames_l = []
	frames_r = []
	jump_l = []
	jump_r = []
	frame = 0
	pos = 0
	change_x = 0
	
	direction = "R"
	
	level = None

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)

		sprite_sheet = SpriteSheet("beaniesprite.png")
		# Load all the right facing images into a list
		image = sprite_sheet.get_image(150, 0, 30, 47)
		self.frames_l.append(image)
		image = sprite_sheet.get_image(120, 0, 30, 47)
		self.frames_l.append(image)
		image = sprite_sheet.get_image(90, 0, 30, 47)
		self.frames_l.append(image)
		image = sprite_sheet.get_image(60, 0, 30, 47)
		self.frames_l.append(image)
		image = sprite_sheet.get_image(30, 0, 30, 47)
		self.frames_l.append(image)
		image = sprite_sheet.get_image(0, 0, 30, 47)
		self.frames_l.append(image)

		# Load all the right facing images, then flip them
		# to face left.
		image = sprite_sheet.get_image(0, 0, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.frames_r.append(image)
		image = sprite_sheet.get_image(30, 0, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.frames_r.append(image)
		image = sprite_sheet.get_image(60, 0, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.frames_r.append(image)
		image = sprite_sheet.get_image(90, 0, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.frames_r.append(image)
		image = sprite_sheet.get_image(120, 0, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.frames_r.append(image)
		image = sprite_sheet.get_image(150, 0, 30, 47)
		image = pygame.transform.flip(image, True, False)
		self.frames_r.append(image)

		
		# Set the image the player starts with
		self.image = self.frames_r[0]

		# Set a referance to the image rect.
		self.rect = self.image.get_rect()
		
		self.pos = self.rect.x
		
	def update(self):
		
		self.pos += self.change_x
		if self.direction == "R":
			frame = (self.pos // 9) % len(self.frames_r)
			self.image = self.frames_r[frame]
		elif self.direction == "L":
			frame = (self.pos // 9) % len(self.frames_l)
			self.image = self.frames_l[frame]
			
			
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

		

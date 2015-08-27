import pygame
import constants
import random


from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite


class Thingers(pygame.sprite.Sprite):
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
		

class Level():
	""" Shifting the background items left or right on the screen """
	
	go = 0
	buffr = 0
	buffl = 0
	fencel = 1
	fencer = 1
	
	
	def __init__(self):
		self.fence_list = pygame.sprite.Group()
		self.fence_temp = pygame.sprite.Group()
		self.walk_temp = pygame.sprite.Group()
		self.junk_list = pygame.sprite.Group()
		self.walk_list = pygame.sprite.Group()
		self.background = pygame.image.load("background_02.png").convert()
		i=-1
		while i<11:
			sprite = Thingers(constants.FENCE_MIDDLE)
			sprite.rect.x = i*40
			sprite.rect.y = constants.FENCE_HEIGHT-64
			self.fence_list.add(sprite)
			sprite = Thingers(constants.CONCRETE)
			sprite.rect.x = i*40
			sprite.rect.y = constants.FENCE_HEIGHT
			self.walk_list.add(sprite)
			i += 1
		
	def update(self):
		self.fence_list.update()
		self.junk_list.update()
		self.walk_list.update()
		if self.go == 1:
			for fence in self.fence_list:
				fence.rect.x += (-constants.O_SPEED)
			for junk in self.junk_list:
				junk.rect.x += (-constants.O_SPEED)
			for walk in self.walk_list:
				walk.rect.x += (-constants.O_SPEED)
			self.buffr += (-constants.O_SPEED)
			self.buffl += (-constants.O_SPEED)
			side = "R"
		
		elif self.go == -1:
			for fence in self.fence_list:
				fence.rect.x += (constants.O_SPEED)
			for junk in self.junk_list:
				junk.rect.x += (constants.O_SPEED)
			for walk in self.walk_list:
				walk.rect.x += (constants.O_SPEED)
			self.buffr += (constants.O_SPEED)
			self.buffl += (constants.O_SPEED)
			side ="L"
		else:
			side = "K"
			
		if self.buffr < constants.RIGHT_BUFF:
			self.make_fence("R")
			
		if self.buffl > constants.LEFT_BUFF:
			self.make_fence("L")
			
		if self.buffr > constants.RIGHT_BUFF+100 or self.buffl < constants.LEFT_BUFF-100:
			self.rem_obj(side)
			
		if len(self.junk_list) > 20:
			self.rem_obj("J")
			
		if random.randrange(1000) < 5 and len(self.junk_list) < 20:
			self.randobj(side)
				
		
	def draw(self,screen):
		""" Draw everything on this level. """

		# Draw the background
		# We don't shift the background as much as the sprites are shifted
		# to give a feeling of depth.
		screen.fill(constants.WHITE)
		screen.blit(self.background,(0,0))

		# Draw all the sprite lists that we have
		self.fence_list.draw(screen)
		self.walk_list.draw(screen)
		self.junk_list.draw(screen)
		
	def left(self):
		self.go = 1
		
	def right(self):
		self.go = -1
		
	def stop(self):
		self.go = 0
		
	def make_fence(self,side):
		
		sprite = Thingers(constants.FENCE_MIDDLE)
		walk = Thingers(constants.T1)
		if side == "R":
			sprite.rect.x = self.buffr
			walk.rect.x = self.buffr
			self.buffr += 40
		else:
			sprite.rect.x = self.buffl-40
			walk.rect.x = self.buffl-40
			self.buffl += -40
		sprite.rect.y = constants.FENCE_HEIGHT-64
		walk.rect.y = constants.FENCE_HEIGHT
		self.fence_list.add(sprite)
		self.walk_list.add(walk)
		
	
	def rem_obj(self,side):
		for fence in self.fence_list:
			if fence.rect.x > constants.LEFT_BUFF:
				self.fence_temp.add(fence)
		for walk in self.walk_list:
			if walk.rect.x > constants.LEFT_BUFF:
				self.walk_temp.add(walk)
		for fence in self.fence_list:
			if fence.rect.x < constants.RIGHT_BUFF:
				self.fence_temp.add(fence)
		for walk in self.walk_list:
			if walk.rect.x < constants.RIGHT_BUFF:
				self.walk_temp.add(walk)
					
		self.fence_list.empty()
		self.walk_list.empty()
		self.fence_list = self.fence_temp.copy()
		self.walk_list = self.walk_temp.copy()
		self.fence_temp.empty()
		self.walk_temp.empty()
		
		if side == "J":
			for fence in self.junk_list:
				if fence.rect.x > constants.LEFT_BUFF:
					self.fence_temp.add(fence)
				if fence.rect.x < constants.RIGHT_BUFF:
					self.fence_temp.add(fence)
			self.junk_list.empty()
			self.junk_list = self.fence_temp.copy()
			self.fence_temp.empty()
		
	def randobj(self,side):
	
		randn = len(constants.OBJ_RAND_LIST)
		thingdat = constants.OBJ_RAND_LIST[random.randrange(randn)]
		sprite = Thingers(thingdat)
		if side == "L":
			sprite.rect.x = random.randrange(385,400)
		elif side == "R":
			sprite.rect.x = -random.randrange(30,70)
		sprite.rect.y = constants.STUFF_HEIGHT-sprite.rect.height
		self.junk_list.add(sprite)

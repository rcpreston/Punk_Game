import pygame
import constants
#import menu

from object_class import Thing
from player import Player
from phone_menu import open_phone

# need handle:
# entrance points = text doc called entrance_list where each line is a set of x,y coords player starts at on map depending on entrance
# exits to map
# position based events?

class Map():
	wall_list = None
	layer_list = None
	object_list = None
	npc_list = None
	
	map_num = 0
	map_folder = ""
	bg_shift = 0
	bg_shift_speed = 0
	back1_shift = 0
	back2_shift = 0
	player_y = 0
	main_shift = 0
	go = 0
	is_collide_r = False
	is_collide_l = False
	
	###
	"""
	Break it up into layers -
	background sky with clouds 40
	Far back items 70
	back wall of player space 150 pixels
	how wide player space? 170 pixels - broken up into 5 pixel tall segments
	50 pixels more below player space

	total height = 480
	no max width, character moves up/down
	screen moves left/right

	player top margin = 264
	player bottom margin = 434
	These account for where the player's FEET should be
	"""
	###


	def __init__(self,map_num):

		self.wall_list = pygame.sprite.Group()
		self.object_list = pygame.sprite.Group()
		self.npc_list = pygame.sprite.Group()
		self.layer_list = pygame.sprite.LayeredUpdates()
		
		self.map_num = map_num
		self.map_folder = "../res/Map/Map"+str(map_num)
		
		text_file = open(self.map_folder+"/map_info.txt", "r")
		lines = text_file.read().split(',')
		text_file.close()
		
		map_length = int(lines[0])
		self.bg_shift = int(lines[1])
		self.bg_shift_speed = int(lines[2])
		self.world_shift = 305 - self.bg_shift
				
		self.background = pygame.image.load(self.map_folder+"/background.png").convert()
		self.front_image = Thing((self.map_folder+"/front_image.png",0,0,map_length,480))
		self.ground = Thing((self.map_folder+"/floor.png",0,0,map_length,480))
		self.back_wall = Thing((self.map_folder+"/back_wall.png",0,0,map_length,480))
		self.back_image1 = Thing((self.map_folder+"/back_image1.png",0,0,map_length,480))
		self.back_image2 = Thing((self.map_folder+"/back_image2.png",0,0,map_length,480))
		
		self.back_image1.rect.x = int(lines[3])
		self.back_image1.rect.y = 0
		self.back1_shift = int(lines[4])
		self.back_image2.rect.x = int(lines[5])
		self.back_image2.rect.y = 0
		self.back2_shift = int(lines[6])
		self.back_wall.rect.x = int(lines[7])
		self.back_wall.rect.y = 0
		self.ground.rect.x = int(lines[8])
		self.ground.rect.y = 0
		self.front_image.rect.x = int(lines[9])
		self.front_image.rect.y = 0
		self.main_shift = int(lines[10])
		self.player_y = int(lines[11])
		
		self.layer_list.add(self.back_image1,layer=0)
		self.layer_list.add(self.back_image2,layer=1)
		self.layer_list.add(self.back_wall,layer=2)
		self.layer_list.add(self.ground,layer=3)
		self.layer_list.add(self.front_image,layer=5)
		
		text_file = open(self.map_folder+"/entrance_list.txt","r")
		self.entrance_list = text_file.read().split('\n')
		text_file.close()
		
		text_file = open(self.map_folder+"/wall_list.txt", "r")
		lines = text_file.read().split('\n')
		text_file.close()
		y_loc = 264
		for line in lines:
			walls = line.split(',')
			for wall in walls:
				new_wall = Thing((self.map_folder+"/wall_collide.png",0,0,5,5))
				new_wall.rect.x = int(wall)+self.bg_shift
				new_wall.rect.y = y_loc
				self.wall_list.add(new_wall)
			y_loc += 5
		

	# Update everything on this level
	def update(self,player):
		""" Update everything in this level."""
		self.layer_list.update()
		self.wall_list.update()
		self.can_shift(player,self.wall_list)
		self.can_shift(player,self.object_list)
		self.can_shift(player,self.npc_list)
		
		self.bg_shift += self.go*self.bg_shift_speed
		self.back_image1.rect.x += self.go*self.back1_shift
		self.back_image2.rect.x += self.go*self.back2_shift
		
		self.ground.rect.x +=self.go*self.main_shift
		self.back_wall.rect.x += self.go*self.main_shift
		self.front_image.rect.x += self.go*self.main_shift

		# Go through all the sprite lists and shift
		for wall in self.wall_list:
			wall.rect.x += self.go*self.main_shift
		for object in self.object_list:
			object.rect.x += self.go*self.main_shift
		for npc in self.npc_list:
			npc.rect.x += self.go*self.main_shift
		

	def draw(self, screen, player):
		""" Draw everything on this level. """

		# Draw the background
		screen.fill(constants.BLACK)
		screen.blit(self.background,(self.bg_shift,0))

		# Draw all the sprite lists that we have
		self.wall_list.draw(screen)
		self.layer_list.add(player,layer=4)
		self.layer_list.draw(screen)
		#self.wall_list.draw(screen)
		#self.npc_list.draw(screen)
		self.layer_list.remove(player)

		#Draw the very front stuff
		
	def left(self):
		self.go = -1
		
	def right(self):
		self.go = 1
		
	def stop(self):
		self.go = 0

	def can_shift(self,player,list):
		for item in list:
			if player.collide_right(item)[0]:
				self.shift_world(player.collide_right(item)[1])
				self.go = 0
				
			elif player.collide_left(item)[0]:
				self.shift_world(player.collide_left(item)[1])
				self.go = 0
				
											
	def char_y(self,entrance):
		return self.player_y
		
	def shift_world(self, shift_x):
	
		""" When move the player space """
		
		self.ground.rect.x += shift_x
		self.back_wall.rect.x += shift_x
		self.front_image.rect.x += shift_x

		# Go through all the sprite lists and shift
		for wall in self.wall_list:
			wall.rect.x += shift_x
		for object in self.object_list:
			object.rect.x += shift_x
		for npc in self.npc_list:
			npc.rect.x += shift_x
		

		
'''
class Scene(object):
	""" This is a generic super-class used to define a level.
		Create a child class for each level with level-specific
		info. """

	# Lists of sprites used in all levels. Add or remove
	# lists as needed for your game. """
	npc_list = None
	wall_list = None
	done = False
	scene_num = 0
	player = 0
	scene_next = [0,0]
	world_shift_x = 0
	world_shift_y = 0

	# Background image
	background = None

	def __init__(self,player):
		""" Constructor. Pass in a handle to player. Needed for when moving platforms
			collide with the player. """
		self.wall_list = pygame.sprite.Group()
		self.npc_list = pygame.sprite.Group()
		self.player = player
		self.background = pygame.image.load("../res/Scene/Scene"+str(scene_num)+"background.png").convert()


	# Update everything on this level
	def update(self):
		""" Update everything in this level."""
		self.wall_list.update()
		self.npc_list.update()

	def draw(self, screen):
		""" Draw everything on this level. """

		# Draw the background
		# We don't shift the background as much as the sprites are shifted
		# to give a feeling of depth.
		screen.fill(constants.BLACK)
		screen.blit(self.background,(self.word_shift_x,self.world_shift_y))

		# Draw all the sprite lists that we have
		self.wall_list.draw(screen)
		self.npc_list.draw(screen)

	def shift_world(self, shift_x,shift_y):
		""" When the user moves left/right and we need to scroll everything: """

		# Keep track of the shift amount
		self.world_shift_x += shift_x
		self.world_shift_y += shift_y

		# Go through all the sprite lists and shift
		for wall in self.wall_list:
			wall.rect.x += shift_x
			wall.rect.y += shift_y
		for npc in self.npc_list:
			npc.rect.x += shift_x
			npc.rect.y += shift_y

	def next(self):
		if self.player == 1:
			return self.scene_next[0]
		elif self.player == 2:
			return self.scene_next[1]

	def is_done(self):
		return self.done
'''

if __name__ == "__main__":
	pygame.init()

	size= [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Punks R Us")

	test_map = Map(1)
	choice = 1

	player = Player(constants.SKUNK)

	player.set_x(305)
	player.set_y(test_map.char_y(1))
	done = False

	clock = pygame.time.Clock()

	while not done:
		# Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					player.go_right()
					test_map.left()
				if event.key == pygame.K_LEFT:
					player.go_left()
					test_map.right()
				if event.key == pygame.K_UP:
					player.go_up()
				if event.key == pygame.K_DOWN:
					player.go_down()
				if event.key == pygame.K_m:
					open_phone()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					player.stop("R")
					test_map.stop()
				if event.key == pygame.K_LEFT:
					player.stop("L")
					test_map.stop()
				if event.key == pygame.K_UP:
					player.stop("U")
				if event.key == pygame.K_DOWN:
					player.stop("D")

		test_map.update(player)
		player.update()

		test_map.draw(screen,player)
		# Limit to 60 frames per second
		clock.tick(60)
		
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
	pygame.quit()
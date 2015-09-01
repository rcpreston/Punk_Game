import pygame
import constants
#import menu

from object_class import Thing
from player import Player
from phone_menu import open_phone

# Call Character select
# Call Episode selection
# Run episode
# Call scene class
# Scene class has:
# all npc data
# all object data
# all special event data
# Script??

class Scene():

	# Lists of sprites used in all levels. Add or remove
	# lists as needed for your game. """
	npc_list = None
	object_list = None
	wall_list = None
	done = False
	scene_folder = ""


	def __init__(self,scene_num):
		""" Constructor. Pass in a handle to player. Needed for when moving platforms collide with the player. """
		self.wall_list = pygame.sprite.Group()
		self.npc_list = pygame.sprite.Group()
		self.object_list = pygame.sprite.Group()
		self.scene_folder = "../res/Scene/Scene"+str(scene_num)
		


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

	def play_scene(self):
		while not self.done:
			

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
				player.stop()
				test_map.stop()

		test_map.update(player)
		player.update()

		test_map.draw(screen,player)
		# Limit to 60 frames per second
		clock.tick(60)
		
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
	pygame.quit()
'''
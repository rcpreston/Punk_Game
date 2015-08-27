import pygame
import objects
import constants

from player import Player

def main():
	pygame.init()
	
	size= [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Punks R Us")
	
	active_sprite_list = pygame.sprite.Group()
	
	# Create the player
	player = Player()
	
	player.rect.x = constants.SCREEN_WIDTH/2 - player.rect.width/2
	player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
	active_sprite_list.add(player)
	
	level = objects.Level()
	#Loop until the user clicks the close button.
	done = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
	
	# -------- Main Program Loop -----------
	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					player.go_right()
					level.left()
				if event.key == pygame.K_LEFT:
					player.go_left()
					level.right()
					
			if event.type == pygame.KEYUP:
				player.stop()
				level.stop()

		# Update the player.
		level.update()
		active_sprite_list.update()


		# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
		level.draw(screen)
		active_sprite_list.draw(screen)

		# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()

if __name__ == "__main__":
	main()

	
	


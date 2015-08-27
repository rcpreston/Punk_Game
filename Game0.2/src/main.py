import pygame
import constants
import object_class
import player
import charselect

def main():
	pygame.init()
	
	size= [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Punks R Us")
	
	# Different pieces!
	map = Map()
	scene = Scene()
	npc_list = pygame.sprite.Group()
	item_list = pygame.sprite.Group()
	text_box = TextBox(self)
	
	character = charselect.CharSelect()
	
	# Getting the player character
	if character == "Quit":
		done = True
	else:
		# Create the player
		player = Player(character)
	
		player.rect.x = constants.SCREEN_WIDTH/2 - player.rect.width/2
		player.rect.y = constants.SCREEN_HEIGHT-45 - player.rect.height
	
	
	
	# Loop until the user clicks the close button.
	done = False
 
	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
	 
	# -------- Main Program Loop -----------
	while not done:
		# --- Main event loop
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop
				
			# Call event check function
			check_event(event,map,scene,player,npc_list,item_list)
	 
		# --- Game logic should go here
		map.update()
		npc_list.update()
		item_list.update()
		player.update()
		scene.update()
	 
		# --- Drawing code should go here
	 
		# First, clear the screen to white. Don't put other drawing commands
		# above this, or they will be erased with this command.
		screen.fill(constants.BLACK)
		map.draw(screen)
		npc_list.draw(screen)
		player.draw(screen)
		item_list.draw(screen)
		if dialogue == True:
			for npc in npc_list:
				if npc.is_talk() == True:
					text = font.render(npc.current_text(player.who()),True,constants.WHITE)
					textsize = font.size(npc.current_text(player.who()))
					text_box.draw(screen,npc.what_box())
					textheight = text_box.rect.y + text_box.rect.height/2 - textsize[1]/2
					screen.blit(text, [constants.SCREEN_WIDTH/2-textsize[0]/2, textheight])
	 
		# --- Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
	 
		# --- Limit to 60 frames per second
		clock.tick(60)
		
	pygame.quit()

if __name__ == "__main__":
	main()

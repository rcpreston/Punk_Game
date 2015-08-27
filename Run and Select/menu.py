import pygame
import constants
from objects import Thingers
from spritesheet_functions import SpriteSheet

def CharSelect():
	# Character Selection screen
	
	# Things we need before loop
	done = False
	choice = constants.BEANIE
	
	size= [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	
	active_sprite_list = pygame.sprite.Group()
	text_list = pygame.sprite.Group()
	
	text_box = Thingers(constants.TB2)
	text_box.rect.x = 0
	text_box.rect.y = constants.SCREEN_HEIGHT - text_box.rect.height
	
	sprite_sheet = SpriteSheet(constants.TB1[0])
	skunkbox = sprite_sheet.get_image(constants.TB1[1],
									constants.TB1[2],
									constants.TB1[3],
									constants.TB1[4])
	sprite_sheet = SpriteSheet(constants.TB2[0])
	beanbox = sprite_sheet.get_image(constants.TB2[1],
									constants.TB2[2],
									constants.TB2[3],
									constants.TB2[4])
	
	arrow = Thingers(constants.A1)
	arrow.rect.x = constants.SCREEN_WIDTH/2-60-arrow.rect.width
	arrow.rect.y = constants.SCREEN_HEIGHT/2 - arrow.rect.height/2
	
	skunk = Thingers(constants.SKUNK_SELECT)
	skunk.rect.x = constants.SCREEN_WIDTH/2+30
	skunk.rect.y = constants.SCREEN_HEIGHT/2 - skunk.rect.height/2
	
	beanie = Thingers(constants.BEANIE_SELECT)
	beanie.rect.x = constants.SCREEN_WIDTH/2-60
	beanie.rect.y = constants.SCREEN_HEIGHT/2 - beanie.rect.height/2
	
	active_sprite_list.add(arrow)
	active_sprite_list.add(skunk)
	active_sprite_list.add(beanie)
	text_list.add(text_box)
	
	select = -1
	
	clock = pygame.time.Clock()
	
	# Select the font to use, size, bold, italics
	font = pygame.font.Font(None, 12)
 

	# Set the loop
	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop
				choice = "Quit"

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					if select == -1:
						select = 1
						text_box.image = skunkbox
						text_box.rect.x = 0
						text_box.rect.y = constants.SCREEN_HEIGHT - text_box.rect.height
						arrow.rect.x += 90
					else:
						select = -1
						text_box.image = beanbox
						text_box.rect.x = 0
						text_box.rect.y = constants.SCREEN_HEIGHT - text_box.rect.height
						arrow.rect.x += -90
				if event.key == pygame.K_RETURN:
					if select == -1:
						choice = constants.BEANIE
					else:
						choice = constants.SKUNK
					done = True
					
			#if event.type == pygame.KEYUP:
				

		# Update the screen
		active_sprite_list.update()
		text_list.update()

		# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
		screen.fill(constants.BLACK)
		screen.blit(pygame.image.load("brickbackground.png").convert(),(0,0))
		# Render the text. "True" means anti-aliased text.
		# Black is the color.
		text = font.render("Choose",True,constants.WHITE)
		textsize = font.size("Choose")
		# Put the image of the text on the screen at 
		screen.blit(text, [constants.SCREEN_WIDTH/2-textsize[0]/2, 2])
		
		active_sprite_list.draw(screen)
		if select == -1:
			text = font.render("Beanie",True,constants.WHITE)
			textsize = font.size("Beanie")
		else:
			text = font.render("Skunk",True,constants.WHITE)
			textsize = font.size("Skunk")
		text_list.draw(screen)
		textheight = text_box.rect.y + text_box.rect.height/2 - textsize[1]/2
		screen.blit(text, [constants.SCREEN_WIDTH/2-textsize[0]/2, textheight])
		

		# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	return choice
	
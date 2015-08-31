import pygame
import constants
from object_class import Thing
import os
from spritesheet_functions import get_frames
from spritesheet_functions import animate_frame

def CharSelect():
	# Character Selection screen
	pygame.init()
	
	size= [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Punks R Us")
	char_list = os.listdir('../res/Character')
	sprite_list = pygame.sprite.Group()
	
	
	done = False
	
	choice = 0
	clock = pygame.time.Clock()
	# Select the font to use, size, bold, italics
	font = pygame.font.Font('../res/Phone/nokiafc22.ttf', 12)
	count = 0
	
	while not done:
		
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					if choice == len(char_list)-1:
						choice = 0
					else:
						choice +=1
					count = 0
				if event.key == pygame.K_LEFT:
					if choice == 0:
						choice = len(char_list)-1
					else:
						choice += -1
					count = 0
				if event.key == pygame.K_RETURN:
					if select == 1:
						choice = constants.BEANIE
					else:
						choice = constants.SKUNK
					done = True
		# Setup to display/"update"
		count += 1
		mug = Thing(("../res/Character/"+char_list[choice]+"/mug.png",0,0,150,194))
		mug.rect.x = 0
		mug.rect.y = 80
		sprite = Thing(("../res/Character/"+char_list[choice]+"/spritesheet.png",30,0,30,47))
		sprite.rect.y = 110
		sprite.rect.x = 240
		text_box = Thing(( "../res/Character/"+char_list[choice]+"/text_box.png",0,0,480,46))
		text_box.rect.x = 0
		text_box.rect.y = 480-47
		
		fight = get_frames("../res/Character/"+char_list[choice]+"/fightsheet.png",120,100,0,1020,0)
		fight_pic = animate_frame(fight,1,count)
		
		text_file = open("../res/Character/"+char_list[choice]+"/char_select.txt","r")
		lines = text_file.read().split('\n')
		text_file.close()
		
		# Draw all yo shit
		screen.fill(constants.BLACK)
		text = font.render('<< Choose Your Player >>',True,constants.WHITE)
		screen.blit(text, [constants.SCREEN_WIDTH/2-font.size('<< Choose Your Player >>')[0]/2, 30])
		text = font.render(lines[0],True,constants.WHITE)
		screen.blit(text, [360-font.size(lines[0])[0]/2,80])
		sprite_list.add(mug)
		sprite_list.add(sprite)
		sprite_list.add(text_box)
		sprite_list.draw(screen)
		sprite_list.empty()
		screen.blit(fight_pic, [290,110])
		text = font.render(lines[1],True,constants.WHITE)
		screen.blit(text, [constants.SCREEN_WIDTH/2-font.size(lines[1])[0]/2, 480-23-font.size(lines[1])[1]/2])
		
		# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
		
		
		
		

	"""
	# Things we need before loop
	done = False
	choice = constants.BEANIE
	
	size= [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	
	active_sprite_list = pygame.sprite.Group()
	text_box = TextBox(self)
	
	arrow = object_class.Thing(constants.A1)
	arrow.rect.x = constants.SCREEN_WIDTH/2-60-arrow.rect.width
	arrow.rect.y = constants.SCREEN_HEIGHT/2 - arrow.rect.height/2
	
	skunk = object_class.Thing(constants.SKUNK_SELECT)
	skunk.rect.x = constants.SCREEN_WIDTH/2+30
	skunk.rect.y = constants.SCREEN_HEIGHT/2 - skunk.rect.height/2
	
	beanie = object_class.Thing(constants.BEANIE_SELECT)
	beanie.rect.x = constants.SCREEN_WIDTH/2-60
	beanie.rect.y = constants.SCREEN_HEIGHT/2 - beanie.rect.height/2
	
	active_sprite_list.add(arrow)
	active_sprite_list.add(skunk)
	active_sprite_list.add(beanie)
	
	select = 1
	
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
					if select == 1:
						select = 2
						arrow.rect.x += 90
					else:
						select = 1
						arrow.rect.x += -90
				if event.key == pygame.K_RETURN:
					if select == 1:
						choice = constants.BEANIE
					else:
						choice = constants.SKUNK
					done = True
					
			#if event.type == pygame.KEYUP:
				

		# Update the screen
		active_sprite_list.update()

		# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
		screen.fill(constants.BLACK)
		screen.blit(pygame.image.load("../res/brickbackground.png").convert(),(0,0))
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
		text_box.draw(screen,select)
		textheight = text_box.rect.y + text_box.rect.height/2 - textsize[1]/2
		screen.blit(text, [constants.SCREEN_WIDTH/2-textsize[0]/2, textheight])
		

		# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	return choice
	"""
	
if __name__ == "__main__":
	CharSelect()
	pygame.quit()
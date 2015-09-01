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
					done = scene_select(char_list[choice])
		# Setup to display/"update"
		count += 1
		mug = Thing(("../res/Character/"+char_list[choice]+"/mug.png",0,0,150,194))
		mug.rect.x = 0
		mug.rect.y = 80
		sprite = Thing(("../res/Character/"+char_list[choice]+"/spritesheet.png",30,0,30,47))
		sprite.rect.y = 110
		sprite.rect.x = 240
		text_box = Thing(( "../res/Character/"+char_list[choice]+"/text_box.png",0,0,640,46))
		text_box.rect.x = 0
		text_box.rect.y = 480-47
		
		text_file = open("../res/Character/"+char_list[choice]+"/char_select.txt","r")
		lines = text_file.read().split('\n')
		text_file.close()
		
		fight = get_frames("../res/Character/"+char_list[choice]+"/fightsheet.png",120,100,0,int(lines[0]),0)
		fight_pic = animate_frame(fight,1,count)
		
		
		
		# Draw all yo shit
		screen.fill(constants.BLACK)
		# Select the font to use, size, bold, italics
		font = pygame.font.Font(constants.F4, 60)
		text = font.render('< Choose Your Player >',True,constants.WHITE)
		screen.blit(text, [constants.SCREEN_WIDTH/2-font.size('< Choose Your Player >')[0]/2, 15])
		# Select the font to use, size, bold, italics
		font = pygame.font.Font(constants.F7, 20)
		text = font.render(lines[1],True,constants.WHITE)
		screen.blit(text, [360-font.size(lines[1])[0]/2,80])
		sprite_list.add(mug)
		sprite_list.add(sprite)
		sprite_list.add(text_box)
		sprite_list.draw(screen)
		sprite_list.empty()
		screen.blit(fight_pic, [290,110])
		font = pygame.font.Font(constants.F7, 12)
		text = font.render(lines[2],True,constants.WHITE)
		screen.blit(text, [constants.SCREEN_WIDTH/2-font.size(lines[2])[0]/2, 480-23-font.size(lines[2])[1]/2])
		
		# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
		
		
		
def scene_select(character):
	# Scene Selection Screen
	
	pygame.init()
	
	size= [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Punks R Us")
	char_folder = "../res/Character/"+character
	sprite_list = pygame.sprite.Group()
	text_file = open(char_folder+"/scene_list.txt","r")
	lines = text_file.read().split('\n')
	text_file.close()
	i=1
	scene_num = []
	scene_list = []
	for line in lines:
		if i%2 != 0:
			scene_num.append(line)
		else:
			scene_list.append(line)
		i+=1
	
	done = False
	select_box = Thing((char_folder+"/select_line.png",0,0,113,30))
	select_box.rect.x = 100
	select_box.rect.y = 100
	sprite_list.add(select_box)
	choice = 0
	clock = pygame.time.Clock()
	count = 0
	
	
	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					if choice == len(scene_list)-1:
						choice = 0
						select_box.rect.y = 100
						select_box.rect.x = 100
					else:
						choice +=1
						select_box.rect.y += 40
						select_box.rect.x += 20
					count = 0
				if event.key == pygame.K_UP:
					if choice == 0:
						choice = len(scene_list)-1
						select_box.rect.y = 100 + choice*40
						select_box.rect.x = 100 + choice*20
					else:
						choice += -1
						select_box.rect.y += -40
						select_box.rect.x += -20
					count = 0
				#if event.key == pygame.K_RETURN:
					# Call shit to set up all the scene stuff
					
		# Setup to display/"update"
		
		# Draw all yo shit
		screen.fill(constants.BLACK)
		
		sprite_list.draw(screen)
		
		# Draw all the text
		font = pygame.font.Font(constants.F4, 60)
		text = font.render('Scene Selection',True,constants.WHITE)
		screen.blit(text, [constants.SCREEN_WIDTH/2-font.size('Scene Selection')[0]/2, 15])
		font = pygame.font.Font(constants.F7, 20)
		y = 100
		x = 120
		for scene in scene_list:
			text = font.render(scene,True,constants.WHITE)
			screen.blit(text, [x, y])
			y += 40
			x += 20
		
		# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
	
	
	return done
	
if __name__ == "__main__":
	CharSelect()
	pygame.quit()
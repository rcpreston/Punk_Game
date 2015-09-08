"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame

import constants

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
    # This points to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.PINK)

        # Return the image
        return image

def get_frames(sheet,width,height,start_x,num_frames,y, flipped = False):
	sprite_sheet = SpriteSheet(sheet)
	frame_list = []
	i = 0
	x_pos = start_x
	if not flipped:
		x_pos = start_x+width*(num_frames-1)
	while i < num_frames:
		image = sprite_sheet.get_image(x_pos, y, width, height)
		i += 1
		x_pos = start_x+width*(num_frames-1-i)
		if flipped:
			image = pygame.transform.flip(image, True, False)
			x_pos = start_x+i*width
		frame_list.append(image)
	return frame_list
	

	
	
def animate_frame(frames,speed,count):
	frame = (count // speed) % len(frames)
	return frames[frame]
	
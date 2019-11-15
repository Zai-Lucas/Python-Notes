import pygame
pygame.init()

screen = pygame.display.set_mode((100,100))

all_colors = pygame.Surface((4096, 4096), depth=24)

for r in range(256):
	print(r + 1, "out of 256")
	x = (r&15) * 256 # the r&15, is a bitwise and 
	y = (r>>4) * 256 # The r>>4, is the same as dividing r by 2^4(16)\

	for g in range(256):
		for b in range(256):
			all_colors.set_at((x+g, y+b), (r,g,b))

	pygame.image.save(all_colors, "allcolors.bmp")
	pygame.quit()
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (800,800)
screen = pygame.display.set_mode(SCREEN_SIZE)\

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		print(event)
	pygame.display.update()
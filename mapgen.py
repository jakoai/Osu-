import math, time, pygame, sys

resolution = [1440, 900]
pygame.init()
screen = pygame.display.set_mode(resolution)

image = pygame.image.load("FLL2018.jpg")
while True:
	time.sleep(0.05)
	screen.fill((0, 0, 0))
	screen.blit(image, (0, 0))
	pygame.display.update()
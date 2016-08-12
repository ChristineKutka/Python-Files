import pygame
import random 

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (18, 100, 128)
SKY_BLUE = 	(175, 238, 238)

pygame.init()


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("House")
screen.fill(SKY_BLUE)
pygame.draw.polygon(screen, BLACK, ((60, 20,), (60, 20), (60, 20), (20,60), (20,60)))
# pygame.draw.polygon(screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

done = False

clock = pygame.time.Clock()

class Person():
	def __init__(self,location_x, location_y,):
		self.location_x = x_location
		self.location_y = y_location
		self.move[]
	
		
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            screen.fill(SKY_BLUE)


		





















while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True 


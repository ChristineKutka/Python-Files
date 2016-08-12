import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (18, 100, 128)
MOVESPEED = 5


#This starts the game(below)
pygame.init()
# set the width and height of the screen (width, height)
screen_size = (700, 700)
# start_x = 5
# start_y = 5

# centerx += start_x
# centery += start_y

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Bouncy Ball")
screen.fill(DARK_BLUE)
pygame.draw.circle(screen, BLUE, (25,25), 30, 4)
# below keeps a variable done that keeps track of if i am still playing  
done = False 
# used to manage how fast the sccreen updates
my_fancy_clock = pygame.time.Clock()



# #main program loop 
# while not done:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			done = True 
# # Game logic is next 

# screen clear coding is here 

# here is where we clear the screen to white. DOnt put other drawing comands above this or they will be erased. 

# if you ant a backgeound image, relpaces this clear with blithing the background imae.

# 	screen.fill(GREEN)
# 	pygame.draw.circle(screen, BLUE, (x,y), 30, 4)
# 	# pygame.draw.line(screen, BLUE, (100, 350), (300, 350))
# # drawing code is here redraw based on the new state
# #update the screen with what ive drawn
# 	pygame.display.flip()
# 	pygame.time.delay(1)
# 	# screen.fill(GREEN)
# 	# pygame.draw.circle(screen, WHITE, (349,250), 30, 4)
# 	# pygame.display.flip()
# 	# pygame.time.delay(1000)
# 	# screen.fill(GREEN)
# 	# pygame.draw.circle(screen, DARK_BLUE, (348,250), 30, 4)
# 	# pygame.display.flip()
# 	# pygame.time.delay(1000)
# 	# if x = 700:
# 	if x >= screen_size():
# 		x *= -1




# # limit to 60 frames per second
# my_fancy_clock.tick(60)
# # clock is used to manage how fast the screen updates clock = pygame.time.Clock()
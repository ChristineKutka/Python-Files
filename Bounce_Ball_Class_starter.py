"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
 



pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]


# BOUNCING BALL CLASS CODE  

class BouncingBall(): 


# 1. Invoke the ball’s flashBounce method within the main program loop
# If you aren’t sure how to invoke (or “call”) the object’s method, consult your slides and/or online documentation
# 2. Make another instance of the Ball object.
# If you aren’t sure what an “instance” is, consult your slides and/or online documentation

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, colors, screen_width, screen_height):

        ball_color = random.choice(colors) # This is outside because of variable scoping.

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)

    
# BouncingBall = []
# BouncingBall.append()
flower = BouncingBall(300, 200, 10, 10, 10)
flower2 = BouncingBall(100, 300, 15, 15, 10)
flower3 = BouncingBall(222, 234, 12, 12, 10)
flower4 = BouncingBall(464, 123, 18, 18, 10)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN) 

#CODE GOES HERE!!!
# Create instance of BouncingBall
# self, x_location, y_location, x_speed, y_speed, ball_size
    
# (self, screen, colors, screen_width, screen_height)
    # flashBounce = []
    # flashBounce.append()
    flower.flashBounce(screen, possible_ball_colors, 700, 500)
    flower2.flashBounce(screen, possible_ball_colors, 700, 500)
    flower3.flashBounce(screen, possible_ball_colors, 700, 500)
    flower4.flashBounce(screen, possible_ball_colors, 700, 500)
    















    
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE



import pygame
from pygame.locals import *
import sys
from ball import Ball
from player import Player
from angle import get_angle

pygame.init()

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
WHITE = (255,255,255)
BLACK = (0,0,0)
START_SCREEN = False
GAME = True
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
# Paddle width and height
paddle_width = 10
paddle_height = 50
# Creating Ball object
ball = Ball(7, SCREEN_HEIGHT, SCREEN_HEIGHT)
# Creating Player objects
player_left = Player("Player 1", paddle_width, paddle_height, 20, SCREEN_HEIGHT // 2 - paddle_height // 2)
player_right = Player("Player 2", paddle_width, paddle_height, SCREEN_WIDTH - 10 - paddle_width, SCREEN_HEIGHT // 2 - paddle_height // 2)

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    # Check if right player is AI
    player_right.set_ai(False)
    # Get keys pressed
    keys = pygame.key.get_pressed()
    # Check for keys pressed and move paddle accordingly
    if keys[119] == True: # w key
        player_left.paddle.move(True)
    if keys[115] == True: # s key
        player_left.paddle.move(False)
    if player_right.get_ai() == False:
        if keys[K_UP] == True: # up arrow
            player_right.paddle.move(True)
        if keys[K_DOWN] == True: # down arrow
            player_right.paddle.move(False)

    # Get ball coordinates
    ball_coords = ball.get_coords()
    # Set ball x and y coordinates as variables
    ball_x = ball_coords[0]
    ball_y = ball_coords[1]
    # Get ball size, x and y speeds
    ball_size = ball.get_size()
    ball_y_speed = ball.get_y_speed()
    ball_x_speed = ball.get_x_speed()
    # Check for collision between ball and roof of screen
    if ball_y + ball_size >= SCREEN_HEIGHT:
        ball.set_y_speed(ball_y_speed * -1)
    elif ball_y - ball_size <= 0:
        ball.set_y_speed(ball_y_speed * -1)

    # Get position of left and right paddles
    left_paddle_y = player_left.paddle.get_y()
    left_paddle_x = player_left.paddle.get_x()
    right_paddle_y = player_right.paddle.get_y()
    right_paddle_x = player_right.paddle.get_x()

    # Check for collision between ball and paddle  
    # Left Paddle  
    if ball_x_speed < 0:
        if ball_y >= left_paddle_y and ball_y <= left_paddle_y + paddle_height:
            if ball_x - ball_size <= left_paddle_x + paddle_width:
                ball.set_x_speed(ball_x_speed * -1)
                # Get new angle of ball
                y_speed = get_angle(ball_y, 5, left_paddle_y)
                ball.set_y_speed(y_speed * -1)
    # Right Paddle
    else:
        if ball_y >= right_paddle_y and ball_y <= right_paddle_y + paddle_height:
            if ball_x + ball_size >= right_paddle_x + paddle_width:
                ball.set_x_speed(ball_x_speed * -1)
                # Get new angle of ball
                y_speed = get_angle(ball_y, 6, right_paddle_y)
                ball.set_y_speed(y_speed * -1)
    
    # Update ball movement
    ball.move()

    # DRAWING
    screen.fill(BLACK)  # always the first drawing command
    if GAME:
        ball.draw(screen)
        player_left.paddle.draw(screen)
        player_right.paddle.draw(screen)
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

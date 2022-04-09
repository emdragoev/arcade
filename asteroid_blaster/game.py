import pygame, sys, time, random
from pygame.locals import *
from player import Player
from asteroid import Asteroid
from laser import Laser
from text import Text
from powerup import PowerUp

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
GAME = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fpsClock = pygame.time.Clock()
powerup_image = pygame.image.load("star.png")

# Creates custom user event
ADDASTEROID = pygame.USEREVENT + 1
pygame.time.set_timer(ADDASTEROID, 1250)

# Creates custom user event
ADDPOWERUP = pygame.USEREVENT + 2
pygame.time.set_timer(ADDPOWERUP, 20000)

# Creates cooldown user event
SHOOT_COOLDOWN = pygame.USEREVENT + 3
pygame.time.set_timer(SHOOT_COOLDOWN, 500)
shot_delay = False

# ---------------------------
# Initialize global variables

# Create Player
player = Player(0, 10)

# Game Over text
game_over = Text(f"Game Over", 100, SCREEN_HEIGHT // 2, 30)
# Create sprite groups
asteroids = pygame.sprite.Group()
lasers = pygame.sprite.Group()
x_laser = pygame.sprite.Group()
power_up = pygame.sprite.Group()

# Create sprite group that encases all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# ---------------------------

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        # Gets player coordinates 
        centerX = player.rect.center[0]
        centerY = player.rect.top
        # Check for KEYDOWN event
        if event.type == SHOOT_COOLDOWN:
            shot_delay = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            # Generates laser at player coordinates at K_SPACE event
            if event.key == K_SPACE and shot_delay == False:
                new_laser = Laser(centerX, centerY, 3, 7)
                # Add laser to lasers and all_sprites sprite group
                lasers.add(new_laser)
                all_sprites.add(new_laser)
                # Set timer for cooldown
                pygame.time.set_timer(SHOOT_COOLDOWN, 500)
                shot_delay = True
            if event.key == K_x and player.powerup == True:
                new_ult_laser = Laser(0, centerY, 400, 7)
                x_laser.add(new_ult_laser)
                all_sprites.add(new_ult_laser)
                player.powerup = False


        # Check for ADDASTEROID event
        elif event.type == ADDASTEROID:
            if GAME == True:
                # Create a new asteroid
                new_enemy = Asteroid(SCREEN_WIDTH)
                # Add asteroid to sprit Group
                asteroids.add(new_enemy)
                all_sprites.add(new_enemy)
        
        # Check for ADDPOWERUP event
        elif event.type == ADDPOWERUP:
            if GAME == True:
                # Create a new powerup
                new_power_up = PowerUp(SCREEN_WIDTH)
                # Add powerup to sprit Group
                power_up.add(new_power_up)
                all_sprites.add(new_power_up)


        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Get keys pressed
    pressed_keys = pygame.key.get_pressed()

    # Detect collision between laser and asteroid sprite group, delete both objects
    regular_collision = pygame.sprite.groupcollide(lasers, asteroids, True, True, collided = None)
    powerup_collision = pygame.sprite.groupcollide(lasers, power_up, True, True, collided = None)
    ult_collision = pygame.sprite.groupcollide(x_laser, asteroids, False, True, collided = None)
    if regular_collision or ult_collision:
        player.score += 1
    elif powerup_collision:
        player.powerup = True

    # End game if player lives is smaller than 0
    if player.lives <= 0:
        GAME = False

    # Update sprite positions
    player.update(pressed_keys)
    asteroids.update(player)
    lasers.update()
    x_laser.update()
    power_up.update(player)
    # Get player lives
    lives = Text(f"Lives: {player.lives}", 2, 2, 16)
    # Get player score
    score = Text(f"Score: {player.score}", 80, 2, 16)

    if GAME != False:
        # Fill the screen with black
        screen.fill(BLACK)
        # Draw player stats on screen
        lives.draw(screen)
        score.draw(screen)
        # Draw the sprites on the screen
        for sprite in all_sprites:
            screen.blit(sprite.surface, sprite.rect)
        if player.powerup == True:
            screen.blit(powerup_image, (375,2))
    else:
        for sprite in all_sprites:
            sprite.kill()
        screen.fill(BLACK)
        game_over.draw(screen)

    # Update the display
    pygame.display.flip()
    fpsClock.tick(30)


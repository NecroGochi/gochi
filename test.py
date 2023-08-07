import pygame
import math

# Initialize Pygame
pygame.init()

# Set the window size
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Circular Motion")

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set player position and properties
player_x = window_width // 2
player_y = window_height // 2
player_radius = 20

# Set object properties
object_radius = 10
object_distance = 100  # Distance from the player
object_angle = 0  # Initial angle

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the object position in polar coordinates
    object_angle += 0.02  # Angular speed
    object_x = player_x + object_distance * math.cos(object_angle)
    object_y = player_y + object_distance * math.sin(object_angle)

    # Clear the screen
    window.fill(black)

    # Draw the player
    pygame.draw.circle(window, white, (player_x, player_y), player_radius)

    # Draw the object
    pygame.draw.circle(window, red, (int(object_x), int(object_y)), object_radius)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()

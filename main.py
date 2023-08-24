import pygame
from Configure.configure import load_configure_data
from Menu.main_menu import MainMenu


# Initialize Pygame
pygame.init()

# Set the window size
window_width = 192 * 5
window_height = 108 * 5
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gochi Game")

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set Fonts
font_title = pygame.font.Font(None, 64)
font_options = pygame.font.Font(None, 32)

configure_data = load_configure_data()

# menu_state: main; lobby; option
menu_state = 'main'
selected_option = 0

# Menus
main_menu = MainMenu(window_width, window_height, font_title, font_options)

# Game loop
running = True
while running:
    main_menu.run_loop()

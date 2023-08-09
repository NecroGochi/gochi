import pygame
from Configure.configure import load_configure_data
from Menu.main_menu import MainMenu
from Configure.language_config import *


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

if configure_data["language"] == "english":
    # Set menu options
    main_menu_options = ENGLISH_MAIN_MENU_OPTIONS

    lobby_menu_options = [
        configure_data["player_name"],
        ENGLISH_LOBBY_MENU_OPTIONS[0],
        ENGLISH_LOBBY_MENU_OPTIONS[1],
        ENGLISH_LOBBY_MENU_OPTIONS[2]
    ]

    options_menu_options = [
        configure_data["player_name"],
        configure_data["language"],
        ENGLISH_OPTIONS_MENU_OPTIONS[0]
    ]


else:
    # Set menu options
    main_menu_options = POLISH_MAIN_MENU_OPTIONS

    lobby_menu_options = [
        configure_data["player_name"],
        POLISH_LOBBY_MENU_OPTIONS[0],
        POLISH_LOBBY_MENU_OPTIONS[1],
        POLISH_LOBBY_MENU_OPTIONS[2]
    ]

    options_menu_options = [
        configure_data["player_name"],
        configure_data["language"],
        POLISH_OPTIONS_MENU_OPTIONS[0]
    ]

# menu_state: main; lobby; option
menu_state = 'main'
selected_option = 0

# Menus
main_menu = MainMenu(window_width, window_height, font_title, font_options)

# Game loop
running = True
while running:
    main_menu.run_loop()

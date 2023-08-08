import pygame
from Configure.configure import load_configure_data
from Menu.main_menu import MainMenu
from Menu.lobby_menu import LobbyMenu
from Menu.options_menu import OptionsMenu
from Configure.language_config import *
from game import game
from campaign import running_campaign

# Initialize Pygame
pygame.init()

# Set the window size
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
main_menu = MainMenu(main_menu_options, window_width, window_height, font_title, font_options)
lobby_menu = LobbyMenu(lobby_menu_options, window_width, window_height, font_title, font_options)
options_menu = OptionsMenu(options_menu_options, window_width, window_height, font_title, font_options)

# Game loop
running = True
while running:

    if menu_state == 'main':
        menu_state = main_menu.events_handler(menu_state)
        main_menu.clear_screen(black)
        main_menu.render_options(white)
        main_menu.render_title(white)
        main_menu.render_version(white)
        main_menu.update_display()

    '''
    if menu_state == 'lobby':
        menu_state = lobby_menu.events_handler(menu_state)
        lobby_menu.clear_screen(black)
        lobby_menu.render_options(white)
        lobby_menu.update_display()
    '''
    if menu_state == "Free_play":
        menu_state = game(menu_state)
        menu_state = 'main'

    if menu_state == "campaign":
        image_path = 'Images\\Campaign_1'
        images = ['dream_TradingCard.jpg', 'dream_TradingCard(1).jpg', 'dream_TradingCard(3).jpg']
        menu_state = running_campaign(menu_state, 'Scenario\\scenario_01_pl.txt', image_path, images)
        menu_state = game(menu_state)
        images = ['dream_TradingCard(3).jpg', 'dream_TradingCard(4).jpg']
        if menu_state == 'end':
            menu_state = running_campaign(menu_state, 'Scenario\\scenario_02_pl.txt', image_path, images)

    if menu_state == 'options':
        menu_state, language = options_menu.events_handler(menu_state)

        if language == "english":
            # Set menu options
            main_menu.update_menu_options(ENGLISH_MAIN_MENU_OPTIONS)
            lobby_menu.update_menu_options([
                configure_data["player_name"],
                ENGLISH_LOBBY_MENU_OPTIONS[0],
                ENGLISH_LOBBY_MENU_OPTIONS[1],
                ENGLISH_LOBBY_MENU_OPTIONS[2]
            ])
            options_menu.update_menu_options([
                configure_data["player_name"],
                configure_data["language"],
                ENGLISH_OPTIONS_MENU_OPTIONS[0]
            ])
            lobby_menu.change_the_language_of_character_class_name_to_english()
        else:
            # Set menu options
            main_menu.update_menu_options(POLISH_MAIN_MENU_OPTIONS)
            lobby_menu.update_menu_options([
                configure_data["player_name"],
                POLISH_LOBBY_MENU_OPTIONS[0],
                POLISH_LOBBY_MENU_OPTIONS[1],
                POLISH_LOBBY_MENU_OPTIONS[2]
            ])
            options_menu.update_menu_options([
                configure_data["player_name"],
                configure_data["language"],
                POLISH_OPTIONS_MENU_OPTIONS[0]
            ])
            lobby_menu.change_the_language_of_character_class_name_to_polish()
        options_menu.clear_screen(black)
        options_menu.render_options(white)
        options_menu.update_display()

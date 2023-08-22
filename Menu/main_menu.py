import pygame
import sys
from campaign import running_campaign
from Configure.new_language_config import *
from game import Game
from Menu.menu import Menu
from Menu.options_menu import OptionsMenu


class MainMenu(Menu):
    def __init__(self, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Gochi Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        # Set menu
        self.title = 'Souls Reaper'
        self.options_menu = [languages[self.language.return_language()]['play'],
                             languages[self.language.return_language()]['campaign'],
                             languages[self.language.return_language()]['options'],
                             languages[self.language.return_language()]['exit']]
        self.selected_option = 0

    def run_loop(self):
        not_end_loop = True
        while not_end_loop:
            not_end_loop = self.events_handler()
            self.clear_screen()
            self.render_options()
            self.render_title()
            self.render_version()
            self.update_display()

    def select_option(self):
        if self.selected_option == 0:
            # Start Game
            game = Game(self.window, self.window_width, self.window_height)
            game.play()
        elif self.selected_option == 1:
            image_path = 'Images\\Campaign_1'
            images = ['dream_TradingCard.jpg', 'dream_TradingCard(1).jpg', 'dream_TradingCard(3).jpg']
            running_campaign('Scenario\\scenario_01_pl.txt', image_path, images)
            game = Game(self.window, self.window_width, self.window_height)
            game.play()
            images = ['dream_TradingCard(3).jpg', 'dream_TradingCard(4).jpg']
            running_campaign('Scenario\\scenario_02_pl.txt', image_path, images)
        elif self.selected_option == 2:
            # Option menu
            OptionsMenu(self.window_width, self.window_height, self.font_title,
                        self.font_options).run_loop()
            self.language.load_configure_language()
            self.options_menu = [languages[self.language.return_language()]['play'],
                                 languages[self.language.return_language()]['campaign'],
                                 languages[self.language.return_language()]['options'],
                                 languages[self.language.return_language()]['exit']]
        elif self.selected_option == 3:
            # Exit
            pygame.quit()
            sys.exit()

    def render_version(self):
        title_text = self.font_options.render("Alfa 0.1", True, self.white)
        title_text_rect = title_text.get_rect(center=(50, self.window_height - 50))
        self.window.blit(title_text, title_text_rect)

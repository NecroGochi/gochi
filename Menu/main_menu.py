import pygame
import sys
from campaign import running_campaign
from Configure.new_language_config import *
from game import game
from language import Language
from Menu.menu import Menu
from Menu.options_menu import OptionsMenu


class MainMenu(Menu):
    language = Language()

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
        self.menu_options = [languages[self.language.return_language()]['game'],
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

    def events_handler(self):
        not_end_loop = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                elif event.key == pygame.K_RETURN:
        return not_end_loop

    def select_option(self):
        if self.selected_option == 0:
            # Start Game
            menu_state = 'main_menu'
            menu_state = game(menu_state)
        elif self.selected_option == 1:
            menu_state = 'main_menu'
            image_path = 'Images\\Campaign_1'
            images = ['dream_TradingCard.jpg', 'dream_TradingCard(1).jpg', 'dream_TradingCard(3).jpg']
            menu_state = running_campaign(menu_state, 'Scenario\\scenario_01_pl.txt', image_path, images)
            menu_state = game(menu_state)
            images = ['dream_TradingCard(3).jpg', 'dream_TradingCard(4).jpg']
            if menu_state == 'end':
                menu_state = running_campaign(menu_state, 'Scenario\\scenario_02_pl.txt', image_path,
                                              images)
        elif self.selected_option == 2:
            # Option menu
            OptionsMenu(self.window_width, self.window_height, self.font_title,
                        self.font_options).run_loop()
            self.language.load_configure_language()
            self.menu_options = [languages[self.language.return_language()]['game'],
                                 languages[self.language.return_language()]['campaign'],
                                 languages[self.language.return_language()]['options'],
                                 languages[self.language.return_language()]['exit']]
        elif self.selected_option == 3:
            # Exit
            pygame.quit()
            sys.exit()

    def clear_screen(self):
        self.window.fill(self.black)

    def render_options(self):
        for position_number, option in enumerate(self.menu_options):
            color = self.is_selected(position_number)
            self.render_text(option, color, position_number, 0)

    def is_selected(self, position_number):
        if position_number == self.selected_option:
            color = self.white
        else:
            color = self.grey
        return color

    def render_text(self, _string, color, position_number, shift):
        text = self.font_options.render(_string, True, color)
        text_rect = text.get_rect(center=(self.window_width // 2, 200 + position_number * 50))
        self.window.blit(text, text_rect)

    def render_title(self):
        title_text = self.font_title.render("Souls Reaper", True, self.white)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

    def render_version(self):
        title_text = self.font_options.render("Alfa 0.1", True, self.white)
        title_text_rect = title_text.get_rect(center=(50, self.window_height - 50))
        self.window.blit(title_text, title_text_rect)

    def update_display(self):
        pygame.display.flip()

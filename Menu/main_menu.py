import pygame
import sys
from Menu.menu import Menu
from Menu.options_menu import OptionsMenu
from Configure.language_config import *


class MainMenu(Menu):

    def __init__(self, menu_options, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Gochi Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        self.menu_options = menu_options
        self.selected_option = 0

    def run_loop(self):
        self.events_handler()
        self.clear_screen()
        self.render_options()
        self.render_title()
        self.render_version()
        self.update_display()

    def events_handler(self, menu_state):
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
                    if self.selected_option == 0:
                        # Start Game
                        menu_state = 'Free_play'
                    elif self.selected_option == 1:
                        menu_state = 'campaign'
                    elif self.selected_option == 2:
                        # Option menu
                        language = OptionsMenu(self.window_width, self.window_height,
                                    self.font_title, self.font_options).run_loop()
                        if language == "english":
                            # Set menu options
                            self.update_menu_options(ENGLISH_MAIN_MENU_OPTIONS)
                        else:
                            # Set menu options
                            self.update_menu_options(POLISH_MAIN_MENU_OPTIONS)
                    elif self.selected_option == 3:
                        # Exit
                        pygame.quit()
                        sys.exit()
        return menu_state

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

    def update_menu_options(self, new_options):
        self.menu_options = new_options

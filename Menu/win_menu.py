import pygame
from Configure.new_language_config import *
from Menu.menu import Menu


class WinMenu(Menu):

    def __init__(self, window, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window_width = window_width
        self.window_height = window_height
        self.window = window
        pygame.display.set_caption("Gochi Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        # Set menu
        self.title = 'WIN'
        self.options_menu = [languages[self.language.return_language()]['exit']]
        self.selected_option = 0

    def run_loop(self):
        not_end_loop = True
        self.language.load_configure_language()
        self.options_menu = [languages[self.language.return_language()]['exit']]
        while not_end_loop:
            not_end_loop = self.events_handler()
            self.clear_screen()
            self.render_options()
            self.render_title()
            self.update_display()

    def select_option(self):
        not_end_loop = True
        if self.selected_option == 0:
            # Back to menu
            not_end_loop = False
        return not_end_loop

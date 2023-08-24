import pygame
from Configure.new_language_config import *
from Menu.menu import Menu


class DefeatedMenu(Menu):
    red = (155, 0, 0)
    title = 'DEFEATED!'

    def __init__(self, window, window_width, window_height, font_title, font_options):
        super().__init__(window, window_width, window_height, font_title, font_options)
        self.options_menu = [languages[self.language.return_language()]['exit']]

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

    def render_title(self):
        title_text = self.font_title.render(self.title, True, self.red)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

import pygame
import sys
from Configure.new_language_config import *
from Menu.menu import Menu


class WeaponLevelUpMenu(Menu):

    def __init__(self, window, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        pygame.display.set_caption("Level up menu Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        # Set Menu
        self.title = 'Weapon level up!'
        self.options_menu = [languages[self.language.return_language()]['back']]
        self.selected_option = 0

    def run_loop(self):
        not_end_loop = True
        item_number = -1
        self.language.load_configure_language()
        self.options_menu[len(self.options_menu) - 1] = languages[self.language.return_language()]['exit']
        while not_end_loop:
            not_end_loop, item_number = self.events_handler()
            self.clear_screen()
            self.render_options()
            self.update_display()
        return item_number

    def events_handler(self):
        not_end_loop = True
        item_number = -1
        for event in pygame.event.get():
            not_end_loop, item_number = self.happened(event)
        return not_end_loop, item_number

    def happened(self, event):
        not_end_loop = True
        item_number = -1
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            not_end_loop, item_number = self.triggered(event)
        return not_end_loop, item_number

    def triggered(self, event):
        not_end_loop = True
        item_number = -1
        if event.key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % len(self.options_menu)
        elif event.key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.options_menu)
        elif event.key == pygame.K_RETURN:
            not_end_loop, item_number = self.select_option()
        return not_end_loop, item_number

    def select_option(self):
        not_end_loop = True
        item_number = -1
        if self.selected_option < len(self.options_menu) - 1:
            item_number = self.selected_option
            not_end_loop = False
        if self.selected_option == len(self.options_menu) - 1:
            not_end_loop = False
        return not_end_loop, item_number

    def add_item_to_menu_option(self, item):
        self.options_menu.append(item)
        length = len(self.options_menu)
        self.options_menu = self.options_menu[:length - 2] + self.options_menu[length - 1:] \
                            + self.options_menu[length - 2:length - 1]

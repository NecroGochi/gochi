import pygame
import sys
from Configure.new_language_config import *
from Menu.menu import Menu
from Menu.new_weapon_menu import NewWeaponMenu
from Menu.weapon_level_up_menu import WeaponLevelUpMenu


class LevelUpMenu(Menu):
    title = 'Level up!'

    def __init__(self, window, window_width, window_height, font_title, font_options):
        super().__init__(window, window_width, window_height, font_title, font_options)
        self.options_menu = [languages[self.language.return_language()]['player_stat_level_up'],
                             languages[self.language.return_language()]['weapon_level_up'],
                             languages[self.language.return_language()]['new_weapon']]

        self.new_weapon_menu = NewWeaponMenu(self.window, self.window_width, self.window_height, self.font_title,
                                             self.font_options)
        self.weapon_level_up = WeaponLevelUpMenu(self.window, self.window_width, self.window_height, self.font_title,
                                                 self.font_options)

    def run_loop(self):
        not_end_loop = True
        item_number = -1
        option_number = [-1, item_number]
        self.language.load_configure_language()
        self.options_menu = [languages[self.language.return_language()]['player_stat_level_up'],
                             languages[self.language.return_language()]['weapon_level_up'],
                             languages[self.language.return_language()]['new_weapon']]
        while not_end_loop:
            not_end_loop, option_number = self.events_handler()
            self.clear_screen()
            self.render_options()
            self.update_display()
        return option_number

    def events_handler(self):
        item_number = -1
        option_number = [-1, item_number]
        for event in pygame.event.get():
            option_number = self.happened(event)
        not_end_loop = self.is_chosen(option_number[1])
        return not_end_loop, option_number

    def happened(self, event):
        item_number = -1
        option_number = [-1, item_number]
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            option_number = self.triggered(event)
        return option_number

    def triggered(self, event):
        item_number = -1
        option_number = [-1, item_number]
        if event.key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % len(self.options_menu)
        elif event.key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.options_menu)
        elif event.key == pygame.K_RETURN:
            option_number = self.select_option()
        return option_number

    def select_option(self):
        item_number = -1
        option_number = [-1, item_number]
        if self.selected_option == 0:
            item_number = 0
            option_number = [0, item_number]
        if self.selected_option == 1:
            item_number = self.weapon_level_up.run_loop()
            option_number = [1, item_number]
        if self.selected_option == 2:
            item_number = self.new_weapon_menu.run_loop()
            option_number = [2, item_number]
        return option_number

    @staticmethod
    def is_chosen(item_number):
        if item_number == -1:
            return True
        else:
            return False

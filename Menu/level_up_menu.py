import pygame
import sys
from Configure.new_language_config import *
from language import Language
from Menu.menu import Menu
from Menu.new_weapon_menu import NewWeaponMenu
from Menu.weapon_level_up_menu import WeaponLevelUpMenu


class LevelUpMenu(Menu):
    language = Language()

    def __init__(self, window, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        pygame.display.set_caption("Level up menu Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        self.menu_options = [languages[self.language.return_language()]['player_stat_level_up'],
                             languages[self.language.return_language()]['weapon_level_up'],
                             languages[self.language.return_language()]['new_weapon']]
        self.selected_option = 0

        self.new_weapon_menu = NewWeaponMenu(self.window, self.window_width, self.window_height, self.font_title,
                                             self.font_options)
        self.weapon_level_up = WeaponLevelUpMenu(self.window, self.window_width, self.window_height, self.font_title,
                                                 self.font_options)

    def run_loop(self):
        not_end_loop = True
        item_number = -1
        option_number = [-1, item_number]
        self.language.load_configure_language()
        self.menu_options = [languages[self.language.return_language()]['player_stat_level_up'],
                             languages[self.language.return_language()]['weapon_level_up'],
                             languages[self.language.return_language()]['new_weapon']]
        while not_end_loop:
            not_end_loop, option_number = self.events_handler()
            self.clear_screen()
            self.render_options()
            self.update_display()
        return option_number

    def events_handler(self):
        not_end_loop = True
        item_number = -1
        option_number = [-1, item_number]
        for event in pygame.event.get():
            not_end_loop, option_number = self.happened(event)
        not_end_loop = self.is_choosen(option_number[1])
        return not_end_loop, option_number

    def happened(self, event):
        not_end_loop = True
        item_number = -1
        option_number = [-1, item_number]
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            not_end_loop, option_number = self.triggered(event)
        return not_end_loop, option_number

    def triggered(self, event):
        not_end_loop = True
        item_number = -1
        option_number = [-1, item_number]
        if event.key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)
        elif event.key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)
        elif event.key == pygame.K_RETURN:
            not_end_loop, option_number = self.select_option()
        return not_end_loop, option_number

    def select_option(self):
        not_end_loop = True
        item_number = -1
        option_number = [-1, item_number]
        if self.selected_option == 0:
            not_end_loop, item_number = False, 0
            option_number = [0, item_number]
        if self.selected_option == 1:
            not_end_loop, item_number = self.weapon_level_up.run_loop()
            option_number = [1, item_number]
        if self.selected_option == 2:
            not_end_loop, item_number = self.new_weapon_menu.run_loop()
            option_number = [2, item_number]
        return not_end_loop, option_number

    def is_choosen(self, item_number):
        if item_number == -1:
            return True
        else:
            return False

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
        title_text = self.font_title.render("Level up!", True, self.white)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

    def update_display(self):
        pygame.display.flip()

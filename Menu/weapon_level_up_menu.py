import pygame
import sys
from Configure.new_language_config import *
from Menu.menu import Menu
from language import Language


class WeaponLevelUpMenu(Menu):
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

        self.menu_options = [languages[self.language.return_language()]['back']]
        self.selected_option = 0

    def run_loop(self):
        not_end_loop = True
        item_number = -1
        self.language.load_configure_language()
        self.menu_options[len(self.menu_options) - 1] = languages[self.language.return_language()]['exit']
        while not_end_loop:
            not_end_loop, item_number = self.events_handler()
            self.clear_screen()
            self.render_options()
            self.update_display()
        return not_end_loop, item_number

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
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)
        elif event.key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)
        elif event.key == pygame.K_RETURN:
            not_end_loop, item_number = self.select_option()
        return not_end_loop, item_number

    def select_option(self):
        not_end_loop = True
        item_number = -1
        if self.selected_option < len(self.menu_options) - 1:
            item_number = self.selected_option
            not_end_loop = False
        if self.selected_option == len(self.menu_options) - 1:
            not_end_loop = False
        return not_end_loop, item_number

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
        title_text = self.font_title.render("Weapon level up!", True, self.white)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

    def update_display(self):
        pygame.display.flip()

    def add_item_to_menu_option(self, item):
        self.menu_options.append(item)
        length = len(self.menu_options)
        self.menu_options = self.menu_options[:length - 2] + self.menu_options[length - 1:] \
                            + self.menu_options[length - 2:length - 1]

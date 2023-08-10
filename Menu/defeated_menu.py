import pygame
import sys
from Configure.new_language_config import *
from language import Language
from Menu.menu import Menu


class DefeatedMenu(Menu):
    red = (155, 0, 0)
    language = Language()

    def __init__(self, menu_options, window, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window_width = window_width
        self.window_height = window_height
        self.window = window
        pygame.display.set_caption("Gochi Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        # Set menu
        self.menu_options = [languages[self.language.return_language()]['exit']]
        self.selected_option = 0

    def events_handler(self, menu_state):
    def run_loop(self):
        not_end_loop = True
        self.menu_options = [languages[self.language.return_language()]['exit']]
        while not_end_loop:
            not_end_loop = self.events_handler()
            self.clear_screen()
            self.render_options()
            self.render_title()
            self.update_display()

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
                        # Back to menu
                        menu_state = 'main'
        return menu_state

    def clear_screen(self):
        self.window.fill(self.black)

    def render_options(self):
        for i, option in enumerate(self.menu_options):
            if i == self.selected_option:
                color = self.white
            else:
                color = self.grey
            self.render_text(option, color, i, 0)

    def render_text(self, _string, color, position_number, shift):
        text = self.font_options.render(_string, True, color)
        text_rect = text.get_rect(center=(self.window_width // 2, 200 + position_number * 50))
        self.window.blit(text, text_rect)

    def render_title(self):
        title_text = self.font_title.render("DEFEATED", True, self.red)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

    def update_display(self):
        pygame.display.flip()

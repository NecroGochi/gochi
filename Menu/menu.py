import pygame
import sys
from language import Language
from Menu.abstract_menu import AbstractMenu


class Menu(AbstractMenu):
    # colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (100, 100, 100)
    language = Language()

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
        self.title = 'Menu'
        self.options_menu = []
        self.selected_option = 0

    def run_loop(self):
        not_end_loop = True
        self.language.load_configure_language()
        self.options_menu = []
        while not_end_loop:
            not_end_loop = self.events_handler()
            self.clear_screen()
            self.render_options()
            self.update_display()

    def events_handler(self):
        not_end_loop = True
        for event in pygame.event.get():
            not_end_loop = self.happened(event)
        return not_end_loop

    def happened(self, event):
        not_end_loop = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            not_end_loop = self.triggered(event)
        return not_end_loop

    def triggered(self, event):
        not_end_loop = True
        if event.key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % len(self.options_menu)
        elif event.key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.options_menu)
        elif event.key == pygame.K_RETURN:
            not_end_loop = self.select_option()
        return not_end_loop

    def clear_screen(self):
        self.window.fill(self.black)

    def render_options(self):
        for position_number, option in enumerate(self.options_menu):
            color = self.is_selected(position_number)
            self.render_text(option, color, position_number, 0)

    def is_selected(self, position_number):
        if position_number == self.selected_option:
            return self.white
        else:
            return self.grey

    def render_text(self, _string, color, number_position, shift):
        text = self.font_options.render(_string, True, color)
        text_rect = text.get_rect(center=(self.window_width // 2, 200 + number_position * 50))
        self.window.blit(text, text_rect)

    def render_title(self):
        title_text = self.font_title.render(self.title, True, self.white)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

    def update_display(self):
        pygame.display.flip()

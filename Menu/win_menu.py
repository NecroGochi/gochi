import pygame
import sys
from Menu.menu import Menu


class WinMenu(Menu):

    def __init__(self, menu_options, window, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window_width = window_width
        self.window_height = window_height
        self.window = window
        pygame.display.set_caption("Gochi Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        self.menu_options = menu_options
        self.selected_option = 0


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
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)
        elif event.key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)
        elif event.key == pygame.K_RETURN:
            not_end_loop = self.select_option()
        return not_end_loop

    def select_option(self):
        not_end_loop = True
        if self.selected_option == 0:
            # Back to menu
            not_end_loop = False
        return not_end_loop

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
        title_text = self.font_title.render("WIN", True, self.white)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

    def update_display(self):
        pygame.display.flip()

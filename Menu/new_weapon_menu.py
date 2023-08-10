import pygame
import sys
from Menu.menu import Menu


class NewWeaponMenu(Menu):

    def __init__(self, menu_options, window, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        pygame.display.set_caption("New Weapon menu Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        self.name_field_rect = pygame.Rect(440 - 100, 185, 200, 30)
        self.menu_options = menu_options
        self.selected_option = 0
        self.name_player = menu_options[0]
        self.name_active = False

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
                    if self.selected_option < len(self.menu_options) - 1:
                        menu_state = str(self.selected_option)
                    if self.selected_option == len(self.menu_options) - 1:
                        menu_state = "pause"
        return menu_state

    def clear_screen(self, color):
        self.window.fill(color)

    def render_options(self, color_selected_button):
        for i, option in enumerate(self.menu_options):
            if i == self.selected_option:
                color = color_selected_button
            else:
                color = (100, 100, 100)
            self.render_text(option, color, i, 0)

    def render_text(self, _string, color, position_number, shift):
        text = self.font_options.render(_string, True, color)
        text_rect = text.get_rect(center=(self.window_width // 2, 200 + position_number * 50))
        self.window.blit(text, text_rect)

    def render_title(self, color):
        title_text = self.font_title.render("New weapon!", True, color)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

    def update_display(self):
        pygame.display.flip()

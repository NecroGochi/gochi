import pygame
import sys
from Menu.menu import Menu
from Menu.language_config import ENGLISH_CHARACTER_CLASS, POLISH_CHARACTER_CLASS


class LobbyMenu(Menu):

    def __init__(self, menu_options, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Gochi Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        self.name_field_rect = pygame.Rect(440 - 100, 185, 200, 30)
        self.menu_options = menu_options
        self.selected_option = 0
        self.name_player = menu_options[0]
        self.name_active = False
        if menu_options[1] == 'english':
            self.character_class = ENGLISH_CHARACTER_CLASS
        else:
            self.character_class = POLISH_CHARACTER_CLASS
        self.selected_character_class = 0

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
                    if self.selected_option == 0:
                        # Start Game
                        self.name_active = not self.name_active
                    elif self.selected_option == 1:
                        if self.selected_character_class + 1 == 12:
                            self.selected_character_class = 0
                        else:
                            self.selected_character_class = self.selected_character_class + 1
                    elif self.selected_option == 2:
                        print("start game")
                    elif self.selected_option == 3:
                        # Back to previous menu
                        menu_state = 'main'

                elif event.key == pygame.K_BACKSPACE:
                    # Pressing Backspace will remove the last character from the name field
                    if self.name_active:
                        self.name_player = self.name_player[:-1]
                else:
                    # Other key presses will append the character to the name field
                    if self.name_active:
                        self.name_player += event.unicode
        return menu_state

    def clear_screen(self, color):
        self.window.fill(color)

    def render_options(self, color_selected_button):
        for i, option in enumerate(self.menu_options):
            if i == self.selected_option:
                color = color_selected_button
            else:
                color = (100, 100, 100)
            if i == 0:
                self.render_name_field(color)
                self.render_text("Player: ", color, i, -100)
            elif i == 1:
                self.render_text(option, color, i, -70)
                self.render_text(self.character_class[self.selected_character_class], color, i, 70)
            else:
                self.render_text(option, color, i, 0)

    def render_text(self, _string, color, position_number, shift):
        text = self.font_options.render(_string, True, color)
        text_rect = text.get_rect(center=(self.window_width // 2 + shift, 200 + position_number * 50))
        self.window.blit(text, text_rect)

    def render_title(self, color):
        title_text = self.font_title.render("Pygame Menu", True, color)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

    def render_name_field(self, color):
        if self.name_active:
            color = (255, 0, 0)
        pygame.draw.rect(self.window, color, self.name_field_rect, 2)
        name_text = self.font_options.render(self.name_player, True, color)
        self.window.blit(name_text, (self.name_field_rect.x + 5, self.name_field_rect.y + 5))

    def update_display(self):
        pygame.display.flip()

    def update_menu_options(self, new_options):
        self.menu_options = new_options

    def change_the_language_of_character_class_name_to_polish(self):
        self.character_class = POLISH_CHARACTER_CLASS

    def change_the_language_of_character_class_name_to_english(self):
        self.character_class = ENGLISH_CHARACTER_CLASS


import pygame
import sys
from Menu.menu import Menu
from Configure.configure import change_configure_file


class OptionsMenu(Menu):

    def __init__(self, menu_options, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Gochi Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options

        self.menu_options = menu_options
        self.selected_option = 0

        # Create a rectungular box for the name field
        self.name_field_rect = pygame.Rect(440 - 100, 185, 200, 30)
        self.name_player = menu_options[0]
        self.language = menu_options[1]
        self.languages = ['english', 'polski']
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
                    if self.selected_option == 0:
                        # Pressing Enter will toggle the active state of the name field
                        self.name_active = not self.name_active
                    elif self.selected_option == 1:
                        if self.language == self.languages[0]:
                            self.language = 'polski'
                        else:
                            self.language = 'english'
                    elif self.selected_option == 2:
                        # Back to previous menu
                        menu_state = 'main'
                        change_configure_file("player_name", self.name_player)
                        change_configure_file("language", self.language)
                elif event.key == pygame.K_BACKSPACE:
                    # Pressing Backspace will remove the last character from the name field
                    if self.name_active:
                        self.name_player = self.name_player[:-1]
                else:
                    # Other key presses will append the character to the name field
                    if self.name_active:
                        self.name_player += event.unicode
        return menu_state, self.language

    def clear_screen(self):
        self.window.fill(self.black)

    def render_options(self):
        for i, option in enumerate(self.menu_options):
            color_option = self.grey
            if i == self.selected_option:
                color_option = self.white
            if i == 0:
                self.render_name_field(color_option)
                self.render_text("Player: ", color_option, i, -100)
            elif i == 1:
                color_polish = self.grey
                color_english = self.grey
                if self.language == self.languages[0]:
                    color_polish = color_option
                    self.render_text_with_line(self.languages[0], color_polish, i, -50)
                    self.render_text(self.languages[1], color_english, i, 50)
                if self.language == self.languages[1]:
                    color_english = color_option
                    self.render_text(self.languages[0], color_polish, i, -50)
                    self.render_text_with_line(self.languages[1], color_english, i, 50)
            else:
                self.render_text(option, color_option, i, 0)

    def render_text(self, _string, color, position_number, shift):
        text = self.font_options.render(_string, True, color)
        text_rect = text.get_rect(center=(self.window_width // 2 + shift, 200 + position_number * 50))
        self.window.blit(text, text_rect)

    def render_text_with_line(self, _string, color, position_number, shift):
        text = self.font_options.render(_string, True, color)
        text_rect = text.get_rect(center=(self.window_width // 2 + shift, 200 + position_number * 50))
        self.window.blit(text, text_rect)
        line_y = text_rect.bottomleft[1] + 2
        pygame.draw.line(self.window, color, (text_rect.left, line_y), (text_rect.right, line_y))

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

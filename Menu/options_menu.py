import pygame
import sys
from Configure.configure import change_configure_file, load_configure_data
from Configure.new_language_config import *
from Menu.menu import Menu
from language import Language


class OptionsMenu(Menu):
    # Set static values
    red = (255, 0, 0)
    language = Language()

    def __init__(self, window_width, window_height, font_title, font_options):
        # Set the window size
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Gochi Game")

        # Set Fonts
        self.font_title = font_title
        self.font_options = font_options
        self.selected_option = 0

        # Set options
        self.options_menu = [languages[self.language.return_language()]['player_name'],
                             languages[self.language.return_language()]['language'],
                             languages[self.language.return_language()]['back']]

        # Set player name rectangular
        self.name_player = load_configure_data()['player_name']
        self.name_field_rect = pygame.Rect(440 - 100, 185, 200, 30)
        self.name_active = False

        # Set language choose
        self.languages_choose = ['english', 'polish']

    def run_loop(self):
        not_end_loop = True
        while not_end_loop:
            not_end_loop = self.events_handler()
            self.clear_screen()
            self.render_options()
            self.update_display()

    def events_handler(self):
        not_end_loop = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
        return not_end_loop
    
    def triggered(self, event):
        not_end_loop = True
        if event.key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % len(self.options_menu)
        elif event.key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.options_menu)
        elif event.key == pygame.K_RETURN:
            not_end_loop = self.select_option()
        elif event.key == pygame.K_BACKSPACE:
            # Pressing Backspace will remove the last character from the name field
            self.delete_char_player_name()
        else:
            # Other key presses will append the character to the name field
            self.write_char_player_name(event)
        return not_end_loop

    def select_option(self):
        if self.selected_option == 0:
            # Pressing Enter will toggle the active state of the name field
            self.name_active = not self.name_active
        elif self.selected_option == 1:
            self.select_language_option()
        elif self.selected_option == 2:
            # Back to previous menu
            change_configure_file("player_name", self.name_player)
            return False
        return True

    def delete_char_player_name(self):
        if self.name_active:
            self.name_player = self.name_player[:-1]

    def write_char_player_name(self, event):
        if self.name_active:
            self.name_player += event.unicode

    def select_language_option(self):
        if self.language.return_language() == self.languages_choose[0]:
            self.language.change_language('polish')
            self.options_menu = [languages['polish']['player_name'],
                                 languages['polish']['language'],
                                 languages['polish']['back']]
        else:
            self.language.change_language('english')
            self.options_menu = [languages['english']['player_name'],
                                 languages['english']['language'],
                                 languages['english']['back']]

    def clear_screen(self):
        self.window.fill(self.black)

    def render_options(self):
        for position_number, option in enumerate(self.options_menu):
            color = self.is_selected(position_number)
            self.render_option(position_number, color)

    def is_selected(self, position_number):
        if position_number == self.selected_option:
            return self.white
        else:
            return self.grey

    def render_option(self, position_number, color):
        if position_number == 0:
            self.render_name_field(color)
            self.render_text(self.options_menu[position_number], color, position_number, -200)
        elif position_number == 1:
            self.render_text(self.options_menu[position_number], color, position_number, -300)
            self.choose_language(color, position_number)
        else:
            self.render_text(self.options_menu[position_number], color, position_number, 0)

    def render_name_field(self, color):
        if self.name_active:
            color = self.red
        pygame.draw.rect(self.window, color, self.name_field_rect, 2)
        name_text = self.font_options.render(self.name_player, True, color)
        self.window.blit(name_text, (self.name_field_rect.x + 5, self.name_field_rect.y + 5))

    def choose_language(self, color_option, position_number):
        color_polish = self.grey
        color_english = self.grey
        if self.language.return_language() == self.languages_choose[0]:
            color_polish = color_option
            self.render_text_with_line(self.languages_choose[0], color_polish, position_number, -50)
            self.render_text(self.languages_choose[1], color_english, position_number, 50)
        if self.language.return_language() == self.languages_choose[1]:
            color_english = color_option
            self.render_text(self.languages_choose[0], color_polish, position_number, -50)
            self.render_text_with_line(self.languages_choose[1], color_english, position_number, 50)

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

    def render_title(self):
        title_text = self.font_title.render("Pygame Menu", True, self.white)
        title_text_rect = title_text.get_rect(center=(self.window_width // 2, 100))
        self.window.blit(title_text, title_text_rect)

    def update_display(self):
        pygame.display.flip()

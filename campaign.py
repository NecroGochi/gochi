import sys
import re
from sprites.creatures.character import *


class Campaign:
    # colors:
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Set the text display area
    text_padding = 20
    text_font = pygame.font.Font(None, 32)

    # Set the name display area
    name_padding = 20
    name_font = pygame.font.Font(None, 36)

    pattern = re.compile(r'(\[(.*)\])?([/>]{3})?(.*)')
    running = False

    # Set text
    line = 0
    next_line_of_text = ''
    next_name = ''

    # Set picture
    num_image = 0
    image_scale = {
        'x': 240,
        'y': 392
    }
    image_position = {
        'x': 360,
        'y': 0
    }

    def __init__(self, window, window_width, window_height, image_path, images):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        # Set the text display area
        self.text_area = pygame.Rect(0, self.window_height // 4 * 3,
                                     window_width, 170)
        # Set the name display area
        self.name_area = pygame.Rect(0, self.window_height // 4 * 3 - 40,
                                     150, 40)
        self.image_path = image_path
        self.images = images
        self.image = pygame.transform.scale(pygame.image.load(self.image_path + '\\' + self.images[self.num_image]),
                                            (self.image_scale['x'], self.image_scale['y']))
        self.count_images = len(images)

    def display_text(self, text):
        # Clear the text area
        pygame.draw.rect(self.window, self.white, self.text_area)
        # Render the text
        text_lines = text.split('$')
        current_line = self.text_area.y + self.text_padding
        for text_line in text_lines:
            text_surface = self.text_font.render(text_line, True, self.black)
            self.window.blit(text_surface, (self.text_area.x + self.text_padding, current_line))
            current_line += text_surface.get_height() + self.text_padding

    def display_name(self, text):
        # Clear the text area
        pygame.draw.rect(self.window, self.white, self.name_area)
        # Render the text
        text_lines = text.split('$')
        current_line = self.name_area.y + self.name_padding
        for text_line in text_lines:
            name_surface = self.name_font.render(text_line, True, self.black)
            self.window.blit(name_surface, (self.name_area.x + self.name_padding, current_line))
            current_line += name_surface.get_height() + self.name_padding

    def advance_text(self, next_line_of_text, next_name):
        self.display_text(next_line_of_text)
        if next_name != '':
            self.display_name(next_name)

    @staticmethod
    def load_scenario_file(path):
        # load conf file
        try:
            with open(path, 'r', encoding='utf-8') as scenario:
                scenario_file = []
                for line in scenario:
                    scenario_file.append(line)
                return scenario_file
        except IOError:
            print("Scenario didn't open")
            return dict()

    def running_campaign(self, text_path):
        # Game loop
        scenario = self.load_scenario_file(text_path)
        self.image = pygame.transform.scale(pygame.image.load(self.image_path + '\\' + self.images[self.num_image]),
                                            (self.image_scale['x'], self.image_scale['y']))
        self.running = True
        while self.running:
            self.events_handler(scenario)

            # Clear the screen
            self.window.fill(self.black)
            self.window.blit(self.image, (self.image_position['x'], self.image_position['y']))
            self.advance_text(self.next_line_of_text, self.next_name)
            # Update the display
            pygame.display.flip()

    def events_handler(self, scenario):
        for event in pygame.event.get():
            self.happened(event, scenario)

    def happened(self, event, scenario):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self.triggered(event, scenario)

    def triggered(self, event, scenario):
        if event.key == pygame.K_SPACE:
            # Advance the text when the Space key is pressed
            self.next_scene(scenario)

    def next_scene(self, scenario):
        next_picture = ''
        if self.line < len(scenario):
            prepared_text = re.findall(self.pattern, scenario[self.line])
            next_picture = prepared_text[0][2]
            self.next_line_of_text = prepared_text[0][3]
            self.next_name = prepared_text[0][1]
            self.line += 1
        else:
            self.running = False
        if next_picture == '>>>' and self.count_images > self.num_image + 1:
            self.num_image += 1
            self.image = pygame.transform.scale(pygame.image.load(self.image_path + '\\' + self.images[self.num_image]),
                                                (self.image_scale['x'], self.image_scale['y']))

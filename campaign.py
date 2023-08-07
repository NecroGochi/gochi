import sys
import re
import pygame
from board import *
from character import *


# Initialize Pygame
pygame.init()

# Set the window size
window_width = 192 * 5
window_height = 108 * 5
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Camera Scrolling")

# Set the text display area
text_area_width = window_width
text_area_height = 170
text_area_x = (window_width - text_area_width) // 2
text_area_y = (window_height - text_area_height) // 2 + 200
text_area_color = (255, 255, 255)
text_color = (0, 0, 0)
text_padding = 20
text_font = pygame.font.Font(None, 32)

# Set the name display area
name_area_width = 150
name_area_height = 40
name_area_x = (window_width - text_area_width) // 2
name_area_y = (window_height - text_area_height) // 2 + 160
name_area_color = (255, 255, 255)
name_color = (0, 0, 0)
name_padding = 20
name_font = pygame.font.Font(None, 36)

pattern = re.compile(r'(\[(.*)\])?([/>]{3})?(.*)')


def display_text(text):
    # Clear the text area
    pygame.draw.rect(window, text_area_color, (text_area_x, text_area_y, text_area_width, text_area_height))
    # Render the text
    lines = text.split('$')
    y = text_area_y + text_padding
    for line in lines:
        text_surface = text_font.render(line, True, text_color)
        window.blit(text_surface, (text_area_x + text_padding, y))
        y += text_surface.get_height() + text_padding

    # Update the display
    #pygame.display.flip()


def display_name(text):
    # Clear the text area
    pygame.draw.rect(window, name_area_color, (name_area_x, name_area_y, name_area_width, name_area_height))

    # Render the text
    lines = text.split('$')
    y = name_area_y + name_padding
    for line in lines:
        name_surface = name_font.render(line, True, name_color)
        window.blit(name_surface, (name_area_x + name_padding, y))
        y += name_surface.get_height() + name_padding

    # Update the display
    #pygame.display.flip()


def advance_text(next_line_of_text, next_name):
    display_text(next_line_of_text)
    if next_name != '':
        display_name(next_name)


# Set colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set font
font = pygame.font.Font(None, 32)

# Set Fonts
font_title = pygame.font.Font(None, 64)
font_options = pygame.font.Font(None, 32)


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


def running_campaign(menu_state, text_path, image_path, images):
    # Set initial player position
    start_time = pygame.time.get_ticks()
    menu_state = "not pause"
    # Game loop
    running = True
    scenario = load_scenario_file(text_path)
    next_line_of_text = ""
    next_name = ""
    next_picture = ""
    line = 0
    num_image = 0
    count_images = len(images)
    scale_x = 240
    scale_y = 392
    image = pygame.transform.scale(pygame.image.load(image_path + '\\' + images[num_image]), (scale_x, scale_y))
    image_x = 360
    image_y = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Advance the text when the Space key is pressed
                    if line < len(scenario):
                        prepared_text = re.findall(pattern, scenario[line])
                        next_picture = prepared_text[0][2]
                        next_line_of_text = prepared_text[0][3]
                        next_name = prepared_text[0][1]
                        line += 1
                    else:
                        running = False
                    if next_picture == '>>>' and count_images > num_image + 1:
                        num_image += 1
                        image = pygame.transform.scale(pygame.image.load(image_path + '\\' + images[num_image]),
                                                       (scale_x, scale_y))

        # Clear the screen
        window.fill(black)
        window.blit(image, (image_x, image_y))
        advance_text(next_line_of_text, next_name)
        # Update the display
        pygame.display.flip()
    menu_state = 'main'
    return menu_state

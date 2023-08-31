from sprites.items.areaweapon import *
import pygame


class Character(Sprite):
    pygame.init()

    black = (0, 0, 0)
    green = (0, 155, 155)
    red = (155, 0, 0)

    health_point_y_bar_size = 10

    font_options = pygame.font.Font(None, 32)

    experience_increase_multiplier = 1000

    flip_image = False
    number_image = 0
    velocity_x = 0
    velocity_y = 0

    def __init__(self, hero, level, actual_experience_points, board_width, board_height):
        # Set player properties
        self.size = hero['Size']
        self.health_points = hero['HP']
        self.actual_health_points = hero['HP']
        self.attack = hero['AP']
        self.defense = hero['DP']
        self.speed = hero['Speed']
        self.actual_experience_points = actual_experience_points
        self.max_experience_points = hero['Max_Exp']
        self.level = level
        self.bonus_level = hero['Bonus_level']

        self.sprite_images = self.load_images(hero['Images'])

        # shifting the render position - centering the hitbox
        self.render_shit = self.size // 4
        self.hitbox = pygame.Rect(board_width // 2, board_height // 2, self.size // 2, self.size // 2)

        self.items = []

    @staticmethod
    def load_images(images):
        python_images = []
        for each in images:
            python_images.append(pygame.image.load(each))
        return python_images

    def add_item(self, item):
        self.items.append(item)
        self.items[len(self.items)-1].left = self.items[0].left

    # Function to render the player
    def render(self, window, board_camera_x, board_camera_y):
        actual_health_point_bar = (self.hitbox.x - board_camera_x - self.render_shit,
                                   self.hitbox.y + self.size - board_camera_y - self.render_shit,
                                   self.actual_health_points * self.size / self.health_points,
                                   self.health_point_y_bar_size)
        lost_health_point_bar = (self.hitbox.x - board_camera_x - self.render_shit +
                                 self.actual_health_points * self.size / self.health_points,
                                 self.hitbox.y + self.size - board_camera_y - self.render_shit,
                                 (self.health_points - self.actual_health_points) * self.size / self.health_points,
                                 self.health_point_y_bar_size)
        self.render_character(window, board_camera_x, board_camera_y)
        self.render_bar(actual_health_point_bar, window, self.green)
        self.render_bar(lost_health_point_bar, window, self.red)

    def render_character(self, window, board_camera_x, board_camera_y):
        image = self.sprite_images[self.number_image]
        image = pygame.transform.scale(image, (self.size, self.size))
        image = pygame.transform.flip(image, self.flip_image, False)
        window.blit(image, (self.hitbox.x - board_camera_x - self.render_shit,
                            self.hitbox.y - board_camera_y - self.render_shit))
        if self.number_image == len(self.sprite_images) - 1:
            self.number_image = 0
        else:
            self.number_image += 1

    @staticmethod
    def render_bar(bar, window, color):
        pygame.draw.rect(window, color, bar)

    def render_text(self, _string, color, window, board_camera_x, board_camera_y):
        text = self.font_options.render(_string, True, color)
        text_rect = text.get_rect(center=(self.hitbox.x - board_camera_x - self.render_shit,
                                          self.hitbox.y + self.size - board_camera_y - self.render_shit))
        window.blit(text, text_rect)

    def go_left(self):
        self.velocity_x = self.speed
        self.flip_image = True

    def go_right(self):
        self.velocity_x = -self.speed
        self.flip_image = False

    def go_up(self):
        self.velocity_y = self.speed

    def go_down(self):
        self.velocity_y = -self.speed

    def update_position(self):
        self.hitbox.x += self.velocity_x
        self.hitbox.y += self.velocity_y

    def collide_board(self, down_board_border, up_board_border, right_board_border, left_board_border):
        # board border
        if down_board_border < self.hitbox.x:
            self.velocity_x = 0
            self.hitbox.x = down_board_border
        if up_board_border > self.hitbox.x:
            self.velocity_x = 0
            self.hitbox.x = up_board_border
        if right_board_border < self.hitbox.y:
            self.velocity_y = 0
            self.hitbox.y = right_board_border
        if left_board_border > self.hitbox.y:
            self.velocity_y = 0
            self.hitbox.y = left_board_border

    def collide_enemy(self, enemy, time, hit, enemy_attack):
        if self.hitbox.colliderect(enemy) and time % 2 == 0 and hit:
            self.actual_health_points = self.actual_health_points - (max(1, round(enemy_attack, self.defense)))

    def get_experience_points(self, experience_points):
        self.actual_experience_points += experience_points

    def get_level(self):
        self.level = self.level + self.actual_experience_points // self.max_experience_points
        self.actual_experience_points = self.actual_experience_points % self.max_experience_points
        self.max_experience_points = self.level * self.experience_increase_multiplier

    def grow_stat(self):
        self.actual_health_points += self.bonus_level['health']
        self.attack += self.bonus_level['attack']
        self.defense += self.bonus_level['defense']
        self.speed += self.bonus_level['speed']

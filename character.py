from orbitingweapon import *
from shootingweapon import *
from areaweapon import *
import pygame


class Character(Sprite):
    def __init__(self, board_width, board_height):
        # Set player properties
        self.size = 100
        self.hp = 49000
        self.actual_hp = 49000
        self.ap = 13
        self.defense = 4
        self.speed = 9
        self.actual_exp = 0
        self.max_exp = 1000
        self.level = 1
        # hp, ap, defence, speed
        self.bonus_level = [3, 5, 2, 1]
        self.flip_image = False

        self.image_sprite = [
            pygame.image.load("Images/Heroes/nekromanta_1.png"),
            pygame.image.load("Images/Heroes/nekromanta_2.png")
        ]
        self.number_image = 0

        # shifting the render position - centering the hitbox
        self.render_shit = self.size // 4
        self.hitbox = pygame.Rect(board_width // 2, board_height // 2, self.size // 2, self.size // 2)
        self.velocity_x = 0
        self.velocity_y = 0

        self.items = [
            OrbitingWeapon(self.hitbox.x, self.hitbox.y),
        ]

    # Function to render the player
    def render(self, window, color, board_camera_x, board_camera_y):
        self.render_character(window, color, board_camera_x, board_camera_y)
        if self.actual_hp > self.actual_hp * 0.1:
            self.render_hp_bar(window, (0, 155, 155), board_camera_x, board_camera_y)
        else:
            self.render_hp_bar(window, (155, 0, 0), board_camera_x, board_camera_y)

    def render_character(self, window, color, board_camera_x, board_camera_y):
        '''pygame.draw.rect(window, color,
                         (self.hitbox.x - board_camera_x - self.render_shit,
                          self.hitbox.y - board_camera_y - self.render_shit,
                          self.size, self.size))
        '''
        image = self.image_sprite[self.number_image]
        image = pygame.transform.scale(image, (self.size, self.size))
        image = pygame.transform.flip(image, self.flip_image, False)
        window.blit(image, (self.hitbox.x - board_camera_x - self.render_shit,
                          self.hitbox.y - board_camera_y - self.render_shit))
        if self.number_image == 0:
            self.number_image = 1
        else:
            self.number_image = 0

    def render_hp_bar(self, window, color, board_camera_x, board_camera_y):
        pygame.draw.rect(window, color,
                         (self.hitbox.x - board_camera_x - self.render_shit,
                          self.hitbox.y + self.size - board_camera_y - self.render_shit,
                          self.actual_hp * self.size / self.hp, 10))

    def render_text(self, _string, color, window, board_camera_x, board_camera_y):
        font_options = pygame.font.Font(None, 32)
        text = font_options.render(_string, True, color)
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

    def collide_board(self, board_border_x1, board_border_x2, board_border_y1, board_border_y2):
        # board border
        if board_border_x1 < self.hitbox.x:
            self.velocity_x = 0
            self.hitbox.x = board_border_x1
        if board_border_x2 > self.hitbox.x:
            self.velocity_x = 0
            self.hitbox.x = board_border_x2
        if board_border_y1 < self.hitbox.y:
            self.velocity_y = 0
            self.hitbox.y = board_border_y1
        if board_border_y2 > self.hitbox.y:
            self.velocity_y = 0
            self.hitbox.y = board_border_y2

    def collide_enemy(self, enemy, time, hit, enemy_attack):
        if self.hitbox.colliderect(enemy) and time % 2 == 0 and hit:
            self.actual_hp = self.actual_hp - (max(1, round(enemy_attack, self.defense)))

    def get_exp(self, exp):
        self.actual_exp += exp

    def get_level(self):
        self.level = self.level + self.actual_exp // self.max_exp
        self.actual_exp = self.actual_exp % self.max_exp
        self.max_exp = self.level * 1000

    def grow_stat(self):
        self.actual_hp += self.bonus_level[0]
        self.ap += self.bonus_level[1]
        self.defense += self.bonus_level[2]
        self.speed += self.bonus_level[3]

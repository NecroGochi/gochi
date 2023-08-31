import pygame
import math
from sprites.items.weapon import *


class ShootingWeapon(Weapon):
    black = (0, 0, 0)
    actual_distance = 0
    max_quantity = 5
    left = True
    angle_offset = 0.2
    hit = True
    number_image = 0

    def __init__(self, position_x, position_y):
        self.name = "Possessed card"
        self.type = "Rect"
        self.distance = 300
        self.quantity = 1
        self.image_weapon = self.load_images(item['Images'])
        self.position_x = position_x + self.distance
        self.position_y = position_y + self.distance
        self.angle = float((2.0 / float(self.quantity)) * 3.14) / 2
        self.angles_right = [0]
        self.angles_left = [self.angle]
        self.angles = self.angles_left
        self.hitbox = [
            pygame.Rect(position_x * math.cos(self.angles[0]),
                        position_y * math.sin(self.angles[0]), 20, 28)
        ]
        self.level = 1
        self.power = 20
        self.speed = 10
        self.bonus_level = [5]

    @staticmethod
    def load_images(images):
        python_images = []
        for each in images:
            python_images.append(pygame.image.load(each))
        return python_images

    def render(self, window, board_camera_x, board_camera_y):
        for each in self.hitbox:
            image = self.image_weapon[self.number_image]
            image = pygame.transform.scale(image, (each[2], each[2]))
            window.blit(image, (each[0] - board_camera_x,
                                each[1] - board_camera_y))

    def move(self, player_position_x, player_position_y, player_velocity_x, player_velocity_y):
        number = 0
        self.is_range_reached(player_position_x, player_position_y)
        for each in self.hitbox:
            each.x = each.x + self.speed * math.cos(self.angles[number]) + player_velocity_x * 2
            each.y = each.y + self.speed * math.sin(self.angles[number]) + player_velocity_y * 2
            number += 1
        self.actual_distance += self.speed

    def is_range_reached(self, player_position_x, player_position_y):
        if self.actual_distance >= self.distance:
            self.check_quantity()
            self.initialize_start_position(player_position_x, player_position_y)
            self.actual_distance = 0

    def check_quantity(self):
        if self.quantity > len(self.hitbox):
            self.add_item()

    def add_item(self):
        if self.level % 2 == 0:
            self.angles_right.pop()
            self.angles_right.append(self.angle * (0.0 + (self.quantity / 2) * self.angle_offset))
            self.angles_right.append(self.angle * (2.0 - (self.quantity / 2) * self.angle_offset))
            self.angles_left.pop()
            self.angles_left.append(self.angle * (1.0 + (self.quantity / 2) * self.angle_offset))
            self.angles_left.append(self.angle * (1.0 - (self.quantity / 2) * self.angle_offset))
        else:
            self.angles_right.append(0)
            self.angles_left.append(self.angle)
        self.choose_angles_by_direction()

    def choose_angles_by_direction(self):
        if self.left:
            self.angles = self.angles_left
        else:
            self.angles = self.angles_right

    def initialize_start_position(self, player_position_x, player_position_y):
        self.hitbox = []
        for each in range(self.quantity):
            self.choose_angles_by_direction()
            self.hitbox.append(pygame.Rect(player_position_x, player_position_y, self.width, self.length))

    def get_level(self):
        self.power += self.bonus_level["power"]
        self.level += 1
        self.quantity += 1

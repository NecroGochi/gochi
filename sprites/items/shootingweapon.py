import pygame
import math
from sprites.items.weapon import *


class ShootingWeapon(Weapon):
    black = (0, 0, 0)
    actual_distance = 0
    max_quantity = 5
    left = True
    angle_offset = 0.2
    length = 28
    width = 20
    hit = True
    type = 'Shooting'

    def __init__(self, item, level, position_x, position_y):
        self.name = item['Name']
        self.shape = item['Shape']
        self.distance = item['Distance_from_player']
        self.quantity = item['Quantity']
        self.power = item['Power']
        self.speed = item['Speed']
        self.bonus_level = item['Bonus_level']
        self.images = self.load_images(item['Images'])
        self.level = level
        self.position_x = position_x + self.distance
        self.position_y = position_y + self.distance
        self.angle = float((2.0 / float(self.quantity)) * 3.14) / 2
        self.angles_right = [0]
        self.angles_left = [self.angle]
        self.angles = self.angles_left
        self.hitbox = [
            pygame.Rect(position_x,
                        position_y, self.width, self.length)
        ]

    def move(self, player_position_x, player_position_y, player_velocity_x, player_velocity_y):
        number = 0
        self.is_range_reached(player_position_x, player_position_y)
        for each in self.hitbox:
            previous_x = each.x
            each.x = each.x + self.speed * math.cos(self.angles[number]) + player_velocity_x * 2
            each.y = each.y + self.speed * math.sin(self.angles[number]) + player_velocity_y * 2
            number += 1
            if previous_x > each.x:
                self.flip_image = True
            else:
                self.flip_image = False
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

import pygame
import math
from sprites.items.weapon import *


class ShootingWeapon(Weapon):
    black = (0, 0, 0)
    left = True

    def __init__(self, position_x, position_y):
        self.name = "Possessed card"
        self.type = "Rect"
        self.distance = 300
        self.actual_distance = 0
        self.quantity = 1
        self.max_quantity = 5
        self.position_x = position_x + self.distance
        self.position_y = position_y + self.distance
        self.angle = float((2.0 / float(self.quantity)) * 3.14) / 2
        self.angles_right = [0]
        self.angles_left = [self.angle]
        self.angles = self.angles_left
        self.angle_offset = 0.1
        self.hitbox = [
            pygame.Rect(position_x * math.cos(self.angles[0]),
                        position_y * math.sin(self.angles[0]), 20, 28)
        ]
        self.level = 1
        self.power = 20
        self.speed = 10
        self.bonus_level = [5]
        self.hit = True
        self.image_weapon = pygame.image.load("Images/Monsters/karta.png")

    def render(self, window, board_camera_x, board_camera_y):
        for each in self.hitbox:
            image = self.image_weapon
            image = pygame.transform.scale(image, (each[2], each[2]))
            pygame.draw.rect(window, self.black,
                             (each.x - board_camera_x,
                              each.y - board_camera_y, each.height,
                              each.width))
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

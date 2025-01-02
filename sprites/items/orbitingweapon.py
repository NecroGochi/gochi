import pygame
import math
from sprites.items.weapon import *


class OrbitingWeapon(Weapon):
    black = (0, 0, 0)
    left = True
    length = 60
    width = 40
    hit = True
    type = "Orbiting"

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
        self.angle = float((2.0 / float(self.quantity)) * 3.14)
        self.angles = [self.angle * 0]
        self.hitbox = [
            pygame.Rect(self.position_x * math.cos(self.angles[0]),
                        self.position_y * math.sin(self.angles[0]), self.width, self.length),
                       ]

    def move(self, player_position_x, player_position_y):
        number = 0
        for each in self.hitbox:
            self.angles[number] += self.speed  # Angular speed
            each.x = player_position_x + self.distance * math.cos(self.angles[number])
            each.y = player_position_y + self.distance * math.sin(self.angles[number])
            number += 1

    def get_level(self):
        self.power += self.bonus_level["power"]
        self.speed += self.bonus_level["speed"]
        self.level += 1
        if self.level <= 6:
            self.add_item()

    def add_item(self):
        self.quantity += 1
        self.angle = float((2.0 / float(self.quantity)) * 3.14)
        angles = []
        for each in range(self.quantity):
            angles.append(self.angle * each)
        self.angles = angles
        hitbox = []
        for each in self.angles:
            hitbox.append(pygame.Rect(self.position_x * math.cos(each),
                                      self.position_y * math.sin(each), self.width, self.length))
        self.hitbox = hitbox

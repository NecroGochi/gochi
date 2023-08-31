import pygame
import math
from sprites.items.weapon import *


class OrbitingWeapon(Weapon):
    black = (0, 0, 0)
    left = True
    length = 60
    width = 40
    hit = True
    number_image = 0

    def __init__(self, item, level, position_x, position_y):
        self.name = item['Name']
        self.type = item['Shape']
        self.distance = item['Distance_from_player']
        self.quantity = item['Quantity']
        self.power = item['Power']
        self.speed = item['Speed']
        self.bonus_level = item['Bonus_level']
        self.image_weapon = self.load_images(item['Images'])
        self.level = level
        self.position_x = position_x + self.distance
        self.position_y = position_y + self.distance
        self.angle = float((2.0 / float(self.quantity)) * 3.14)
        self.angles = [self.angle * 0]
        self.hitbox = [
            pygame.Rect(self.position_x * math.cos(self.angles[0]),
                        self.position_y * math.sin(self.angles[0]), self.width, self.length),
                       ]

    @staticmethod
    def load_images(images):
        python_images = []
        for each in images:
            python_images.append(pygame.image.load(each))
        return python_images

    def render(self, window, board_camera_x, board_camera_y):
        for each in self.hitbox:
            image = self.image_weapon[self.number_image]
            image = pygame.transform.scale(image, (each[2], each[3]))
            pygame.draw.rect(window, self.black,
                             (each.x - board_camera_x,
                              each.y - board_camera_y, each.width,
                              each.height))
            window.blit(image, (each[0] - board_camera_x,
                                each[1] - board_camera_y))

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

import pygame
import math
from sprite import *


class OrbitingWeapon(Sprite):
    def __init__(self, position_x, position_y):
        self.name = "Possessed book"
        self.type = "Rect"
        self.distance = 150
        self.quantity = 1
        self.position_x = position_x + self.distance
        self.position_y = position_y + self.distance
        self.angle = float((2.0 / float(self.quantity)) * 3.14)
        self.left = 1
        self.angles = [self.angle * 0]
        self.hitbox = [
            pygame.Rect(self.position_x * math.cos(self.angles[0]),
                        self.position_y * math.sin(self.angles[0]), 40, 60),
                       ]
        self.level = 1
        self.power = 20
        self.speed = 0.02
        self.bonus_level = [2, 0.02]
        self.hit = True
        self.image_weapon = pygame.image.load("Images/Monsters/ksiazka.png")

    def render(self, window, color, board_camera_x, board_camera_y):
        for each in self.hitbox:
            image = self.image_weapon
            image = pygame.transform.scale(image, (each[2], each[3]))
            pygame.draw.rect(window, color,
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
        self.power += self.bonus_level[0]
        self.speed += self.bonus_level[1]
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
                            self.position_y * math.sin(each), 40, 60))
            self.hitbox = hitbox

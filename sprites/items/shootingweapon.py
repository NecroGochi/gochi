import pygame
import math
from sprites.creatures.sprite import *


class ShootingWeapon(Sprite):
    def __init__(self, position_x, position_y):
        self.name = "Possessed card"
        self.type = "Rect"
        self.distance = 300
        self.actual_distance = 0
        self.quantity = 1
        self.position_x = position_x + self.distance
        self.position_y = position_y + self.distance
        self.angle = float((2.0 / float(self.quantity)) * 3.14) / 2
        self.left = 1
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
        self.hit = True
        self.image_weapon = pygame.image.load("Images/Monsters/karta.png")

    def render(self, window, color, board_camera_x, board_camera_y):
        for each in self.hitbox:
            image = self.image_weapon
            image = pygame.transform.scale(image, (each[2], each[2]))
            pygame.draw.rect(window, color,
                             (each.x - board_camera_x,
                              each.y - board_camera_y, each.height,
                              each.width))
            window.blit(image, (each[0] - board_camera_x,
                                each[1] - board_camera_y))

    def move(self, player_position_x, player_position_y):
        number = 0
        for each in self.hitbox:
            each.x = player_position_x + (self.actual_distance + self.speed) * math.cos(self.angles[number])
            each.y = player_position_y + (self.actual_distance + self.speed) * math.sin(self.angles[number])
            self.actual_distance += self.speed
            number += 1
            if self.actual_distance >= self.distance:
                self.actual_distance = 0
                self.hitbox.remove(each)
                self.hitbox.append(pygame.Rect(player_position_x, player_position_y, 20, 28))
    def choose_angles(self):
        if self.left == 1:
            self.angles = self.angles_left
        else:
            self.angles = self.angles_right

    def get_level(self):
        self.power += self.bonus_level[0]
        self.level += 1
        if self.level == 2:
            self.quantity += 1
            self.angles_right = [self.angle * 1.91, 0.79]
            self.angles_left = [self.angle * 1.25, self.angle * 0.75]
            if self.left == 1:
                self.angles = self.angles_left
            else:
                self.angles = self.angles_right
            hitbox = []
            for each in self.angles:
                hitbox.append(pygame.Rect(self.position_x * math.cos(each),
                                          self.position_y * math.sin(each), 20, 28))
            self.hitbox = hitbox
        if self.level == 3:
            self.quantity += 1
            self.angles_right = [0, self.angle * 0.33, self.angle * 1.66]
            self.angles_left = [self.angle, self.angle * 0.66, self.angle * 1.33]
            if self.left == 1:
                self.angles = self.angles_left
            else:
                self.angles = self.angles_right
            hitbox = []
            for each in self.angles:
                hitbox.append(pygame.Rect(self.position_x * math.cos(each),
                                          self.position_y * math.sin(each), 20, 28))
            self.hitbox = hitbox
        if self.level == 4:
            self.quantity += 1
            self.angles_right = [self.angle * 0.08, self.angle * 0.25, self.angle * 1.92, self.angle * 1.75]
            self.angles_left = [self.angle * 0.92, self.angle * 0.75, self.angle * 1.08, self.angle * 1.25]
            if self.left == 1:
                self.angles = self.angles_left
            else:
                self.angles = self.angles_right
            hitbox = []
            for each in self.angles:
                hitbox.append(pygame.Rect(self.position_x * math.cos(each),
                                          self.position_y * math.sin(each), 20, 28))
            self.hitbox = hitbox
        if self.level == 5:
            self.quantity += 1
            self.angles_right = [0, self.angle * 0.16, self.angle * 0.33, self.angle * 1.83, self.angle * 1.67]
            self.angles_left = [self.angle, self.angle * 0.83, self.angle * 0.66, self.angle * 1.17, self.angle * 1.33]
            if self.left == 1:
                self.angles = self.angles_left
            else:
                self.angles = self.angles_right
            hitbox = []
            for each in self.angles:
                hitbox.append(pygame.Rect(self.position_x * math.cos(each),
                                          self.position_y * math.sin(each), 20, 28))
            self.hitbox = hitbox

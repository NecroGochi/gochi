import pygame
from sprites.items.weapon import *


class AreaWeapon(Weapon):
    type = "Area"

    def __init__(self, position_x, position_y):
        self.name = "Cup of cold coffe"
        self.shape = "Circle"
        self.left = True
        self.hitbox = [
            [position_x, position_y, 100]
        ]
        self.image_scale = 2
        self.level = 1
        self.power = 1
        self.bonus_level = [1, 10]
        self.render_shift = 10
        self.render_image_shift = 90
        self.image_weapon = pygame.image.load("Images/Monsters/mrozona_kawa.png")

    def render(self, window, board_camera_x, board_camera_y):
        for each in self.hitbox:
            image = self.image_weapon
            image = pygame.transform.scale(image, (each[2] * self.image_scale, each[2] * self.image_scale))
            image.set_alpha(200)
            window.blit(image, (each[0] - board_camera_x - self.render_image_shift,
                                each[1] - board_camera_y - self.render_image_shift))

    def move(self, player_position_x, player_position_y):
        for each in self.hitbox:
            each[0] = player_position_x
            each[1] = player_position_y

    def get_level(self):
        self.power += self.bonus_level[0]
        self.level += 1
        if self.level <= 6:
            self.hitbox[0][2] += self.bonus_level[1]
            self.render_image_shift += self.bonus_level[1]

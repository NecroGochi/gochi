import pygame
from sprites.items.weapon import *


class AreaWeapon(Weapon):
    type = "Area"
    left = True
    radius = 100
    image_scale = 2
    render_shift = 10
    render_image_shift = 90
    alpha = 200
    number_image = 0

    def __init__(self, item, level, position_x, position_y):
        self.name = item["Name"]
        self.shape = item["Shape"]
        self.power = item["Power"]
        self.bonus_level = item["Bonus_level"]
        self.image_weapon = self.load_images(item['Images'])
        self.level = level
        self.hitbox = [
            [position_x, position_y, self.radius]
        ]

    def render(self, window, board_camera_x, board_camera_y):
        for each in self.hitbox:
            image = self.image_weapon[self.number_image]
            image = pygame.transform.scale(image, (each[2] * self.image_scale, each[2] * self.image_scale))
            image.set_alpha(self.alpha)
            window.blit(image, (each[0] - board_camera_x - self.render_image_shift,
                                each[1] - board_camera_y - self.render_image_shift))

    def move(self, player_position_x, player_position_y):
        for each in self.hitbox:
            each[0] = player_position_x
            each[1] = player_position_y

    def get_level(self):
        self.power += self.bonus_level["power"]
        self.level += 1
        if self.level <= 6:
            self.hitbox[0][2] += self.bonus_level["range"]
            self.render_image_shift += self.bonus_level["range"]

from sprites.items.weapon import *


class AreaWeapon(Weapon):
    type = "Area"
    left = True
    radius = 100
    flip_image = False

    def __init__(self, item, level, position_x, position_y):
        self.name = item["Name"]
        self.shape = item["Shape"]
        self.power = item["Power"]
        self.bonus_level = item["Bonus_level"]
        self.images = self.load_images(item['Images'])
        self.level = level
        self.hitbox = [
            [position_x, position_y, self.radius, self.radius]
        ]
        self.render_image_shift = 90
        self.alpha = 200
        self.image_scale = 2

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

from enemy import *


class Boss(Enemy):
    def __init__(self, position_x, position_y, size, color, speed, ap, dp, hp, exp, image):
        # Set player properties
        self.size = size
        self.image = color
        self.speed = speed
        self.hit = True
        self.ap = ap
        self.dp = dp
        self.hp = hp
        self.actual_hp = hp
        self.boss = True
        self.exp = exp
        self.final_boss = False

        self.image_sprite = pygame.image.load(image)
        self.flip_image = False

        # Set initial player position
        self.hitbox = pygame.Rect(position_x, position_y, self.size, self. size)

    def render_hp_bar(self, window, color, board_camera_x, board_camera_y):
        pygame.draw.rect(window, color,
                         (self.hitbox.x - board_camera_x,
                          self.hitbox.y + self.size - board_camera_y,
                          self.actual_hp * self.size / self.hp, 10))

    def is_final_boss(self):
        self.final_boss = True


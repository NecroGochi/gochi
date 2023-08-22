from sprites.creatures.enemy import *


class Boss(Enemy):
    health_point_y_bar_size = 10

    def __init__(self, position_x, position_y, size, color, speed, attack, defense, health, experience, image):
        # Set player properties
        self.size = size
        self.image = color
        self.speed = speed
        self.hit = True
        self.attack = attack
        self.defense = defense
        self.health_points = health
        self.actual_health_points = health
        self.boss = True
        self.experience = experience
        self.final_boss = False

        self.image_sprite = pygame.image.load(image)
        self.flip_image = False

        # Set initial player position
        self.hitbox = pygame.Rect(position_x, position_y, self.size, self. size)

    def render_hp_bar(self, window, color, board_camera_x, board_camera_y):
        pygame.draw.rect(window, color,
                         (self.hitbox.x - board_camera_x,
                          self.hitbox.y + self.size - board_camera_y,
                          self.actual_health_points * self.size / self.health_points, self.health_point_y_bar_size))

    def is_final_boss(self):
        self.final_boss = True


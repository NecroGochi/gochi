from sprites.creatures.enemy import *


class Boss(Enemy):
    health_point_y_bar_size = 10
    boss = True
    final_boss = False

    def __init__(self, position_x, position_y, size, color, speed, attack, defense, health, experience, image):
        super().__init__(position_x, position_y, size, color, speed, attack, defense, health, experience, image)

    def render_hp_bar(self, window, color, board_camera_x, board_camera_y):
        pygame.draw.rect(window, color,
                         (self.hitbox.x - board_camera_x,
                          self.hitbox.y + self.size - board_camera_y,
                          self.actual_health_points * self.size / self.health_points, self.health_point_y_bar_size))

    def is_final_boss(self):
        self.final_boss = True

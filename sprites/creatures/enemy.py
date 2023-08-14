from sprites.creatures.sprite import Sprite
import pygame
import math


class Enemy(Sprite):
    def __init__(self, position_x, position_y, size, color, speed, ap, dp, hp, exp, image):
        # Set player properties
        self.size = size
        self.color = color
        self.speed = speed
        self.hit = True
        self.ap = ap
        self.dp = dp
        self.hp = hp
        self.actual_hp = hp
        self.boss = False
        self.exp = exp

        self.image_sprite = pygame.image.load(image)
        self.flip_image = False

        # Set initial player position
        self.hitbox = pygame.Rect(position_x, position_y, self.size, self. size)

    # Function to render the player
    def render(self, window, board_camera_x, board_camera_y):
        image = self.image_sprite
        image = pygame.transform.scale(image, (self.size, self.size))
        image = pygame.transform.flip(image, self.flip_image, False)

        window.blit(image, (self.hitbox.x - board_camera_x,
                            self.hitbox.y - board_camera_y))

    def move(self, player_position_x, player_position_y, player_velocity_x, player_velocity_y):
        previous_x = self.hitbox.x
        enemy_x = self.hitbox.x
        enemy_y = self.hitbox.y
        angle = math.atan2(player_position_y - self.hitbox.y, player_position_x - self.hitbox.x)

        # Calculate the velocities in the x and y directions
        velocity_x = self.speed * math.cos(angle)
        velocity_y = self.speed * math.sin(angle)

        # Update the enemy positions based on the velocities
        enemy_x += velocity_x
        enemy_y += velocity_y

        self.hitbox.x = enemy_x + player_velocity_x * 2
        self.hitbox.y = enemy_y + player_velocity_y * 2

        if previous_x > self.hitbox.x:
            self.flip_image = True
        else:
            self.flip_image = False

    def collide_weapon(self, weapon, weapon_attack):
        if self.hitbox.colliderect(weapon):
            self.actual_hp = self.actual_hp - (max(1, round(weapon_attack, self.dp)))

    def collide_weapon_circle(self, weapon, weapon_attack):
        distance = math.sqrt((weapon[0] - self.hitbox.x) ** 2 + (weapon[1] - self.hitbox.y) ** 2)
        if distance < weapon[2] + self.size:
            self.actual_hp = self.actual_hp - (max(1, round(weapon_attack, self.dp)))

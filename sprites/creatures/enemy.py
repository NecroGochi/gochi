from sprites.sprite import Sprite
import pygame
import math


class Enemy(Sprite):
    boss = False
    hit = True

    def __init__(self, position_x, position_y, size, speed, attack, defense, health, experience, image):
        # Set player properties
        self.size = size
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.health_points = health
        self.actual_health_points = health
        self.experience = experience
        self.images = self.load_images(image)
        # Set initial player position
        self.hitbox = [pygame.Rect(position_x, position_y, self.size, self. size)]

    def move(self, player_position_x, player_position_y, player_velocity_x, player_velocity_y):
        previous_x = self.hitbox[0].x
        enemy_x = self.hitbox[0].x
        enemy_y = self.hitbox[0].y
        angle = math.atan2(player_position_y - self.hitbox[0].y, player_position_x - self.hitbox[0].x)

        # Calculate the velocities in the x and y directions
        velocity_x = self.speed * math.cos(angle)
        velocity_y = self.speed * math.sin(angle)

        # Update the enemy positions based on the velocities
        enemy_x += velocity_x
        enemy_y += velocity_y

        self.hitbox[0].x = enemy_x + player_velocity_x * 2
        self.hitbox[0].y = enemy_y + player_velocity_y * 2

        if previous_x > self.hitbox[0].x:
            self.flip_image = True
        else:
            self.flip_image = False

    def collide_weapon(self, weapon, attack_points):
        if self.hitbox[0].colliderect(weapon):
            self.actual_health_points = self.actual_health_points - (max(1, round(attack_points - self.defense, 0)))

    def collide_weapon_circle(self, weapon_position, attack_points):
        if self.calculate_delta_for_x(weapon_position) >= 0 or self.calculate_delta_for_y(weapon_position) >= 0:
            self.actual_health_points = self.actual_health_points - (max(1, round(attack_points - self.defense, 0)))

    def calculate_delta_for_x(self, weapon_position):
        a = 1
        b = float(-2.0 * float(weapon_position[0]))
        c = float(weapon_position[0]) ** 2 - (float(weapon_position[2]) ** 2 -
                                              (float(weapon_position[1]) - float(self.hitbox[0].y)) ** 2)
        delta = b ** 2 - (4 * a * c)
        return delta

    def calculate_delta_for_y(self, weapon_position):
        a = 1
        b = float(-2.0 * float(weapon_position[1]))
        c = float(weapon_position[1]) ** 2 - (float(weapon_position[2]) ** 2 -
                                              (float(weapon_position[0]) - float(self.hitbox[0].x)) ** 2)
        delta = b ** 2 - (4 * a * c)
        return delta


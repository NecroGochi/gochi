import pygame


class Board:
    def __init__(self, window_width, window_height, border_x1, border_y1, border_x2, border_y2):
        # Set board properties
        self.width = 192 * 10
        self.height = 108 * 10

        # Set camera properties
        self.camera_width = window_width
        self.camera_height = window_height
        self.camera_x = 0
        self.camera_y = 0

        # Set background properties
        self.background = pygame.image.load("Images\\Plansza.png")
        self.background = pygame.transform.scale_by(self.background, 1)
        self.background_x = self.camera_x - 960
        self.background_y = self.camera_y - 540

        # Set border
        self.border_x1 = border_x1
        self.border_y1 = border_y1
        self.border_x2 = border_x2
        self.border_y2 = border_y2

    def update_camera_position(self, position_player_x, position_player_y):
        self.camera_x = position_player_x - self.camera_width // 2
        self.camera_y = position_player_y - self.camera_height // 2

    def update_background_position(self):
        self.background_x = self.camera_x - 960
        self.background_y = self.camera_y - 540

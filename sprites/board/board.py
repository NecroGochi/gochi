import pygame


class Board:
    centering = {
        'x': 960,
        'y': 540
    }
    scale = 2
    camera_x = 0
    camera_y = 0

    def __init__(self, window_width, window_height, obstacles, board_picture):
        # Set board properties
        self.width = window_width * self.scale
        self.height = window_height * self.scale

        # Set camera properties
        self.camera_width = window_width
        self.camera_height = window_height

        # Set background properties
        self.background = pygame.image.load(board_picture)
        self.background = pygame.transform.scale_by(self.background, 1)
        self.background_x = self.camera_x - self.centering['x']
        self.background_y = self.camera_y - self.centering['y']

        # Set obstacles
        self.obstacles = obstacles

    def update_camera_position(self, position_player_x, position_player_y):
        self.camera_x = position_player_x - self.camera_width // 2
        self.camera_y = position_player_y - self.camera_height // 2

    def update_background_position(self):
        self.background_x = self.camera_x - self.centering['x']
        self.background_y = self.camera_y - self.centering['y']

import pygame


class Board:
    centering = {
        'x': 960,
        'y': 540
    }

    def __init__(self, window_width, window_height, down_board_border, right_board_border, up_board_border,
                 left_board_border):
        # Set board properties
        self.width = 192 * 10
        self.height = 108 * 10

        # Set camera properties
        self.camera_width = window_width
        self.camera_height = window_height
        self.camera_x = 0
        self.camera_y = 0

        # Set background properties
        self.background = pygame.image.load("Images/Boards/Plansza.png")
        self.background = pygame.transform.scale_by(self.background, 1)
        # 960
        self.background_x = self.camera_x - self.centering['x']
        self.background_y = self.camera_y - self.centering['y']

        # Set border
        self.down_border = down_board_border
        self.right_border = right_board_border
        self.up_border = up_board_border
        self.left_border = left_board_border

    def update_camera_position(self, position_player_x, position_player_y):
        self.camera_x = position_player_x - self.camera_width // 2
        self.camera_y = position_player_y - self.camera_height // 2

    def update_background_position(self):
        self.background_x = self.camera_x - self.centering['x']
        self.background_y = self.camera_y - self.centering['y']

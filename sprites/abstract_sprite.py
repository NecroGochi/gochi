from abc import ABC, abstractclassmethod


class Sprite(ABC):

    def render(self, window, board_camera_x, board_camera_y):
        pass
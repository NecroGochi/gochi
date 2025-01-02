import pygame


class Sprite:
    hitbox = []
    images = []
    number_image = 0
    image_scale = 1
    alpha = 255
    render_image_shift = 0
    flip_image = False

    @staticmethod
    def load_images(images):
        python_images = []
        for each in images:
            python_images.append(pygame.image.load(each))
        return python_images

    def render(self, window, board_camera_x, board_camera_y):
        for each in self.hitbox:
            image_render = self.images[self.number_image]
            image_render = pygame.transform.scale(image_render, (each[2] * self.image_scale,
                                                                 each[3] * self.image_scale))
            image_render = pygame.transform.flip(image_render, self.flip_image, False)
            image_render.set_alpha(self.alpha)
            window.blit(image_render, (each[0] - board_camera_x - self.render_image_shift,
                                       each[1] - board_camera_y - self.render_image_shift))



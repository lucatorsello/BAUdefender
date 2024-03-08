import pygame
from pygame import Surface


class Entity:
    def __init__(
        self,
        sprite: str,
        window: Surface,
        x_pos: int = None,
        y_pos: int = None,
    ):

        self.sprite = pygame.image.load(sprite)
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.window = window

    def render(self):
        if self.x_pos:
            self.window.blit(self.sprite, (self.x_pos, self.y_pos))
        else:
            window_width = self.window.get_width()
            window_height = self.window.get_height()
            sprite_width = self.sprite.get_width()
            sprite_height = self.sprite.get_height()
            sprite_x = (window_width - sprite_width) // 2
            sprite_y = (window_height - sprite_height) // 2
            self.window.blit(self.sprite, (sprite_x, sprite_y))

    def collision(): ...

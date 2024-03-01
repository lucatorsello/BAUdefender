import os
import pygame
from pygame.time import Clock
from pygame.surface import Surface

from event_handling import handle_events


def game_loop(window: Surface, clock: Clock, FPS: int):
    current_dir = os.path.dirname(__file__)
    grass = pygame.image.load(f"{current_dir}/graphics/grass.png").convert()
    game_runnning = True
    c = 0
    while game_runnning:
        c += 0.5
        scroll_x = c % grass.get_width()
        scroll_y = 0
        x = -scroll_x
        while x < window.get_width():
            y = -scroll_y
            while y < window.get_height():
                window.blit(grass, (x, y))
                y += grass.get_height()
            x += grass.get_width()

        clock.tick(FPS)
        game_runnning = handle_events()
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

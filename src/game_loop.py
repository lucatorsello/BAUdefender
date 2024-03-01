import os
import pygame
from pygame.time import Clock
from pygame.surface import Surface


from event_handling import handle_events


def game_loop(window: Surface, clock: Clock, FPS: int):
    current_dir = os.path.dirname(__file__)
    grass = pygame.image.load(f"{current_dir}/graphics/grass3.png").convert()
    game_runnning = True
    x_distance = 0
    y_distance = 0
    x_move = 0
    y_move = 0
    speed = 0.5
    while game_runnning:
        game_runnning, x_move, y_move = handle_events(x_move=x_move, y_move=y_move)

        x_distance += speed * x_move
        y_distance += speed * y_move
        scroll_x = x_distance % grass.get_width()
        scroll_y = y_distance % grass.get_width()
        x = 0

        # as scroll increases blit on new x and y range
        while x < window.get_width() + 100:
            y = 0
            while y < window.get_height() + 100:
                window.blit(grass, (x - scroll_x, y - scroll_y))
                y += grass.get_height()
            x += grass.get_width()

        clock.tick(FPS)
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

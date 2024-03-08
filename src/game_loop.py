import os
import random
import pygame
from pygame.time import Clock
from pygame.surface import Surface


from event_handling import handle_events
from entity.player.player import PlayerEntity
from entity.enemy.enemy import EnemyEntity


def game_loop(window: Surface, clock: Clock, FPS: int):
    current_dir = os.path.dirname(__file__)
    grass = pygame.image.load(f"{current_dir}/graphics/grass3.png").convert()
    game_runnning = True
    x_distance = 0
    y_distance = 0
    x_move = 0
    y_move = 0
    speed = 0.5
    enemy_speed = 0.5
    window_width = window.get_width()
    window_height = window.get_height()
    enemies = []

    while game_runnning:
        game_runnning, x_move, y_move = handle_events(x_move=x_move, y_move=y_move)
        x_distance += speed * x_move
        y_distance += speed * y_move
        scroll_x = x_distance % grass.get_width()
        scroll_y = y_distance % grass.get_width()
        padding = 50
        x = 0
        player = PlayerEntity(
            sprite=f"{current_dir}/graphics/grass2.png", window=window
        )
        if len(enemies) == 0:
            for n in range(100):
                if random.choice([True, False]):
                    if random.choice([True, False]):
                        random_x = random.randint(-padding, 0)
                        random_y = random.randint(0, window_height)
                    else:
                        random_x = random.randint(window_width, window_width + padding)
                        random_y = random.randint(0, window_height)
                else:
                    if random.choice([True, False]):
                        random_y = random.randint(-padding, 0)
                        random_x = random.randint(0, window_width)
                    else:
                        random_y = random.randint(
                            window_height,
                            window_height + padding,
                        )
                        random_x = random.randint(0, window_width)
                enemies.append(
                    EnemyEntity(
                        sprite=f"{current_dir}/graphics/grass.png",
                        window=window,
                        x_pos=random_x,
                        y_pos=random_y,
                        speed=enemy_speed,
                    ),
                )
        # as scroll increases blit on new x and y range
        while x < window.get_width() + 100:
            y = 0
            while y < window.get_height() + 100:
                window.blit(grass, (x - scroll_x, y - scroll_y))
                y += grass.get_height()
            x += grass.get_width()

        clock.tick(FPS)
        for enemy in enemies:
            enemy.render()
            enemy.move()
            print(f"enemy {enemy} rendered")
        player.render()
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

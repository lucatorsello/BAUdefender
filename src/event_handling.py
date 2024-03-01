import pygame


def handle_events(x_move, y_move):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, 0, 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x_move += 1
            if event.key == pygame.K_a:
                x_move += -1
            if event.key == pygame.K_s:
                y_move += 1
            if event.key == pygame.K_w:
                y_move += -1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                x_move += -1
            if event.key == pygame.K_a:
                x_move += +1
            if event.key == pygame.K_s:
                y_move += -1
            if event.key == pygame.K_w:
                y_move += +1
    return True, x_move, y_move

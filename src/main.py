import pygame
from game_loop import game_loop


def main():
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 60
    display_info = pygame.display.Info()
    width, height = display_info.current_w, display_info.current_h
    window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption("game")

    game_loop(window, clock, FPS)


if __name__ == "__main__":
    main()

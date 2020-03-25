import sys
import pygame
from chapter12.settings import Settings
from chapter12.ship import Ship
import chapter12.game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_height, ai_setting.screen_width))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:
        gf.check_events(ship)
        gf.update_screen(ai_setting, screen, ship)


run_game()

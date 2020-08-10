import pygame

from controllers.game_manager import GameManager
from controllers.screen_controller import ScreenController
from utils.const import SCREEN_SIZE
from utils.logger import logger



if __name__ == '__main__':
    logger.info("game Start")

    pygame.init()
    screen_controller = ScreenController()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    while GameManager.getInstance().running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("game screen is done by QUIT")
                GameManager.getInstance().running = False
            screen_controller.update_event(event)

        screen_controller.update()
        screen_controller.draw(screen)
        pygame.display.update()

    GameManager.getInstance().save_state()
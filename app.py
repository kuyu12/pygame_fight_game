import pygame
from pydispatch import dispatcher

from controllers.stage_controller import StageController
from utils.utils_factory import UtilsFactory
from utils.logger import logger

# TODO:
# player data controller
# attack reaction

if __name__ == '__main__':
    logger.info("Game Start")
    pygame.init()
    running = True

    player_data = UtilsFactory.get_player_data('Frozen')
    stage_data = UtilsFactory.get_state_data(1)
    stage_controller = StageController(stage_data,player_data)
    screen = pygame.display.set_mode(stage_data.background.size)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Game screen is done by QUIT")
                running = False
            stage_controller.update_event(event)

        stage_controller.update()
        stage_controller.draw(screen)
        pygame.display.update()


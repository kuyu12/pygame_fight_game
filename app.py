import pygame
from controllers.collision_controller import CollisionController
from controllers.sprite_controller import SpriteController
from controllers.stage_controller import StageController
from utils.utils_factory import UtilsFactory
from views.gui_views.user_info_view import UserInfoView
from controllers.player_controller import PlayerController
from views.sprite_views.enemy_sprite import EnemySprite
from views.sprite_views.user_sprite import UserSprite

# TODO:
# player data controller
# attack reaction


pygame.init()
running = True

player_data = UtilsFactory.get_player_data('Frozen')
stage_data = UtilsFactory.get_state_data(1)
stage_controller = StageController(stage_data,player_data)

screen = pygame.display.set_mode(stage_data.background.size)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        stage_controller.update_event(event)

    stage_controller.update()
    stage_controller.draw(screen)
    # screen.blit(view, (0, 0))
    pygame.display.update()

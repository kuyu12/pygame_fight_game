import pygame
from controllers.collision_controller import CollisionController
from controllers.sprite_controller import SpriteController
from utils.utils_factory import UtilsFactory
from views.gui_views.user_info_view import UserInfoView
from controllers.player_controller import PlayerController
from views.sprite_views.enemy_sprite import EnemySprite
from views.sprite_views.user_sprite import UserSprite

# TODO:
# Create state creator
# player data controller
# attack reaction


pygame.init()

running = True

player_data = UtilsFactory.get_player_data('Frozen')
stage_data = UtilsFactory.get_state_data(1)

player = UserSprite(stage_data, player_data)
player_controller = PlayerController(player)
view = UserInfoView((270, 100), player_data)

enemy_data = UtilsFactory.get_player_data('Grey')
enemy = EnemySprite((600, 600), stage_data.background.size, enemy_data, player)

sprite_controller = SpriteController(stage_data.background, player, enemy)
collision_controller = CollisionController(sprite_controller)

screen = pygame.display.set_mode(stage_data.background.size)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player_controller.update_event(event)

    sprite_controller.update()
    sprite_controller.draw(screen)
    collision_controller.update()
    screen.blit(view, (0, 0))
    pygame.display.update()

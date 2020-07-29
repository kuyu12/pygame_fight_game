import pygame

from controllers.collision_controller import CollisionController
from controllers.player_controller import PlayerController
from controllers.sprite_controller import SpriteController
from utils.color import BLACK, WHITE
from utils.const import USER_INFO_SIZE
from views.gui_views.user_info_view import UserInfoView
from views.sprite_views.user_sprite import UserSprite


class StageController:
    def __init__(self, stage_data, player_data):
        self.stage_data = stage_data
        self.player_data = player_data

        self.user_sprite = UserSprite(self.stage_data, self.player_data)
        self.sprite_controller = SpriteController(self.stage_data.background, self.user_sprite)
        self.player_controller = PlayerController(self.user_sprite)
        self.collision_controller = CollisionController(self.sprite_controller)

        self.user_info_view = UserInfoView(USER_INFO_SIZE, self.player_data)

        # enemy_data = UtilsFactory.get_player_data('Grey')
        # enemy = EnemySprite((600, 600), stage_data.background.size, enemy_data, player)

    def update(self):
        self.sprite_controller.update()
        self.collision_controller.update()

    def draw(self, surface):
        self.sprite_controller.draw(surface)
        surface.blit(self.user_info_view, (0, 0))

    def update_event(self, event):
        self.player_controller.update_event(event)

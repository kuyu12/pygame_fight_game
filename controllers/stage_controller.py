import uuid

from controllers.collision_controller import CollisionController
from controllers.player_controller import PlayerController
from controllers.sprite_controller import SpriteController
from model.game_state import GameState
from utils.const import USER_INFO_SIZE
from utils.json_mappers.stage_json_mapper import SignalMapper
from utils.utils_factory import UtilsFactory
from views.gui_views.stage_headline import StageHeadline
from views.gui_views.user_info_view import UserInfoView
from views.sprite_views.enemy_sprite import EnemySprite
from views.sprite_views.user_sprite import UserSprite
from utils.logger import logger
from pydispatch import dispatcher

class StageController:

    def __init__(self, stage_data, player_data):
        logger.info("StageController is Created")

        # Stage Data
        self.stage_data = stage_data
        self.player_data = player_data
        self.game_state = GameState(self.player_data)

        self.user_sprite = UserSprite(self.stage_data, self.player_data,self.game_state.user_state.user_id)

        # controllers
        self.sprite_controller = SpriteController(self.stage_data.background, self.user_sprite)
        self.player_controller = PlayerController(self.user_sprite)
        self.collision_controller = CollisionController(self.sprite_controller)

        # views
        self.user_info_view = UserInfoView(USER_INFO_SIZE, self.player_data)
        self.stage_headline = StageHeadline(self.stage_data.stage_name)




        # TEMP
        enemy_data = UtilsFactory.get_player_data('Grey')
        enemy_id = uuid.uuid4()
        self.game_state.add_enemy(enemy_data,enemy_id)
        self.enemy = EnemySprite((800, 600), stage_data.background.size, enemy_data, self.user_sprite,enemy_id)
        self.sprite_controller.add(self.enemy)
        # END TEMP




    def update(self):
        self.sprite_controller.update()
        self.collision_controller.update()
        self.user_info_view.update(self.game_state)

    def draw(self, surface):
        self.sprite_controller.draw(surface)
        self.stage_headline.draw(surface)
        self.user_info_view.draw(surface)

    def update_event(self, event):
        self.player_controller.update_event(event)

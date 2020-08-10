import datetime
import uuid
import random

from controllers.game.collision_controller import CollisionController
from controllers.game.player_controller import PlayerController
from controllers.surface_controller import SurfaceController
from controllers.game.sprite_controller import SpriteController
from enums.screen_type import ScreenType
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


class StageController(SurfaceController):

    def __init__(self, stage_data, player_data):
        logger.info("StageController is Created")

        # Stage Data
        self.start_stage_time = datetime.datetime.now()
        self.stage_data = stage_data
        self.player_data = player_data
        self.game_state = GameState(self.player_data)
        self.user_sprite = UserSprite(self.stage_data, self.player_data, self.game_state.user_state.user_id)
        self.finish_wave = True

        # controllers
        self.sprite_controller = SpriteController(self.stage_data.background, self.user_sprite)
        self.player_controller = PlayerController(self.user_sprite)
        self.collision_controller = CollisionController(self.sprite_controller)

        # views
        self.user_info_view = UserInfoView(USER_INFO_SIZE, self.player_data)
        self.stage_headline = StageHeadline(self.stage_data.stage_name)

        # events
        dispatcher.connect(self.handle_collision_event, signal=SignalMapper.COLLISION_UPDATE, sender=dispatcher.Any)

    def update(self):
        self.stage_update()
        self.sprite_controller.update()
        self.collision_controller.update()
        self.user_info_view.update(self.game_state)
        self.update_state()

    def draw(self, surface):
        self.sprite_controller.draw(surface, self.game_state)
        self.stage_headline.draw(surface)
        self.user_info_view.draw(surface)

    def update_event(self, event):
        self.player_controller.update_event(event)

    def update_state(self):
        dead_enemies = list(
            filter(lambda x: self.game_state.enemies[x].user_health <= 0, self.game_state.enemies)).copy()
        for dead_enemy in dead_enemies:
            logger.info("enemy: " + dead_enemy + " is dead")
            self.sprite_controller.dead_by_id(dead_enemy)
            self.game_state.enemies.pop(dead_enemy)

    def handle_collision_event(self, event):
        self.game_state.handle_collision_event(event)
        self.sprite_controller.handle_collision_event(event)

    def add_enemy(self,name):
        enemy_data = UtilsFactory.get_player_data(name)
        enemy_id = uuid.uuid4()
        self.game_state.add_enemy(enemy_data, enemy_id)
        enemy = EnemySprite((random.randint(100, 900), 600), self.stage_data.background.size, enemy_data,
                                 self.user_sprite, enemy_id)
        self.sprite_controller.add(enemy)

    def stage_update(self):
        if self.finish_wave and len(self.game_state.enemies) == 0:
            self.finish_wave = False
            self.start_stage_time = datetime.datetime.now()

        pass_time = datetime.datetime.now() - self.start_stage_time
        if pass_time > datetime.timedelta(seconds = 6) and len(self.game_state.enemies) == 0:
            if len(self.stage_data.road_map) == 0:
                print("Stage is end ")
                dispatcher.send(signal=SignalMapper.SCREEN_TYPE_CHANGE,
                                event=ScreenType.MENU)
                return

            current_enemeis = self.stage_data.road_map.pop(0)
            print(current_enemeis)
            for enemy_dict in current_enemeis:
                for key in enemy_dict:
                    [self.add_enemy(enemy_dict[key]) for num in range(int(key))]
            self.finish_wave = True





import json

from utils.json_mappers.game_data_json_mapper import GameDataMapper
from utils.logger import logger
from utils.path_utils import CONFIGURATION_FILES_PATH
from utils.utils_factory import UtilsFactory


class GameManager:
    __instance = None

    @staticmethod
    def getInstance():
        if GameManager.__instance is None:
            with open(CONFIGURATION_FILES_PATH + '/game_data/game_data.json') as f:
                game_data_json = json.load(f)
                GameManager(game_data_json)
        return GameManager.__instance

    def __init__(self,game_data_json):
        self.game_data = game_data_json
        self.running = True
        self.user_player = game_data_json[GameDataMapper.SELECTED_PLAYER]
        self.stage = 1

        if GameManager.__instance is not None:
            raise Exception("Singleton")
        else:
            GameManager.__instance = self

    def get_user_data(self):
        return UtilsFactory.get_player_data(self.user_player)

    def get_stage_data(self):
        return UtilsFactory.get_state_data(self.stage)

    def save_state(self):
        logger.info("Save GameManager State to file")
        self.game_data[GameDataMapper.SELECTED_PLAYER] = self.user_player
        with open(CONFIGURATION_FILES_PATH + '/game_data/game_data.json', 'w') as game_data_file:
            json.dump(self.game_data, game_data_file)
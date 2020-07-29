import json
from model.player_data import PlayerData
from model.stage_data import StageData
from utils.path_utils import CONFIGURATION_FILES_PATH


class UtilsFactory:

    @staticmethod
    def get_player_data(player_name):
        with open(CONFIGURATION_FILES_PATH+'/players/'+player_name+'.json') as f:
            player_json = json.load(f)
            return PlayerData(player_json)

    @staticmethod
    def get_state_data(stage):
        with open(CONFIGURATION_FILES_PATH+'/stages/state_'+str(stage)+'.json') as f:
            stage_json = json.load(f)
            return StageData(stage_json)
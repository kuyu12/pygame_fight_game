import json

from model.player_data import PlayerData
from utils.path_utils import CONFIGURATION_FILES_PATH
from views.sprite_views.player_sprite import PlayerSprite


class PlayerSpriteFactory:

    @staticmethod
    def get_player_data(player_name):
        with open(CONFIGURATION_FILES_PATH+'/players/'+player_name+'.json') as f:
            player_json = json.load(f)
            return PlayerData(player_json)
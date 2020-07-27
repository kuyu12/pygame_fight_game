from utils.path_utils import SPRINT_IMAGE_PATH
from utils.player_json_mapper import SpriteMapper, InfoMapper


class PlayerData:

    def __init__(self, player_json):
        self.player_data = player_json
        self.sprite_data = self.player_data[SpriteMapper.SPRITE]
        self.player_info_data = self.player_data[InfoMapper.USER_INFO]

        # sprite paths
        self.sprite_walk_path = SPRINT_IMAGE_PATH + self.sprite_data[SpriteMapper.SPRITE_WALK]
        self.sprite_stand_path = SPRINT_IMAGE_PATH + self.sprite_data[SpriteMapper.SPRITE_STAND]
        self.sprite_hand_attack_path = SPRINT_IMAGE_PATH + self.sprite_data[SpriteMapper.SPRITE_HAND_ATTACK]
        self.sprite_foot_attack_path = SPRINT_IMAGE_PATH + self.sprite_data[SpriteMapper.SPRITE_FOOT_ATTACK]
        self.sprite_running_hand_attack_path = SPRINT_IMAGE_PATH + self.sprite_data[
            SpriteMapper.SPRITE_RUNNING_HAND_ATTACK]
        self.sprite_running_foot_attack_path = SPRINT_IMAGE_PATH + self.sprite_data[SpriteMapper.SPRITE_FOOT_ATTACK]
        self.sprite_defense_path = SPRINT_IMAGE_PATH + self.sprite_data[SpriteMapper.SPRITE_DEFENSE]
        self.sprite_defense_running_path = SPRINT_IMAGE_PATH + self.sprite_data[SpriteMapper.SPRITE_DEFENSE_RUNNING]
        self.sprite_running_path = SPRINT_IMAGE_PATH + self.sprite_data[SpriteMapper.SPRITE_RUNNING]

        # player info
        self.player_name = self.player_info_data[InfoMapper.PLAYER_NAME]
        self.profile_image = self.player_info_data[InfoMapper.PROFILE_IMAGE]
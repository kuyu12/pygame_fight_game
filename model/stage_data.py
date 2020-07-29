from utils.json_mappers.stage_json_mapper import StageMapper
from views.sprite_views.background_sprite import BackgroundSprite


class StageData:

    def __init__(self, stage_json):
        self.stage_data = stage_json
        self.road_map = self.stage_data[StageMapper.ROOD_MAP]
        self.background = BackgroundSprite(self.stage_data[StageMapper.STAGE_IMAGE])
        self.stage_name = self.stage_data[StageMapper.STAGE_NAME]
        self.user_start_position = (self.stage_data[StageMapper.USER_START_POSITION][0] ,self.stage_data[StageMapper.USER_START_POSITION][1])

import uuid

from views.sprite_views.player_sprite import PlayerSprite


class UserSprite(PlayerSprite):
    def __init__(self, stage_data, player_data,player_id = uuid.uuid4()):
        self.player_data = player_data
        self.move_speed = 1
        super().__init__(stage_data.user_start_position, stage_data.background.size,player_data,1,player_id)
from utils.json_mappers.player_json_mapper import ComboMapper
from views.sprite_views.player_sprite import ComboAttack


class ComboEvent:

    def __init__(self, player):
        self.combo_attack = ComboData(player_data=player.player_data)
        self.player = player


class ComboData:
    def __init__(self, player_data):
        self.combo_type = ComboAttack.SHOT
        self.attack_count = player_data.combo_data[ComboMapper.COMBO_ATTACK]
        self.move_x = player_data.combo_data[ComboMapper.MOVE_X]
        self.move_y = player_data.combo_data[ComboMapper.MOVE_Y]
        self.off_set = (player_data.combo_data[ComboMapper.OFF_SET_X], player_data.combo_data[ComboMapper.OFF_SET_Y])

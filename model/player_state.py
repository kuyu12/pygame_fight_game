from utils.json_mappers.player_json_mapper import AttackMapper
from views.sprite_views.attack_sprite import AttackState
from views.sprite_views.movement_sprite import State


class PlayerState:
    def __init__(self, player_data, player_id):
        self.user_health = player_data.basic_health
        self.user_base_health = player_data.basic_health
        self.user_mana = player_data.basic_mana
        self.user_id = str(player_id)
        self.attack_dict = player_data.attack_dict

    def get_attack_damage(self, attack_state, player_state):
        if player_state == State.RUNNING_ATTACK:
            if attack_state == AttackState.HAND:
                return self.attack_dict[AttackMapper.ATTACK_RUNNING_HAND]
            if attack_state == AttackState.FOOT:
                return self.attack_dict[AttackMapper.ATTACK_RUNNING_FOOT]
        else:
            if attack_state == AttackState.HAND:
                return self.attack_dict[AttackMapper.ATTACK_HAND]
            if attack_state == AttackState.FOOT:
                return self.attack_dict[AttackMapper.ATTACK_FOOT]
        return 0

    def set_damage(self,damage):
        self.user_health -= damage

        if self.user_health <= 0:
            self.user_health = 0
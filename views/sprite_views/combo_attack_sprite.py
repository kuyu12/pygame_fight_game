from views.sprite_views.attack_sprite import AttackSprite, AttackState
from views.sprite_views.movement_sprite import Direction, State


class ComboAttackSprite(AttackSprite):

    def __init__(self, player_data, combo_attack, on_finish):
        self.combo_attack = combo_attack
        self.combo_images = player_data.get_combo_images(combo_attack.combo_type)
        self.attack_state = AttackState.COMBO
        loc = (player_data.location[0] + combo_attack.off_set[0],player_data.location[1] + combo_attack.off_set[1])
        super().__init__(loc, player_data.bounds_size)

        self.directions[player_data.faceDirection] = True
        self.is_blocking_move = True
        self.finish_block_state = State.DEAD

        if player_data.faceDirection == Direction.RIGHT:
            self.move_x = combo_attack.move_x
        else:
            self.move_x = -combo_attack.move_x

        self.on_dead_animation_finish = on_finish

    def load_images(self):
        self.images = self.combo_images

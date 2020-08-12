from views.sprite_views.attack_sprite import AttackSprite, AttackState
from views.sprite_views.movement_sprite import Direction, State


class ComboAttackSprite(AttackSprite):

    def __init__(self, player_data, combo, on_finish):
        self.combo = combo
        self.combo_images = player_data.get_combo_images(combo)
        self.attack_state = AttackState.COMBO

        super().__init__(player_data.location, player_data.bounds_size)

        self.directions[player_data.faceDirection] = True
        self.is_blocking_move = True
        self.finish_block_state = State.DEAD

        if player_data.faceDirection == Direction.RIGHT:
            self.move_x = 4
        else:
            self.move_x = -4

        self.on_dead_animation_finish = on_finish

    def load_images(self):
        self.images = self.combo_images

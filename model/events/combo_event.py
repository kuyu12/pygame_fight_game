from views.sprite_views.player_sprite import ComboAttack


class ComboEvent:

    def __init__(self,player):
        self.combo_attack = ComboAttack.SHOT
        self.player = player

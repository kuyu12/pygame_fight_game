from math import sqrt
import random

from views.sprite_views.animated_sprite import Update_Type
from views.sprite_views.attack_sprite import AttackState
from views.sprite_views.movement_sprite import State, Direction
from views.sprite_views.player_sprite import PlayerSprite


class EnemySprite(PlayerSprite):

    def __init__(self, start_position, bounds_size, player_data, user_player):
        super().__init__(start_position, bounds_size, player_data, 0.7)
        self.user_player = user_player
        self.firstMove = False
        self.Y_DEDUCTION_THRESHOLD = 0.1
        self.direction_x = 0
        self.direction_y = 0

        self.is_attack_y_ready = False
        self.is_attack_x_ready = False

    def update(self, update_type=Update_Type.TIME):

        # TODO: refactor this section.

        dif_x = self.user_player.rect.centerx - self.rect.centerx;
        dif_y = self.user_player.rect.centery - self.rect.centery;

        if not self.firstMove:
            if abs(dif_x) < 300:
                self.firstMove = True
            super().update(update_type)
            return

        hyp = sqrt(dif_x * dif_x + dif_y * dif_y);
        if hyp != 0:
            self.direction_x = dif_x / hyp;
            self.direction_y = dif_y / hyp;

        if abs(dif_x) > self.rect.width / 2:
            self.is_attack_x_ready = False
            if self.direction_x > 0:
                self.control_move(State.WALKING, Direction.RIGHT)
                self.control_move(State.STANDING, Direction.LEFT)
            if self.direction_x < 0:
                self.control_move(State.WALKING, Direction.LEFT)
                self.control_move(State.STANDING, Direction.RIGHT)
        else:
            self.is_attack_x_ready = True
            self.control_move(State.STANDING, Direction.RIGHT)
            self.control_move(State.STANDING, Direction.LEFT)

        if self.direction_y > self.Y_DEDUCTION_THRESHOLD or dif_y < -self.Y_DEDUCTION_THRESHOLD:
            self.is_attack_y_ready = False
            if self.direction_y > 0:
                self.control_move(State.WALKING, Direction.DOWN)
                self.control_move(State.STANDING, Direction.UP)
            if self.direction_y < 0:
                self.control_move(State.WALKING, Direction.UP)
                self.control_move(State.STANDING, Direction.DOWN)
        else:
            self.is_attack_y_ready = True
            self.control_move(State.STANDING, Direction.DOWN)
            self.control_move(State.STANDING, Direction.UP)

        if self.is_attack_x_ready and self.is_attack_y_ready:
            if bool(random.getrandbits(1)):
                self.attack(AttackState.HAND)
            else:
                self.attack(AttackState.FOOT)




        super().update(update_type)

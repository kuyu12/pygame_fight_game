from enum import Enum
from views.sprite_views.movement_sprite import MovementSprite, State, Direction


class AttackState(Enum):
    HAND = 1
    FOOT = 2
    DEFENSE = 3
    COMBO = 4


class AttackSprite(MovementSprite):
    def __init__(self, start_position, bounds_size):
        super().__init__(start_position, bounds_size)
        self.is_attack_active = False
        self.attack_block_count = 0
        self.attack_block_max = 6
        self.attack_state = AttackState.HAND

        self.on_dead_animation_finish = lambda x: x  # empty func

    def attack(self, attack):
        self.attack_state = attack
        self.set_state(State.ATTACK, self.faceDirection)

    def is_attack_combo(self, attack):
        if self.attack_state == AttackState.DEFENSE \
                and attack == AttackState.HAND \
                and (self.directions[Direction.RIGHT] or self.directions[Direction.LEFT]):
            return True
        return False

    def is_on_attack_mode(self):
        if (self.state == State.ATTACK or self.state == State.RUNNING_ATTACK) \
                and self.attack_state != AttackState.DEFENSE:
            return True
        return False

    def is_on_defence_mode(self):
        if (self.state == State.ATTACK or self.state == State.RUNNING_ATTACK) \
                and self.attack_state == AttackState.DEFENSE:
            return True

        if self.state == State.BEATEN:
            return True

        return False

    def on_state_change(self, state, direction):
        if self.state == State.ATTACK:
            self.images = self.get_attack_images()
            self.attack_block_count = 0
            self.is_attack_active = True

        if self.state == State.DEAD:
            self.on_dead_animation_finish(self)
            return

        super().on_state_change(state, direction)

    def get_attack_images(self):
        if self.last_state == State.RUNNING:
            self.state = State.RUNNING_ATTACK
            if self.attack_state == AttackState.HAND:
                return self.attack_running_hand_R if self.faceDirection == Direction.RIGHT else self.attack_running_hand_L

            if self.attack_state == AttackState.FOOT:
                return self.attack_running_foot_R if self.faceDirection == Direction.RIGHT else self.attack_running_foot_L

            if self.attack_state == AttackState.DEFENSE:
                return self.defense_running_R if self.faceDirection == Direction.RIGHT else self.defense_running_L
            return

        if self.attack_state == AttackState.HAND:
            return self.attack_hand_R if self.faceDirection == Direction.RIGHT else self.attack_hand_L

        if self.attack_state == AttackState.COMBO:
            return self.shot_move_R if self.faceDirection == Direction.RIGHT else self.shot_move_L

        if self.attack_state == AttackState.FOOT:
            return self.attack_foot_R if self.faceDirection == Direction.RIGHT else self.attack_foot_L

        if self.attack_state == AttackState.DEFENSE:
            return self.defense_R if self.faceDirection == Direction.RIGHT else self.defense_L

    def frame_was_update(self):
        super().frame_was_update()
        if not self.is_attack_active:
            return

        if self.attack_block_count == 0:
            self.attack_block_max = len(self.images)

        self.attack_block_count += 1
        if self.attack_block_count >= self.attack_block_max:
            self.attack_block_count = 0
            self.is_attack_active = False
            if self.state == State.ATTACK or self.state == State.RUNNING_ATTACK:
                self.set_state(State.STANDING, self.faceDirection)

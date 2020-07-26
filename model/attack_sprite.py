from enum import Enum

from model.movement_sprite import MovementSprite, State, Direction


class AttackState(Enum):
    HAND = 1
    FOOT = 2
    DEFENSE = 3
    SHOT = 4


class AttackSprite(MovementSprite):
    def __init__(self, start_position, bounds_size):
        super().__init__(start_position, bounds_size)
        self.is_state_block = False
        self.block_count = 0
        self.block_max = 6
        self.attack_state = AttackState.HAND

    def attack(self, attack):
        self.attack_state = attack
        self.set_state(State.ATTACK,self.faceDirection)

    def on_state_change(self, state, direction):
        if self.state == State.ATTACK:
            self.images = self.get_attack_images()
            self.block_count = 0
            self.is_state_block = True

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

        if self.attack_state == AttackState.FOOT:
            return self.attack_foot_R if self.faceDirection == Direction.RIGHT else self.attack_foot_L

        if self.attack_state == AttackState.DEFENSE:
            return self.defense_R if self.faceDirection == Direction.RIGHT else self.defense_L

    def frame_was_update(self):
        if not self.is_state_block:
            return
        if self.block_count == 0:
            self.block_max = len(self.images)

        self.block_count += 1
        if self.block_count >= self.block_max:
            self.block_count = 0
            self.is_state_block = False
            if self.state == State.ATTACK or self.state == State.RUNNING_ATTACK:
                self.set_state(State.STANDING, self.faceDirection)
import uuid
from enum import Enum
from functools import reduce
import pygame
from views.sprite_views.attack_sprite import AttackSprite
from views.sprite_views.movement_sprite import State, Direction


class ComboAttack(Enum):
    SHOT = 1


class PlayerSprite(AttackSprite):

    def __init__(self, start_position, bounds_size, player_data, move_speed, player_id=uuid.uuid4()):
        self.player_data = player_data
        self.move_speed = move_speed
        self.player_id = str(player_id)
        super().__init__(start_position, bounds_size)

    def load_images(self):

        # walk
        self.walk_images_R = self.get_images_with_path(self.player_data.sprite_walk_path)
        self.walk_images_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.walk_images_R))

        # stand
        self.stand_R = self.get_images_with_path(self.player_data.sprite_stand_path)
        self.stand_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.stand_R))

        # attack
        self.attack_hand_R = self.get_images_with_path(self.player_data.sprite_hand_attack_path)
        self.attack_hand_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.attack_hand_R))
        self.attack_foot_R = self.get_images_with_path(self.player_data.sprite_foot_attack_path)
        self.attack_foot_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.attack_foot_R))

        self.attack_running_hand_R = self.get_images_with_path(self.player_data.sprite_running_hand_attack_path)
        self.attack_running_hand_L = list(
            map(lambda x: pygame.transform.flip(x, True, False), self.attack_running_hand_R))
        self.attack_running_foot_R = self.get_images_with_path(self.player_data.sprite_running_foot_attack_path)
        self.attack_running_foot_L = list(
            map(lambda x: pygame.transform.flip(x, True, False), self.attack_running_foot_R))

        # defense
        self.defense_R = self.get_images_with_path(self.player_data.sprite_defense_path)
        self.defense_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.defense_R))

        self.defense_running_R = self.get_images_with_path(self.player_data.sprite_defense_running_path)
        self.defense_running_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.defense_running_R))

        # running
        self.running_R = self.get_images_with_path(self.player_data.sprite_running_path)
        self.running_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.running_R))

        self.fall_R = self.get_images_with_path(self.player_data.sprite_fall_path)
        self.fall_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.fall_R))

        self.dead_R = self.get_images_with_path(self.player_data.sprite_dead_path)
        self.dead_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.dead_R))

        if self.player_data.is_support_fire_attack:
            self.shot_move_R = self.get_images_with_path(self.player_data.sprite_fire_attack_move_path)
            self.shot_move_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.shot_move_R))

            self.shot_R = self.get_images_with_path(self.player_data.sprite_fire_attack_path)
            self.shot_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.shot_R))
        else:
            self.shot_move_R = self.attack_hand_R
            self.shot_move_L = self.attack_hand_L

        self.images = self.stand_R

    def get_combo_images(self, combo):
        if not self.player_data.is_support_fire_attack:
            return None

        if combo == ComboAttack.SHOT:
            return self.shot_R if self.faceDirection == Direction.RIGHT else self.shot_L

        return None

    def control_move(self, state=None, direction=None):
        if direction is None:
            direction = self.faceDirection

        if state is None:
            state = self.state

        self.set_state(state, direction)

    def set_dead_state(self, on_dead_animation_finish):
        self.is_blocking_move = False
        self.control_move(State.FALL_TO_DEAD)
        self.on_dead_animation_finish = on_dead_animation_finish

    def on_state_change(self, state, direction):
        super().on_state_change(state, direction)

        if self.state == State.WALKING:
            self.images = self.walk_images_R if self.faceDirection == Direction.RIGHT else self.walk_images_L

        elif self.state == State.RUNNING:
            self.images = self.running_R if self.faceDirection == Direction.RIGHT else self.running_L

        elif self.state == State.STANDING:
            self.images = self.stand_R if self.faceDirection == Direction.RIGHT else self.stand_L

        elif self.state == State.BEATEN:
            self.images = self.fall_R if self.faceDirection == Direction.RIGHT else self.fall_L
            self.is_blocking_move = True
            self.finish_block_state = State.STANDING

        elif self.state == State.FALL_TO_DEAD:
            self.images = self.dead_R if self.faceDirection == Direction.RIGHT else self.dead_L
            self.is_blocking_move = True
            self.finish_block_state = State.DEAD

    def change_movement_by_state(self, state, direction):
        if state == State.WALKING:
            if self.directions[Direction.RIGHT]:
                self.move_x = self.move_speed
            elif self.directions[Direction.LEFT]:
                self.move_x = -self.move_speed
            else:
                self.move_x = 0
            if self.directions[Direction.UP]:
                self.move_y = -self.move_speed
            elif self.directions[Direction.DOWN]:
                self.move_y = self.move_speed
            else:
                self.move_y = 0

        if state == State.RUNNING:
            if self.directions[Direction.RIGHT]:
                self.move_x = self.move_speed * 3
            if self.directions[Direction.LEFT]:
                self.move_x = -self.move_speed * 3
            if self.directions[Direction.UP]:
                self.move_y = -self.move_speed
            if self.directions[Direction.DOWN]:
                self.move_y = self.move_speed

        if self.state == State.RUNNING_ATTACK:
            if self.directions[Direction.RIGHT]:
                self.move_x = self.move_speed * 2
            if self.directions[Direction.LEFT]:
                self.move_x = -self.move_speed * 2

        if self.state == State.STANDING:
            self.directions[direction] = False

        if self.state == State.ATTACK or self.state == State.DEAD:
            for dir in self.directions:
                self.directions[dir] = False

        if self.state == State.BEATEN:
            if self.directions[Direction.RIGHT]:
                self.move_x = -self.move_speed * 3
            elif self.directions[Direction.LEFT]:
                self.move_x = +self.move_speed * 3

        if reduce(lambda a, b: a + b, self.directions.values()) == 0:
            self.move_x = 0
            self.move_y = 0

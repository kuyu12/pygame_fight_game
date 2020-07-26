from functools import reduce
import random

import pygame

from model.attack_sprite import AttackSprite
from model.movement_sprite import State, Direction, Direction
from utils.path_utils import SPRINT_IMAGE_PATH


class PlayerSprite(AttackSprite):

    def __init__(self, start_position, bounds_size):
        super().__init__(start_position, bounds_size)

    def load_images(self):
        # walk
        self.walk_images_R = self.get_images_with_path(SPRINT_IMAGE_PATH + '/player/walk')
        self.walk_images_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.walk_images_R))

        # stand
        self.stand_R = self.get_images_with_path(SPRINT_IMAGE_PATH + '/player/stand')
        self.stand_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.stand_R))

        # attack
        self.attack_hand_R = self.get_images_with_path(SPRINT_IMAGE_PATH + '/player/attack_1')
        self.attack_hand_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.attack_hand_R))
        self.attack_foot_R = self.get_images_with_path(SPRINT_IMAGE_PATH + '/player/attack_2')
        self.attack_foot_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.attack_foot_R))

        self.attack_running_hand_R = self.get_images_with_path(SPRINT_IMAGE_PATH + '/player/attack_running_1')
        self.attack_running_hand_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.attack_running_hand_R))
        self.attack_running_foot_R = self.get_images_with_path(SPRINT_IMAGE_PATH + '/player/attack_running_2')
        self.attack_running_foot_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.attack_running_foot_R))

        # defense
        self.defense_R = self.get_images_with_path(SPRINT_IMAGE_PATH + '/player/defense')
        self.defense_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.defense_R))

        self.defense_running_R = self.get_images_with_path(SPRINT_IMAGE_PATH + '/player/defense_running')
        self.defense_running_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.defense_running_R))

        # running
        self.running_R = self.get_images_with_path(SPRINT_IMAGE_PATH + '/player/running')
        self.running_L = list(map(lambda x: pygame.transform.flip(x, True, False), self.running_R))

        self.images = self.stand_R

    def control_move(self, state=None, direction=None):
        if direction is None:
            direction = self.faceDirection

        if state is None:
            state = self.state

        self.set_state(state, direction)

    def on_state_change(self, state, direction):
        super().on_state_change(state, direction)

        if self.state == State.WALKING:
            self.images = self.walk_images_R if self.faceDirection == Direction.RIGHT else self.walk_images_L

        elif self.state == State.RUNNING:
            self.images = self.running_R if self.faceDirection == Direction.RIGHT else self.running_L

        elif self.state == State.STANDING:
            self.images = self.stand_R if self.faceDirection == Direction.RIGHT else self.stand_L

    def change_movement_by_state(self, state, direction):
        if state == State.WALKING:
            if self.directions[Direction.RIGHT]:
                self.move_x = 1
            elif self.directions[Direction.LEFT]:
                self.move_x = -1
            else:
                self.move_x = 0
            if self.directions[Direction.UP]:
                self.move_y = -1
            elif self.directions[Direction.DOWN]:
                self.move_y = 1
            else:
                self.move_y = 0

        if state == State.RUNNING:
            if self.directions[Direction.RIGHT]:
                self.move_x = 3
            if self.directions[Direction.LEFT]:
                self.move_x = -3
            if self.directions[Direction.UP]:
                self.move_y = -1
            if self.directions[Direction.DOWN]:
                self.move_y = 1

        if self.state == State.RUNNING_ATTACK:
            if self.directions[Direction.RIGHT]:
                self.move_x = 2
            if self.directions[Direction.LEFT]:
                self.move_x = -2

        if self.state == State.STANDING:
            self.directions[direction] = False

        if self.state == State.ATTACK:
            for dir in self.directions:
                self.directions[dir] = False

        if reduce(lambda a,b: a+b,self.directions.values()) == 0:
            self.move_x = 0
            self.move_y = 0


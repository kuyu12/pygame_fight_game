import math
import random

from tf_agents.environments import py_environment
from tf_agents.specs import array_spec
from tf_agents.trajectories import time_step as ts
import numpy as np


class littleFighterEnv(py_environment.PyEnvironment):

    def __init__(self):
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=3, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(4,), dtype=np.int32, minimum=0, name='observation')
        self._state = self.__get_rand_state()
        self._max_round = 1000
        self._round_counter = 0
        self._episode_ended = False
        self._isWin = False

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    # [enemy x,enemy y,player x,player y]
    def set_location(self,location):
        self._state = location

    def __get_rand_state(self):
        return [450, 600, random.randint(100, 900), random.randint(500, 700)]

    def _reset(self):
        self._state = self.__get_rand_state()
        self._episode_ended = False
        self._round_counter = 0
        self._isWin = False
        return ts.restart(np.array(self._state, dtype=np.int32))

    def _step(self, action):
        self._round_counter += 1
        if self._episode_ended:
            return self.reset()

        if self._state[2] - 50 <= self._state[0] <= self._state[2] + 50 and \
                self._state[3] - 50 <= self._state[1] <= self._state[3] + 50:
            self._isWin = True
            self._episode_ended = True

        if self._round_counter >= self._max_round:
            self._isWin = False
            self._episode_ended = True

        if self._episode_ended:
            print(self._state)
            if self._isWin:
                return ts.termination(np.array(self._state, dtype=np.int32), 1)
            else:
                return ts.termination(np.array(self._state, dtype=np.int32), -1)

        if action == 0:
            self._state[0] = self._state[0] + 1  # x+1
            if self._state[0] <= self._state[2]:
                return ts.transition(np.array(self._state, dtype=np.int32), reward=0.1, discount=1.0)
            else:
                return ts.termination(np.array(self._state, dtype=np.int32), -1)
        elif action == 1:
            self._state[0] = self._state[0] - 1  # x-1
            if self._state[0] >= self._state[2]:
                return ts.transition(np.array(self._state, dtype=np.int32), reward=0.1, discount=1.0)
            else:
                return ts.termination(np.array(self._state, dtype=np.int32), -1)
        elif action == 2:
            self._state[1] = self._state[1] + 1  # y+1
            if self._state[1] <= self._state[3]:
                return ts.transition(np.array(self._state, dtype=np.int32), reward=0.1, discount=1.0)
            else:
                return ts.termination(np.array(self._state, dtype=np.int32), -1)
        elif action == 3:
            self._state[1] = self._state[1] - 1  # y-1
            if self._state[1] >= self._state[3]:
                return ts.transition(np.array(self._state, dtype=np.int32), reward=0.1, discount=1.0)
            else:
                return ts.termination(np.array(self._state, dtype=np.int32), -1)

        else:
            raise ValueError('`action` should be between 0 to 3', action)

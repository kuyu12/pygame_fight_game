from enum import Enum
from functools import reduce

from views.sprite_views.animated_sprite import AnimatedSprite, Update_Type


class State(Enum):
    STANDING = 1
    WALKING = 2
    RUNNING = 3
    ATTACK = 4
    RUNNING_ATTACK = 5


class Direction(Enum):
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"


class MovementSprite(AnimatedSprite):

    def __init__(self, start_position, bounds_size):
        self.load_images()
        self.move_x = 0
        self.move_y = 0
        self.position_x = start_position[0]
        self.position_y = start_position[1]

        self.bounds_size = bounds_size
        self.faceDirection = Direction.RIGHT
        self.state = State.STANDING
        self.last_state = State.STANDING
        self.directions = {
            Direction.RIGHT: False,
            Direction.LEFT: False,
            Direction.UP: False,
            Direction.DOWN: False
        }

        super().__init__(start_position, self.images)

    def set_state(self, state, direction):
        self.directions[direction] = state != State.STANDING
        if state != State.STANDING and self.state != State.RUNNING or state == State.ATTACK:
            self.last_state = self.state
            self.state = state
        else:
            if reduce(lambda a, b: a + b, self.directions.values()) == 0:
                self.last_state = self.state
                self.state = state
        self.on_state_change(self.state, direction)

    def update(self, update_type=Update_Type.TIME):
        super().update(update_type)
        self.move_one_time(self.move_x, self.move_y)

    def move_one_time(self, def_x, def_y):
        wight = self.bounds_size[0]
        height = self.bounds_size[1]
        if wight - self.size[0] >= self.rect.x + def_x >= 0:
            self.position_x += def_x
            self.rect.x = self.position_x
        if height * 0.8 - self.size[1] <= self.rect.y + def_y <= height - self.size[1]:
            self.position_y += def_y
            self.rect.y = self.position_y

    def on_state_change(self, state, direction):
        if state != self.state:
            self.index = 0
        self.update_face_direction(self.directions)
        self.change_movement_by_state(state, direction)
        # change sprite images

    def update_face_direction(self, directions):
        if directions[Direction.RIGHT]:
            self.faceDirection = Direction.RIGHT
        if directions[Direction.LEFT]:
            self.faceDirection = Direction.LEFT

    def change_movement_by_state(self, state, direction):
        pass

    def load_images(self):
        # load sprite images
        # create self.images with default images
        pass

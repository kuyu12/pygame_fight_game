import os
import pygame
from enum import Enum
import re


class Update_Type(Enum):
    TIME = 1
    FRAME = 2


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position, images):
        super(AnimatedSprite, self).__init__()

        self.images = images
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = len(images)
        self.current_frame = 0

        self.dt = 0.01

        self.rect.x = position[0]
        self.rect.y = position[1]

    def update_time_dependent(self, dt):
        self.current_time = self.current_time + dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.frame_was_update()

    def update_frame_dependent(self):
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.frame_was_update()

    def frame_was_update(self):
        pass

    def update(self, update_type=Update_Type.TIME):
        if update_type == Update_Type.TIME:
            self.update_time_dependent(self.dt)

        if update_type == Update_Type.FRAME:
            self.update_frame_dependent()

    @staticmethod
    def get_images_with_path(path):
        images = []

        dirlist = sorted(os.listdir(path),key = lambda x: int(re.findall(r'[0-9]+', x)[-1]))

        for image in dirlist:

            images.append(pygame.image.load(os.path.join(path, image)))
        return images

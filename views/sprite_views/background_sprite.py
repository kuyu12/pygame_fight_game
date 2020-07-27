from utils.path_utils import BACKGROUND_IMAGES_PATH
from views.sprite_views.animated_sprite import AnimatedSprite


class BackgroundSprite(AnimatedSprite):

    def __init__(self, background_name):
        self.images = self.get_images_with_path(BACKGROUND_IMAGES_PATH + '/'+background_name)
        super(BackgroundSprite, self).__init__((0, 0), self.images)

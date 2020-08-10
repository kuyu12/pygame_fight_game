import pygame
from pygame.rect import Rect

from utils.color import WHITE
from utils.path_utils import PROFILE_IMAGES_PATH
from utils.utils_factory import UtilsFactory
from views.gui_views.surface_inteface import SurfaceInterface


# self.player_name = self.player_info_data[InfoMapper.PLAYER_NAME]
# self.profile_image = self.player_info_data[InfoMapper.PROFILE_IMAGE]
# self.basic_health = self.player_info_data[InfoMapper.START_HEALTH]
# self.basic_mana = self.player_info_data[InfoMapper.START_MANA]

class PlayerSettingView(SurfaceInterface):
    def __init__(self,location, player_name):
        super().__init__((120,150))
        self.is_select = False
        self.location = location
        self.player_name = player_name
        self.player_data = UtilsFactory.get_player_data(player_name)
        self.rect = Rect(0,0,0,0)

        profile_img = pygame.transform.scale(pygame.image.load(PROFILE_IMAGES_PATH + self.player_data.profile_image),(95,95))
        self.blit(profile_img, (5, 5))

        small_font = pygame.font.SysFont(pygame.font.get_default_font(), 25)
        textHealthSurface = small_font.render("Health:" + str(self.player_data.basic_health), True, WHITE)
        self.blit(textHealthSurface, (20, 110))

        textManaSurface = small_font.render("Mana:" + str(self.player_data.basic_mana), True, WHITE)
        self.blit(textManaSurface, (20, 135))

    def draw(self, surface):
        if self.is_select:
            pygame.draw.rect(surface, WHITE, (self.location[0], self.location[1], 105, 105))
        self.rect = surface.blit(self, self.location)

    def get_rect(self):
        return self.rect

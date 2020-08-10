import pygame

from utils.color import RED, BLACK, BLUE
from utils.path_utils import PROFILE_IMAGES_PATH, USER_INFO_BACKGROUND_PATH
from views.gui_views.surface_inteface import SurfaceInterface


class UserInfoView(SurfaceInterface):
    def __init__(self, size, player_data):
        super().__init__(size)
        self.player_data = player_data
        self.health_base = player_data.basic_health
        self.health = self.health_base
        self.mana_base = player_data.basic_mana
        self.mana = self.mana_base

        background = pygame.transform.scale(pygame.image.load(USER_INFO_BACKGROUND_PATH), size)
        self.blit(background, (0, 0))

        profile_img = pygame.transform.scale(pygame.image.load(PROFILE_IMAGES_PATH + self.player_data.profile_image),
                                             (80, 80))
        self.blit(profile_img, (10, 10))

        font = pygame.font.SysFont(pygame.font.get_default_font(), 36)
        small_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

        textNameSurface = font.render(self.player_data.player_name, True, BLACK)
        self.blit(textNameSurface, [100, 10])

        textHealthSurface = small_font.render("Health:", True, BLACK)
        self.blit(textHealthSurface, [100, 36])

        textManaSurface = small_font.render("Mana:", True, BLACK)
        self.blit(textManaSurface, [100, 61])

    def update(self, game_state):
        self.health = game_state.user_state.user_health
        self.mana = game_state.user_state.user_mana

    def draw(self, surface):
        surface.blit(self, (0, 0))

        health_draw = 150
        if self.health != 0:
            health_draw = 150 * self.health / self.health_base
        pygame.draw.rect(self, BLACK, pygame.Rect(100, 50, 150, 10), 0)
        pygame.draw.rect(self, RED, pygame.Rect(100, 50, health_draw, 10), 0)
        pygame.draw.rect(self, BLACK, pygame.Rect(100, 50, 150, 10), 1)

        mana_draw = 150
        if self.mana != 0:
            mana_draw = 150 * self.mana / self.mana_base
        pygame.draw.rect(self, BLACK, pygame.Rect(100, 75, 150, 10), 0)
        pygame.draw.rect(self, BLUE, pygame.Rect(100, 75, mana_draw, 10))
        pygame.draw.rect(self, BLACK, pygame.Rect(100, 75, 150, 10), 1)

import pygame
from utils.color import WHITE
from utils.const import HEADLINE_SIZE
from views.gui_views.surface_inteface import SurfaceInterface
import time


class StageHeadline(SurfaceInterface):
    def __init__(self,name):
        super().__init__((0,0))
        self.name = name
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), HEADLINE_SIZE)
        self.textNameSurface = self.font.render(self.name, True, WHITE)
        self.start = time.time()

    def draw(self, surface):
        if time.time() - self.start <= 3:
            surface.blit(self.textNameSurface,
                     [surface.get_size()[0] / 2 - self.textNameSurface.get_size()[0] / 2, surface.get_size()[1] / 2])
import pygame
from pydispatch import dispatcher
from controllers.surface_controller import SurfaceController
from controllers.game.sprite_controller import SpriteController
from enums.screen_type import ScreenType
from utils.logger import logger
from utils.color import WHITE, GREY
from utils.const import HEADLINE_SIZE, NORMAL_SIZE, SCREEN_SIZE, BUTTON_SIZE
from utils.json_mappers.stage_json_mapper import SignalMapper
from views.gui_views.button import Button
from views.sprite_views.background_sprite import BackgroundSprite



class MenuController(SurfaceController):

    def __init__(self):
        logger.info("MenuController is Created")

        self.background = BackgroundSprite(background_name='background1')
        self.sprite_controller = SpriteController(self.background)

        self.font_headline = pygame.font.SysFont(pygame.font.get_default_font(), HEADLINE_SIZE)
        self.font_button = pygame.font.SysFont(pygame.font.get_default_font(), NORMAL_SIZE)
        self.textHeadlineSurface = self.font_headline.render("Fight Back", True, WHITE)

        self.buttonStart = Button(
            None, SCREEN_SIZE[0] / 2 - BUTTON_SIZE[0] / 2, SCREEN_SIZE[1] / 2, BUTTON_SIZE[0], BUTTON_SIZE[1],
            text='Start',
            fontSize=50, margin=20,
            inactiveColour=WHITE,
            pressedColour=GREY, radius=20,
            onClick=lambda: self.send_change_type_signl(ScreenType.GAME))

        self.buttonSelect = Button(
            None, SCREEN_SIZE[0] / 2 - BUTTON_SIZE[0] / 2, SCREEN_SIZE[1] / 2 + BUTTON_SIZE[1]*2, BUTTON_SIZE[0], BUTTON_SIZE[1],
            text='Character',
            fontSize=50, margin=20,
            inactiveColour=WHITE,
            pressedColour=GREY, radius=20,
            onClick=lambda: self.send_change_type_signl(ScreenType.SETTING))

        self.buttonQuit = Button(
            None, SCREEN_SIZE[0] / 2 - BUTTON_SIZE[0] / 2, SCREEN_SIZE[1] / 2 + BUTTON_SIZE[1]*4, BUTTON_SIZE[0], BUTTON_SIZE[1],
            text='Quit',
            fontSize=50, margin=20,
            inactiveColour=WHITE,
            pressedColour=GREY, radius=20,
            onClick=lambda: self.send_change_type_signl(ScreenType.QUIT))

    def send_change_type_signl(self,type):
        dispatcher.send(signal=SignalMapper.SCREEN_TYPE_CHANGE,
                        event=type)

    def update(self):
        self.sprite_controller.update()

    def update_event(self, event):
        self.buttonStart.listen(event)
        self.buttonSelect.listen(event)
        self.buttonQuit.listen(event)

    def draw(self, surface):
        self.sprite_controller.draw(surface)
        surface.blit(self.textHeadlineSurface,
                     [surface.get_size()[0] / 2 - self.textHeadlineSurface.get_size()[0] / 2,
                      surface.get_size()[1] / 6])

        self.buttonStart.draw(surface)
        self.buttonSelect.draw(surface)
        self.buttonQuit.draw(surface)


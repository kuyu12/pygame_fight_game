import random

import pygame
from pydispatch import dispatcher

from controllers.game.sprite_controller import SpriteController
from controllers.game_manager import GameManager
from controllers.surface_controller import SurfaceController
from enums.screen_type import ScreenType
from utils.color import WHITE, GREY
from utils.const import SCREEN_SIZE, BUTTON_SIZE
from utils.json_mappers.stage_json_mapper import SignalMapper
from views.gui_views.button import Button
from views.gui_views.player_setting_view import PlayerSettingView
from views.sprite_views.background_sprite import BackgroundSprite


class SettingController(SurfaceController):

    def __init__(self):
        self.background = BackgroundSprite(background_name='background1')
        self.sprite_controller = SpriteController(self.background)

        self.player_setting_dict = []
        player_temp = ["frozen","firen","grey","rudolf"]
        for i in range(4):
                self.player_setting_dict.append(PlayerSettingView((SCREEN_SIZE[0]/4 * i + 50,SCREEN_SIZE[1]/3 ),player_temp[i]))

        self.buttonStart = Button(
            None, SCREEN_SIZE[0] / 2 - BUTTON_SIZE[0] / 2, SCREEN_SIZE[1] / 1.2, BUTTON_SIZE[0], BUTTON_SIZE[1],
            text='Menu',
            fontSize=50, margin=20,
            inactiveColour=WHITE,
            pressedColour=GREY, radius=20,
            onClick=lambda: self.send_change_type_signl(ScreenType.MENU))

    def send_change_type_signl(self,type):
        selected_player = next(filter(lambda x: x.is_select,self.player_setting_dict),None)
        GameManager.getInstance().user_player = selected_player.player_name
        dispatcher.send(signal=SignalMapper.SCREEN_TYPE_CHANGE,
                        event=type)

    def update(self):
        self.sprite_controller.update()

    def update_event(self, event):
        self.buttonStart.listen(event)

        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            pos = pygame.mouse.get_pos()
            clicked_player = next(filter(lambda x: x.get_rect().collidepoint(pos),self.player_setting_dict),None)
            print(clicked_player)
            if clicked_player:
                for element in self.player_setting_dict:
                    element.is_select = False
                clicked_player.is_select = True

    def draw(self, surface):
        self.sprite_controller.draw(surface)
        [element.draw(surface) for element in self.player_setting_dict]
        self.buttonStart.draw(surface)

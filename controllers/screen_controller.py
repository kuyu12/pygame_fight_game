from pydispatch import dispatcher
from controllers.game_manager import GameManager
from controllers.menu.menu_controller import MenuController
from controllers.game.stage_controller import StageController
from controllers.setting.setting_controller import SettingController
from controllers.surface_controller import SurfaceController
from enums.screen_type import ScreenType
from utils.json_mappers.stage_json_mapper import SignalMapper


def get_controller(screen_type):
    gameManager = GameManager.getInstance()
    if screen_type == ScreenType.MENU:
        return MenuController()
    if screen_type == ScreenType.GAME:
        return StageController(gameManager.get_stage_data()
                               , gameManager.get_user_data())
    if screen_type == ScreenType.SETTING:
        return SettingController()

    return None


class ScreenController(SurfaceController):

    def __init__(self):
        self.type = ScreenType.MENU
        self.current_surface_controller = MenuController()

        # events
        dispatcher.connect(self.on_change_type_request, signal=SignalMapper.SCREEN_TYPE_CHANGE, sender=dispatcher.Any)

    def on_change_type_request(self, event):
        print(event)
        if isinstance(event, ScreenType):
            controller = get_controller(event)
            if controller:
                self.type = type
                self.current_surface_controller = controller
            else:
                GameManager.getInstance().running = False

    def update(self):
        self.current_surface_controller.update()

    def update_event(self, event):
        self.current_surface_controller.update_event(event)

    def draw(self, surface):
        self.current_surface_controller.draw(surface)

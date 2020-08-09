from utils.utils_factory import UtilsFactory


class GameManager:
    __instance = None

    @staticmethod
    def getInstance():
        if GameManager.__instance is None:
            GameManager()
        return GameManager.__instance

    def __init__(self):
        self.running = True
        self.user_player = 'Firen'
        self.stage = 1

        if GameManager.__instance is not None:
            raise Exception("Singleton")
        else:
            GameManager.__instance = self

    def get_user_data(self):
        return UtilsFactory.get_player_data(self.user_player)

    def get_stage_data(self):
        return UtilsFactory.get_state_data(self.stage)
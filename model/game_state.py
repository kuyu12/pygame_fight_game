import uuid
from pydispatch import dispatcher
from model.player_state import PlayerState
from utils.json_mappers.stage_json_mapper import SignalMapper
from utils.logger import logger


class GameState:

    def __init__(self, player_data, player_id=uuid.uuid4()):
        logger.info("player is added with id: " + str(player_id))
        self.enemies = {}
        self.user_state = PlayerState(player_data, player_id)

        # events
        dispatcher.connect(self.handle_collision_event, signal=SignalMapper.COLLISION_UPDATE, sender=dispatcher.Any)

    def add_enemy(self, enemy_data, enemy_id=uuid.uuid4()):
        logger.info("enemy is added with id: "+str(enemy_id))
        enemy_state = PlayerState(enemy_data, enemy_id)
        self.enemies[str(enemy_id)] = enemy_state

    # subscribe:

    def handle_collision_event(self,message):
        logger.info("collision happened with " + str(message))
        if self.user_state.user_id == message['beaten']:
            beat_enemy = self.enemies.get(message['beat'],None)
            damage = beat_enemy.get_attack_damage(message['attack'],message['state'])
            self.user_state.user_health -= damage
            print(self.user_state.user_health)

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

    def add_enemy(self, enemy_data, enemy_id=uuid.uuid4()):
        logger.info("enemy is added with id: " + str(enemy_id))
        enemy_state = PlayerState(enemy_data, enemy_id)
        self.enemies[str(enemy_id)] = enemy_state

    def handle_collision_event(self, event):
        if self.user_state.user_id == event.beaten:
            beat_enemy = self.enemies.get(event.beat, None)
            damage = beat_enemy.get_attack_damage(event.attack, event.state)
            self.user_state.set_damage(damage)

        elif self.enemies.get(event.beaten):
            damage = self.user_state.get_attack_damage(event.attack, event.state)
            self.enemies.get(event.beaten).set_damage(damage)

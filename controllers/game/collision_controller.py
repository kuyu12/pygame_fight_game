from pydispatch import dispatcher
from model.events.collision_event import CollisionEvent
from utils.const import COLLISION_DELAY_TIME_SEC
from utils.json_mappers.stage_json_mapper import SignalMapper
from views.sprite_views.attack_sprite import AttackState
from views.sprite_views.combo_attack_sprite import ComboAttackSprite
from views.sprite_views.enemy_sprite import EnemySprite
from views.sprite_views.user_sprite import UserSprite
from datetime import datetime


class CollisionController:
    def __init__(self, spriteController):
        self.spriteController = spriteController
        self.collision_delay = {}

    def update(self):
        userSprite = next(filter(lambda x: isinstance(x, UserSprite), self.spriteController.sprites()))
        for sprite in self.spriteController.sprites():
            if isinstance(sprite, EnemySprite) and sprite.rect.colliderect(userSprite.rect):
                if sprite.is_on_attack_mode() and not userSprite.is_on_defence_mode():
                    self.send_attack_event(sprite.player_id, userSprite.player_id, sprite.attack_state,
                                           sprite.state)
                if userSprite.is_on_attack_mode() and not sprite.is_on_defence_mode():
                    self.send_attack_event(userSprite.player_id, sprite.player_id, userSprite.attack_state,
                                           userSprite.state)

            if isinstance(sprite,ComboAttackSprite):
                for sprite_com in self.spriteController.sprites():
                    if isinstance(sprite_com, EnemySprite) and sprite_com.rect.colliderect(sprite.rect) and not sprite_com.is_on_defence_mode():
                        self.send_attack_event("", sprite_com.player_id, AttackState.COMBO,
                                               sprite.state)

    def send_attack_event(self, beat, beaten, attack, state):
        id = beat+beaten
        if id in self.collision_delay:
            if datetime.now() - self.collision_delay[id] > COLLISION_DELAY_TIME_SEC:
                self.collision_delay.pop(id)
            else:
                return

        self.collision_delay[id] = datetime.now()
        dispatcher.send(signal=SignalMapper.COLLISION_UPDATE,
                        event=CollisionEvent(
                            {"beaten": beaten,
                             "beat": beat,
                             "attack": attack,
                             "state": state}))

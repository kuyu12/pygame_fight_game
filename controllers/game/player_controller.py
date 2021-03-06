import pygame
from pydispatch import dispatcher
from model.events.combo_event import ComboEvent
from utils.json_mappers.stage_json_mapper import SignalMapper
from views.sprite_views.attack_sprite import AttackState
from views.sprite_views.movement_sprite import Direction, State


class PlayerController:

    def __init__(self, player,game_state):
        self.player = player
        self.game_state = game_state
        self.dbclock_R = pygame.time.Clock()
        self.dbclock_L = pygame.time.Clock()

    def update_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.dbclock_L.tick() < 250:
                    self.player.control_move(State.RUNNING, Direction.LEFT)
                else:
                    self.player.control_move(State.WALKING, Direction.LEFT)
            if event.key == pygame.K_RIGHT:
                if self.dbclock_R.tick() < 250:
                    self.player.control_move(State.RUNNING, Direction.RIGHT)
                else:
                    self.player.control_move(State.WALKING, Direction.RIGHT)

            if event.key == pygame.K_UP:
                self.player.control_move(State.WALKING, Direction.UP)
            if event.key == pygame.K_DOWN:
                self.player.control_move(State.WALKING, Direction.DOWN)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player.control_move(State.STANDING, Direction.LEFT)
            if event.key == pygame.K_RIGHT:
                self.player.control_move(State.STANDING, Direction.RIGHT)
            if event.key == pygame.K_UP:
                self.player.control_move(State.STANDING, Direction.UP)
            if event.key == pygame.K_DOWN:
                self.player.control_move(State.STANDING, Direction.DOWN)
            if event.key == pygame.K_a:
                self.combo_attack_if_needed(AttackState.HAND)
            if event.key == pygame.K_s:
                self.combo_attack_if_needed(AttackState.FOOT)
            if event.key == pygame.K_d:
                self.player.attack(AttackState.DEFENSE)

    def combo_attack_if_needed(self, attack):
        if self.player.is_attack_combo(attack) and self.game_state.user_state.user_mana > 10:
            dispatcher.send(signal=SignalMapper.COMBO_ATTACK,
                            event=ComboEvent(self.player))
            self.player.attack(AttackState.COMBO)

        else:
            self.player.attack(attack)

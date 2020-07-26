import pygame

from model.AttackSprite import AttackState
from model.movement_sprite import Direction, State


class PlayerController:

    def __init__(self, player):
        self.player = player
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
                self.player.attack(AttackState.HAND)
            if event.key == pygame.K_s:
                self.player.attack(AttackState.FOOT)
            if event.key == pygame.K_d:
                self.player.attack(AttackState.DEFENSE)

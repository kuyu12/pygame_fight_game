import pygame

from views.sprite_views.enemy_sprite import EnemySprite


class SpriteController(pygame.sprite.Group):
    def __init__(self, background, *sprites):
        self.background_group = pygame.sprite.Group(background)
        super().__init__(sprites)

    def update(self, *args, **kwargs):
        super().update()
        self.background_group.update()
        self.sortSpriteByLocation()

    def draw(self, surface, game_state):
        self.background_group.draw(surface)
        super().draw(surface)

        # draw heath bar
        enemies_sprites = filter(lambda x: isinstance(x, EnemySprite), self.sprites())
        for sprite in enemies_sprites:
            enemy_data = game_state.enemies.get(sprite.player_id,None)
            sprite.draw_hp_bar(surface,enemy_data.user_health,enemy_data.user_base_health)

    def sortSpriteByLocation(self):
        sprites = sorted(self.sprites(), key=lambda x: x.rect.centery)
        self.empty()
        super().add(sprites)

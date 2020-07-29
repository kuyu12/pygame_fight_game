import pygame


class SpriteController(pygame.sprite.Group):
    def __init__(self, background, *sprites):
        self.background_group = pygame.sprite.Group(background)
        super().__init__(sprites)

    def update(self, *args, **kwargs):
        super().update()
        self.background_group.update()
        self.sortSpriteByLocation()

    def draw(self, surface):
        self.background_group.draw(surface)
        super().draw(surface)

    def sortSpriteByLocation(self):
        sprites = sorted(self.sprites(), key=lambda x: x.rect.centery)
        self.empty()
        super().add(sprites)
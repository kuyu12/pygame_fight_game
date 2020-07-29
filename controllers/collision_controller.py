from views.sprite_views.enemy_sprite import EnemySprite
from views.sprite_views.user_sprite import UserSprite


class CollisionController:
    def __init__(self, spriteController):
        self.spriteController = spriteController

    def update(self):
        userSprite = next(filter(lambda x: isinstance(x, UserSprite), self.spriteController.sprites()))
        for sprite in self.spriteController.sprites():
            if isinstance(sprite, EnemySprite) and sprite.rect.colliderect(userSprite.rect):
                if sprite.is_on_attack_mode() and not userSprite.is_on_defence_mode():
                    print(userSprite.state)
                    print(userSprite.attack_state)
                    print("you get hit!!")
                if userSprite.is_on_attack_mode() and not sprite.is_on_defence_mode():
                    print("you Attck!")

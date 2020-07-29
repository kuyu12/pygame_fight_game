import pygame
from controllers.player_factory import PlayerSpriteFactory
from controllers.sprite_controller import SpriteController
from views.gui_views.user_info_view import UserInfoView
from controllers.player_controller import PlayerController
from views.sprite_views.background_sprite import BackgroundSprite
from views.sprite_views.enemy_sprite import EnemySprite
from views.sprite_views.player_sprite import PlayerSprite

pygame.init()

running = True

background = BackgroundSprite('background3')
player_data = PlayerSpriteFactory.get_player_data('Frozen')



player = PlayerSprite((200,600),background.size,player_data,1)
player_controller = PlayerController(player)
view = UserInfoView((270, 100), player_data)

enemy_data = PlayerSpriteFactory.get_player_data('Grey')
enemy = EnemySprite((600,600),background.size,enemy_data,player)


sprite_controller = SpriteController(background,player,enemy)

screen = pygame.display.set_mode(background.size)
screen_rect = background.rect
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player_controller.update_event(event)

    sprite_controller.update()
    sprite_controller.draw(screen)
    screen.blit(view, (0, 0))
    pygame.display.update()

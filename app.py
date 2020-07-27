import pygame

from controllers.player_factory import PlayerSpriteFactory
from views.gui_views.user_info_view import UserInfoView
from controllers.player_controller import PlayerController
from views.sprite_views.background_sprite import BackgroundSprite
from views.sprite_views.player_sprite import PlayerSprite

pygame.init()

running = True

background = BackgroundSprite('background3')


player_data = PlayerSpriteFactory.get_player_data('Frozen')
player = PlayerSprite((300,600),background.size,player_data)
controller = PlayerController(player)
view = UserInfoView((270, 100), player_data)

all_sprites = pygame.sprite.Group()
all_sprites.add(background, player)

screen = pygame.display.set_mode(background.size)
screen_rect = background.rect
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        controller.update_event(event)

    all_sprites.update()
    all_sprites.draw(screen)

    screen.blit(view, (0, 0))
    pygame.display.update()

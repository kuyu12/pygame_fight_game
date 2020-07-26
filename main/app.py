import pygame

from main.player_controller import PlayerController
from model.background_sprite import BackgroundSprite
from model.player_sprite import PlayerSprite

running = True

background = BackgroundSprite('background3')
player = PlayerSprite((background.size[0]/2-40,600),background.size)
controller = PlayerController(player)

all_sprites = pygame.sprite.Group()
all_sprites.add(background,player)

screen = pygame.display.set_mode(background.size)
screen_rect = background.rect
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        controller.update_event(event)

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
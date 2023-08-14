import pygame
from sys import exit

from functions import *
from variables import *
from player import *


pygame.init()
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Nauka pygame")
clock = pygame.time.Clock()

# testa = pygame.Rect(0, 0, 12, 12)

# text
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("My game", False, "Green")

# load spritesheet
big_sprite_original = pygame.image.load("graphics/BigSpritev7.png").convert_alpha()

# scale spritesheet

width = big_sprite_original.get_width()
height = big_sprite_original.get_height()
big_sprite = pygame.transform.scale(
    big_sprite_original, (width * scale, height * scale)
)

# player
player = Player(30, 30, big_sprite, "npc_1")

# groups
player_group = pygame.sprite.Group()  # type: ignore
player_group.add(player)  # type: ignore

counter = 0
delta_time = 0
while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # counter
    # print(counter)
    # counter += 0.1
    # if counter > 3:
    #     counter = 0

    # reset screen
    screen.fill((50, 50, 50))

    # blits
    screen.blit(text_surface, (50, 50))
    # screen.blit(big_sprite, (0, 0))

    # draw group
    player_group.draw(screen)
    player_group.update(delta_time)

    pygame.display.flip()

    delta_time = clock.tick(60)

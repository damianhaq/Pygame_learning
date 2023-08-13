import pygame
from sys import exit
from spritesheet_data import spritesheet_data
from functions import *


pygame.init()
screen = pygame.display.set_mode((800, 400))

pygame.display.set_caption("Nauka pygame")
clock = pygame.time.Clock()

# text
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("My game", False, "Green")

# elf
elf = pygame.image.load("graphics/elf_m_idle_anim_f0.png").convert_alpha()
big_sprite_small = pygame.image.load("graphics/BigSpritev7.png").convert_alpha()
# big_sprite = pygame.transform.scale2x(big_sprite_small)
width = big_sprite_small.get_width()
height = big_sprite_small.get_height()
scale = 3
big_sprite = pygame.transform.scale(big_sprite_small, (width * scale, height * scale))

counter = 0
while True:
    # counter
    # print(counter)
    counter += 0.1
    if counter > 3:
        counter = 0

    # reset screen
    screen.fill((50, 50, 50))

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(elf, (0, 0))
    screen.blit(text_surface, (50, 50))

    screen.blit(
        big_sprite,
        (100, 100),
        (
            spritesheet_data["npc_1"]["idle"][int(counter)]["x"] * scale,
            spritesheet_data["npc_1"]["idle"][int(counter)]["y"] * scale,
            spritesheet_data["npc_1"]["idle"][int(counter)]["w"] * scale,
            spritesheet_data["npc_1"]["idle"][int(counter)]["h"] * scale,
        ),
    )

    pygame.display.update()
    clock.tick(60)

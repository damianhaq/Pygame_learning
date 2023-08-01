import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Nauka pygame")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

elf = pygame.image.load("graphics/elf_m_idle_anim_f0.png")
text_surface = test_font.render("My game", False, "Green")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(elf, (0, 0))
    screen.blit(text_surface, (50, 50))

    pygame.display.update()
    clock.tick(60)

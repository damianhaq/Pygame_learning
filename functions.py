# import pygame


# def create_surface_array(spritesheet_data, spritesheet_image):
#     arr = []
#     for sprite in spritesheet_data:
#         print(sprite)

#         sur = pygame.Surface((sprite["w"], sprite["h"])).convert_alpha()
#         sur.blit(spritesheet_image, (0, 0), (0, 0, sprite["w"], sprite["h"]))
#         sur.set_colorkey((0, 0, 0))
#         arr.append(sur)

#     return arr

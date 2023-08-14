import pygame
from spritesheet_data import *
from variables import *


class Player(pygame.sprite.Sprite):
    def __init__(
        self, x: int, y: int, spritesheet: pygame.surface.Surface, npc_name: str
    ):
        super().__init__()
        self.x = x
        self.y = y
        self.spritesheet = spritesheet
        self.npc_name = npc_name
        self.scale: int = scale

        self.current_sprite: int = 0
        self.sub_rects: list[pygame.Rect] = []
        self.current_anim_time: int = 0

        # subsurface return small part of surface
        for i in spritesheet_data["characters"][self.npc_name]["idle"]:
            self.sub_rects.append(
                pygame.Rect(
                    i["x"] * self.scale,
                    i["y"] * self.scale,
                    i["w"] * self.scale,
                    i["h"] * self.scale,
                )
            )

        self.image = self.spritesheet.subsurface(self.sub_rects[self.current_sprite])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.x += 1
            print("space")
            self.rect.move_ip(1, 1)

    def animation_state(self, delta_time: int):
        self.current_anim_time += delta_time
        if self.current_anim_time > 100:
            self.current_sprite += 1
            self.current_anim_time = 0

        if self.current_sprite >= len(
            spritesheet_data["characters"][self.npc_name]["idle"]
        ):
            self.current_sprite = 0
        self.image = self.spritesheet.subsurface(self.sub_rects[self.current_sprite])

    def update(self, delta_time: int):  # type:ignore
        self.player_input()
        self.animation_state(delta_time)

import pygame
import os
from domain.Initvalues import *

dirname = os.path.dirname(__file__)


class Tile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()


        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "tile.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.image.convert()
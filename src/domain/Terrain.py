import pygame
import os
from domain.Initvalues import *

dirname = os.path.dirname(__file__)


class Terrain(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()


        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", filename)
        )

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.image.convert()

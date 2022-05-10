import pygame
import os
from domain.Initvalues import *
from domain.Terrain import Terrain


dirname = os.path.dirname(__file__)


class Tile(Terrain):
    def __init__(self, x, y):

        filename = "tile.png"
        super().__init__(x, y, filename)


        
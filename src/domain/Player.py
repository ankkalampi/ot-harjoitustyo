import pygame
import os
from domain.Initvalues import *
from domain.Entity import Entity
from domain.Initvalues import HEROACCELERATION
from domain.Initvalues import HEROMAXSPEED
from domain.Initvalues import HEROJUMPACCELERATION

dirname = os.path.dirname(__file__)


class Player(Entity):
    def __init__(self, x, y):
        filename = "hero.png"
        acceleration = HEROACCELERATION
        jump_height = HEROJUMP
        max_speed = HEROMAXSPEED
        jump_acceleration = HEROJUMPACCELERATION
        super().__init__(x, y, filename, acceleration, jump_height, max_speed, jump_acceleration)


    
import pygame
import os
from domain.Initvalues import MONSTERACCELERATION, MONSTERJUMPACCELERATION, MONSTERMAXSPEED
from domain.Player import Player
from domain.Initvalues import *
from domain.Entity import Entity
from domain.Behavior import Behavior
from domain.MonsterBehavior import MonsterBehavior

dirname = os.path.dirname(__file__)


class Monster(Entity):
   

    def __init__(self, x, y, player):
        self.player = player
        filename = "monster.png"
        acceleration = MONSTERACCELERATION
        jump_height = MONSTERJUMPACCELERATION
        max_speed = MONSTERMAXSPEED
        jump_acceleration = MONSTERJUMP
        super().__init__(x, y, filename, acceleration, jump_height, max_speed, jump_acceleration)
        self.hunting = False
        self.homex = x
        self.homey = y
        self.behavior = MonsterBehavior(self)
        
    

    def act(self):
        self.behavior.act()
        self.moveself()

    
            
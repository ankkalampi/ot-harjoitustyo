import pygame
import os
from domain.Initvalues import MONSTERACCELERATION, MONSTERJUMPACCELERATION, MONSTERMAXSPEED
from domain.Player import Player
from domain.Initvalues import *
from domain.Entity import Entity


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
        
    
    def hunt(self):
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets","monster.png")
        )
        ##self.image = pygame.transform.scale(self.image, (BLOCKWIDTH * 3, BLOCKHEIGHT * 3))

        self.at_home = False

        if self.rect.x < self.player.rect.x:
                self.going_right = True
                self.going_left = False
        elif self.rect.x > self.player.rect.x:
                self.going_right = False
                self.going_left = True

        if self.rect.x > self.player.rect.x  - 20 and self.rect.y > self.player.rect.y:
            self.jump = True

        if self.rect.x < self.player.rect.x + 20 and self.rect.y > self.player.rect.y:
            self.jump = True

    def go_home(self):
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "monster_passive.png")
        )
        ##self.image = pygame.transform.scale(self.image, (BLOCKWIDTH * 3, BLOCKHEIGHT * 3))

        

        
        
        
        
        if self.rect.x > self.homex:
            self.going_left = True
            self.going_right = False
        elif self.rect.x < self.homex:
            self.going_left = False
            self.going_right = True


        if self.rect.x < self.homex + 10 and self.rect.x > self.homex -10:
            self.going_left = False
            self.going_right = False


        

    

    def act(self):

        if self.player.rect.x > self.rect.x + FOLLOWDISTANCE or self.player.rect.x < self.rect.x - FOLLOWDISTANCE:
            self.hunting = False
        elif self.player.rect.y > self.rect.y +FOLLOWDISTANCE or self.player.rect.y < self.rect.y -FOLLOWDISTANCE:
            self.hunting = False   
        else:   
            self.hunting = True
           
        if self.hunting:
            self.hunt()
        else:
            self.go_home()

        

        self.moveself()
            
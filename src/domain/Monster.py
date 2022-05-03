import pygame
import os
from domain.Player import Player
from domain.Initvalues import HEIGHT, WIDTH, FOLLOWDISTANCE, MONSTERSPEED


dirname = os.path.dirname(__file__)


class Monster(pygame.sprite.Sprite):
   

    def __init__(self, x, y, player):
        super().__init__()


        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "monster.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.homex = x
        self.homey = y

        self.player = player

        self.falling = True
        self.hunting = False


    

    def moveself(self, dx, dy):
        if self.rect.x + dx +39 > WIDTH or self.rect.x + dx < 0:
            dx = 0

        if self.rect.y + dy +54 > HEIGHT or self.rect.y + dy < 0:
            dy = 0
 
        self.rect.move_ip(dx, dy)

        if self.falling:
            self.rect.move_ip(0, 2)

    def act(self):

        if self.player.rect.x > self.rect.x + FOLLOWDISTANCE or self.player.rect.x < self.rect.x - FOLLOWDISTANCE:
            self.hunting = False
        elif self.player.rect.y > self.rect.y +FOLLOWDISTANCE or self.player.rect.y < self.rect.y -FOLLOWDISTANCE:
            self.hunting = False   
        else:   
            self.hunting = True
           
        if self.hunting:
            targetx = self.player.rect.x
            targety = self.player.rect.y
        else:
            targetx = self.homex
            targety = self.homey


        if self.rect.x < targetx:
            dx = MONSTERSPEED
        else:
            dx = -MONSTERSPEED

        if self.rect.y < targety:
            dy = MONSTERSPEED
            
        else:
            dy = -MONSTERSPEED
            
        dy = 0

        self.moveself(dx, dy)
            
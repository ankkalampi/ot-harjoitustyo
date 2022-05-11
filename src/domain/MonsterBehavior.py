import pygame
from domain.Behavior import Behavior
from domain.Initvalues import FOLLOWDISTANCE
import domain.Globals



class MonsterBehavior(Behavior):
    def __init__(self, entity):
        super().__init__(entity)
        self.player = domain.Globals.player
        self.is_go_home = True





    def act(self):

        if self.entity.player.rect.x > self.entity.rect.x + FOLLOWDISTANCE or self.entity.player.rect.x < self.entity.rect.x - FOLLOWDISTANCE:
            self.is_hunt = False
        elif self.entity.player.rect.y > self.entity.rect.y +FOLLOWDISTANCE or self.entity.player.rect.y < self.entity.rect.y -FOLLOWDISTANCE:
            self.is_hunt = False   
        else:   
            self.is_hunt = True
           
        if self.is_hunt:
            self.hunt()
        else:
            self.go_home()
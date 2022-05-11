import pygame
import os

dirname = os.path.dirname(__file__)

class Behavior:
    def __init__(self, entity):
        self.entity = entity
        
        self.is_hunt = False
        self.is_go_home = False




    def act():
        pass



    def hunt(self):
        self.entity.image = pygame.image.load(
            os.path.join(dirname, "..", "assets","monster.png")
        )
        ##self.image = pygame.transform.scale(self.image, (BLOCKWIDTH * 3, BLOCKHEIGHT * 3))

        self.entity.at_home = False

        if self.entity.rect.x < self.entity.player.rect.x:
                self.entity.going_right = True
                self.entity.going_left = False
        elif self.entity.rect.x > self.entity.player.rect.x:
                self.entity.going_right = False
                self.entity.going_left = True

        if self.entity.rect.x > self.entity.player.rect.x  - 20 and self.entity.rect.y > self.entity.player.rect.y:
            self.entity.jump = True

        if self.entity.rect.x < self.entity.player.rect.x + 20 and self.entity.rect.y > self.entity.player.rect.y:
            self.entity.jump = True

    def go_home(self):
        self.entity.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "monster_passive.png")
        )
        ##self.image = pygame.transform.scale(self.image, (BLOCKWIDTH * 3, BLOCKHEIGHT * 3))

        

        
        
        
        
        if self.entity.rect.x > self.entity.homex:
            self.entity.going_left = True
            self.entity.going_right = False
        elif self.entity.rect.x < self.entity.homex:
            self.entity.going_left = False
            self.entity.going_right = True


        if self.entity.rect.x < self.entity.homex + 10 and self.entity.rect.x > self.entity.homex -10:
            self.entity.going_left = False
            self.entity.going_right = False
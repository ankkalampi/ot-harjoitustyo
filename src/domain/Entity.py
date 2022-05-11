import pygame
import os
from domain.Initvalues import *
from domain.Initvalues import FALLINGSPEED
import domain.Globals
from domain.Behavior import Behavior

dirname = os.path.dirname(__file__)

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, acceleration, jump_height, max_speed, jump_acceleration):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", filename)
        )
        self.image.convert()
        
        self.jump_acceleration = jump_acceleration
        self.acceleration = acceleration
        self.max_speed = max_speed
        self.jump_height = jump_height

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.falling = True
        self.jump = False
        self.going_left = False
        self.going_right = False

        self.right_force = 0
        self.left_force = 0
        self.jump_force = 0

        self.can_jump = False
        
        self.deceleration = 1

        self.move_vector = pygame.Vector2()
        self.move_vector.xy = (0,0)

        self.behavior = Behavior(self)
   


    def moveself(self):
 
    ## add force 

        ## add input force
        if self.move_vector.x > -self.max_speed and self.move_vector.x < self.max_speed:
            if self.going_left:
                    self.move_vector.x -= self.acceleration

            if self.going_right:
                    self.move_vector.x += self.acceleration


        if self.jump and self.can_jump:
            self.move_vector.y -= self.jump_height
            self.can_jump = False

        ## add gravity
        if self.move_vector != 0:

            self.move_vector.y += FALLINGSPEED
            self.can_jump = False

        ## add deceleration
        if self.move_vector.x > 0:
            self.move_vector.x -= 1
        elif self.move_vector.x < 0:
            self.move_vector.x += 1


    ## check collision

        ## Check level boundaries, restrict sprite movement over boundaries
        if self.rect.right + self.move_vector.x > domain.Globals.level_width:
            self.move_vector.x = 0
            self.rect.right = domain.Globals.level_width
            
        if self.rect.left + self.move_vector.x < 0:
            self.move_vector.x = 0
            self.rect.left = 0

        if self.rect.bottom + self.move_vector.y > domain.Globals.level_height:
            self.move_vector.y = 0
            self.rect.bottom = domain.Globals.level_height
            self.can_jump = True

        if self.rect.top + self.move_vector.y < 0: 
            self.move_vector.y = 0
            self.rect.top = 0
 

         ## check collision with terrain
        if self.move_vector.x != 0:
            self.move_single_axis(self.move_vector.x, 0)
        if self.move_vector.y != 0:  
            self.move_single_axis(0, self.move_vector.y)


        ## check collision with level floor
        if self.rect.bottom >= domain.Globals.level_height:
            self.can_jump = True
            self.falling = False
            self.move_vector.y = 0





    ## function for moving along a single axis
    ## using this approach prevents glitching when colliding with multiple blocks
    def move_single_axis(self, dx, dy):
        self.rect.move_ip(dx, dy)
        
        for terrain in domain.Globals.all_terrains:
            if self.rect.colliderect(terrain.rect):
                
                if dx > 0: 
                    self.rect.right = terrain.rect.left
                    self.move_vector.x = 0

                if dx < 0: 
                    self.rect.left = terrain.rect.right
                    self.move_vector.x = 0

                if dy > 0: 
                    self.rect.bottom = terrain.rect.top
                    self.move_vector.y = 0
                    self.can_jump = True

                if dy < 0: 
                    self.rect.top = terrain.rect.bottom
                    self.move_vector.y = 0
            



    def act(self):
        pass
    
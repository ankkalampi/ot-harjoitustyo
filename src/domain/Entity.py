import pygame
import os
from domain.Initvalues import *
from domain.Initvalues import FALLINGSPEED
import domain.Globals

dirname = os.path.dirname(__file__)

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, acceleration, jump_height, max_speed, jump_acceleration):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", filename)
        )
        self.image.convert()
        ##self.image = pygame.transform.scale(self.image, (BLOCKWIDTH * 3, BLOCKHEIGHT * 3))

        

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
   


    def moveself(self):

        
        if self.falling:
            
            self.move_vector.y += FALLINGSPEED 
        else:
            self.move_vector.y = 0
        
    

        if self.going_left:
           
            self.move_vector.x -= self.acceleration

        if self.going_right:
            
            self.move_vector.x += self.acceleration

        if self.jump:
            if self.can_jump:

                self.can_jump = False
                self.falling = True
                self.move_vector.y -= self.jump_height
                
                

        if self.move_vector.x < -self.max_speed:
            
            self.move_vector.x = -self.max_speed

        if self.move_vector.x > self.max_speed:
           
            self.move_vector.x = self.max_speed
        

        

        

        if self.move_vector.x < 0:
            
            self.move_vector.x += self.deceleration

        if self.move_vector.x > 0:
            
            self.move_vector.x -= self.deceleration




        if self.rect.right + self.move_vector.x > domain.Globals.level_width:
            
            self.move_vector.x = 0
            self.rect.right = domain.Globals.level_width
            
            
        if self.rect.left + self.move_vector.x < 0:
            
            self.move_vector.x = 0
            self.rect.left = 0

        if self.rect.bottom + self.move_vector.y > domain.Globals.level_height:
            
            self.move_vector.y = 0
            self.rect.bottom = domain.Globals.level_height


        if self.rect.top + self.move_vector.y < 0:
            
            self.move_vector.y = 0
            self.rect.top = 0




        if self.rect.bottom >= domain.Globals.level_height:
            self.can_jump = True
            self.falling = False

        self.rect.move_ip(self.move_vector.x, self.move_vector.y)


    

    def act(self):
        self.moveself()
    
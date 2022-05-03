import pygame
import os
from domain.Initvalues import *
from domain.Initvalues import FALLINGSPEED

dirname = os.path.dirname(__file__)

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, acceleration, jump_height, max_speed, jump_acceleration):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", filename)
        )

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


        self.deceleration = 1
        self.dx = 0
        self.dy = 0
   


    def moveself(self):

        
        
    

        if self.going_left:
            self.dx -= self.acceleration

        if self.going_right:
            self.dx += self.acceleration

        if self.jump:
            self.jump = False
            self.dy -= self.jump_height

        if self.dx < -self.max_speed:
            self.dx = -self.max_speed

        if self.dx > self.max_speed:
            self.dx = self.max_speed
        

        

        if self.falling:
            self.dy += FALLINGSPEED

        if self.dx < 0:
            self.dx += self.deceleration

        if self.dx > 0:
            self.dx -= self.deceleration

        if self.rect.x + self.dx + BLOCKWIDTH > WIDTH or self.rect.x + self.dx < 0:
            self.dx = 0

        if self.rect.y + self.dy + BLOCKHEIGHT > HEIGHT or self.rect.y + self.dy < 0:
            self.dy = 0

        self.rect.move_ip(self.dx, self.dy)


    

    def act(self):
        self.moveself()
    
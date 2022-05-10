import pygame
import os
from domain.Player import Player
from domain.Level import Level
from domain.Initvalues import *
from enum import Enum
import domain.Globals


class Camera_Mode(Enum):
    FOLLOW = 1
    STILL = 2
    SCROLL_LEFT = 3
    SCROLL_RIGHT = 4

class Camera:
    def __init__(self, player, window, level):
        self.player = player
        self.level = level

        self.canvas = pygame.Surface((domain.Globals.level_width, domain.Globals.level_height))
        
        self.display_offset = pygame.Vector2(int(WIDTH /2), int(HEIGHT / 2))
        self.window = window
        
        self.viewport = pygame.Rect((self.player.rect.x - self.display_offset.x), (self.player.rect.y - self.display_offset.y), WIDTH, HEIGHT)
        self.camera_mode = Camera_Mode
        self.camera_mode = Camera_Mode.FOLLOW

        if (self.player.rect.top - self.display_offset.y < 0 ):
            self.viewport.top = 0

        if (self.player.rect.bottom + self.display_offset.y > domain.Globals.level_height):
            self.viewport.bottom = domain.Globals.level_height

        if (self.player.rect.left - self.display_offset.x < 0):
            self.viewport.left = 0

        if (self.player.rect.right + self.display_offset.x > domain.Globals.level_width):
            self.viewport.right =  domain.Globals.level_width

        

        
    def move_camera(self, camera_mode):
        if camera_mode == Camera_Mode.FOLLOW:
            
            ##self.viewport.move_ip(self.player.move_vector.x, self.player.move_vector.y)
            self.viewport.x = self.player.rect.x - self.display_offset.x
            self.viewport.y = self.player.rect.y - self.display_offset.y
            
            

            if (self.player.rect.top - self.display_offset.y < 0 ):
                self.viewport.top = 0
            

            if (self.player.rect.bottom + self.display_offset.y > domain.Globals.level_height):
                self.viewport.bottom = domain.Globals.level_height
            

            if (self.player.rect.left - self.display_offset.x < 0):
                self.viewport.left = 0
            

            if (self.player.rect.right + self.display_offset.x > domain.Globals.level_width):
                self.viewport.right =  domain.Globals.level_width
            

                
             


            

    def update(self):
        self.canvas.fill((10,20,30))
        self.level.all_sprites.draw(self.canvas) 

        self.move_camera(self.camera_mode)
        self.window.blit(self.canvas, (0,0), self.viewport) 

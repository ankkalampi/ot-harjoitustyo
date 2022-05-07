import pygame
import os
from domain.Player import Player
from domain.Level import Level
from domain.Initvalues import *

class Camera:
    def __init__(self, player, canvas, window, level):
        self.player = player
        self.level = level
        print(self.level.level_size_x , "   "  , self.level.level_size_y)

        self.canvas = pygame.Surface((self.level.level_size_x * BLOCKWIDTH, self.level.level_size_y * BLOCKHEIGHT))
        
        self.window = window

       

    def update(self):
        self.canvas.fill((10,20,30))
        self.level.all_sprites.draw(self.canvas) 
        self.canvas.blit(self.canvas, self.player.rect) 
        
        self.window.blit(self.canvas, (0,0)) 


import pygame
from pygame.locals import *
from domain.Level import Level
from domain.Monster import Monster
from domain.NPC import NPC
from domain.Player import Player
from domain.Initvalues import *
from domain.Tile import Tile
from domain.Camera import Camera
 
pygame.init()
 

##canvas = pygame.Surface((WIDTH * 2, HEIGHT * 2))
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Peli")


level1 = Level("level1.txt")
player = level1.player


camera1 = Camera(player, window, level1)

kello = pygame.time.Clock()
oikealle = False
vasemmalle = False
ylos = False
alas = False


run = True

while run:
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.going_left = True
            if event.key == pygame.K_RIGHT:
                player.going_right = True
            if event.key == pygame.K_UP:
                player.jump = True
            if event.key == pygame.K_DOWN:
                alas = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.going_left = False
            if event.key == pygame.K_RIGHT:
                player.going_right = False
            if event.key == pygame.K_UP:
                player.jump = False
            if event.key == pygame.K_DOWN:
                pass
        if event.type == pygame.QUIT:
            run = False

 
    level1.update_level()
    camera1.update()

    
    pygame.display.update()
    kello.tick(100)
    ##print("Falling: " , player.falling, "   Can jump: ", player.can_jump)
pygame.quit()

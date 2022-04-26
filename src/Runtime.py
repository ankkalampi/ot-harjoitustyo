
import pygame
from pygame.locals import *
from domain.Level import Level

 
pygame.init()
 
HEIGHT = 600
WIDTH = 800

 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peli")
level1 = Level()

kello = pygame.time.Clock()
oikealle = False
vasemmalle = False
ylos = False
alas = False

run = True

while run:
    displaysurface.fill((20,30,50))
    level1.all_sprites.draw(displaysurface)
    level1.all_sprites.update()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vasemmalle = True
            if event.key == pygame.K_RIGHT:
                oikealle = True
            if event.key == pygame.K_UP:
                ylos = True
            if event.key == pygame.K_DOWN:
                alas = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vasemmalle = False
            if event.key == pygame.K_RIGHT:
                oikealle = False
            if event.key == pygame.K_UP:
                ylos = False
            if event.key == pygame.K_DOWN:
                alas = False
        if event.type == pygame.QUIT:
            run = False


    if oikealle:
        level1.move_player(10,0)  
    if vasemmalle:
        level1.move_player(-10,0)
    if ylos:
        level1.move_player(0,-10)
    if alas:
        level1.move_player(0,10)     
    pygame.display.flip()
    kello.tick(60)
pygame.quit()

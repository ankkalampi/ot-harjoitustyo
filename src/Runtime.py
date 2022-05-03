
import pygame
from pygame.locals import *
from domain.Level import Level
from domain.Monster import Monster
from domain.NPC import NPC
from domain.Player import Player
from domain.Initvalues import *
from domain.Tile import Tile
 
pygame.init()
 

 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peli")
player = Player(200,50)
monsters = []
NPCs = []
tiles = []
monsters.append(Monster(20, 50, player))
monsters.append(Monster(80, 100, player))
monsters.append(Monster(120, 50, player))

NPCs.append(NPC(80, 30))
NPCs.append(NPC(250, 300))


def build_floor(length, startx, starty, tiles):
    for x in range(1, length):
        tiles.append(Tile((startx + x * 39), starty))



build_floor(20, 420, 500, tiles)

level1 = Level(monsters, NPCs, tiles, player)

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


    
    for monster in monsters:
        monster.act()   

    player.act()

        

    for npc in NPCs:
        pass

    


    pygame.display.flip()
    kello.tick(60)
pygame.quit()

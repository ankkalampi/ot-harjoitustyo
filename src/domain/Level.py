
import pygame
from domain.Initvalues import *
from domain.Monster import Monster
from domain.Player import Player
from domain.Tile import Tile
from domain.NPC import NPC



class Level:
   

    def __init__(self, path):
        self.all_sprites = pygame.sprite.Group()
        self.all_entities_sprites = pygame.sprite.Group()
        self.monster_sprites = pygame.sprite.Group()
        self.NPC_sprites = pygame.sprite.Group()
        self.tile_sprites = pygame.sprite.Group()

        self.monsters = []
        self.NPCs = []
        self.tiles = []
        self.player = Player(0,0)
        self.all_entities = []
        self.level_size = (0,0)
        self.level_size_x = 0
        self.level_size_y = 0

        self.create_level(path)

        self.colliding_entities = dict()


    def create_level(self, path):
        with open(path) as l:
            lines = l.readlines()

       
        coordinate_y = 0
        coordinate_x = 0

        for line in lines:
            coordinate_x = 0
            for chr in line:
                
                if chr == "#":
                    tile = Tile((coordinate_x * BLOCKWIDTH * BLOCK_SIZE), (coordinate_y * BLOCKHEIGHT * BLOCK_SIZE))
                    self.tiles.append(tile)
                    
                    self.all_sprites.add(tile)
                    self.tile_sprites.add(tile)
                    
                elif chr == "N":
                    npc = NPC((coordinate_x * BLOCKWIDTH * BLOCK_SIZE), (coordinate_y * BLOCKHEIGHT * BLOCK_SIZE))
                    self.NPCs.append(npc)
                    self.all_sprites.add(npc)
                    self.NPC_sprites.add(npc)
                    self.all_entities.append(npc)
                    self.all_entities_sprites.add(npc)
                    
                elif chr == "M":
                    monster = Monster((coordinate_x * BLOCKWIDTH * BLOCK_SIZE), (coordinate_y * BLOCKHEIGHT * BLOCK_SIZE), self.player)
                    self.monsters.append(monster)
                    self.all_sprites.add(monster)
                    self.monster_sprites.add(monster)
                    self.all_entities.append(monster)
                    self.all_entities_sprites.add(monster)
                    
                elif chr == "H":
                    self.player.rect.x = coordinate_x * BLOCKWIDTH * BLOCK_SIZE
                    self.player.rect.y = coordinate_y * BLOCKHEIGHT * BLOCK_SIZE
                    self.all_sprites.add(self.player)
                    self.all_entities.append(self.player)
                    self.all_entities_sprites.add(self.player)

                elif chr == "\n":
                    pass
                coordinate_x +=1
            coordinate_y += 1

        self.level_size_x = coordinate_x
        self.level_size_y = coordinate_y


    def update_level(self):

        

        
        for entity in self.all_entities:
            entity.falling = True
            collided = pygame.sprite.spritecollide(entity, self.tiles, False, False)
            for col in collided:
                entity.falling = False

            entity.act()
        

           

           

       

    


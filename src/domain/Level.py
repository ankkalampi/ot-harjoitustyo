import pygame
from domain.Monster import Monster
from domain.Player import Player



class Level:
    def __init__(self, monsters, NPCs, tiles, player):
        self.monsters = monsters
        self.NPCs = NPCs
        self.tiles = tiles
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.monster_sprites = pygame.sprite.Group()
        self.NPC_sprites = pygame.sprite.Group()
        self.tile_sprites = pygame.sprite.Group()
        self._init_sprites()


    def _init_sprites(self):
            
            

            for monster in self.monsters:
                self.all_sprites.add(monster)
                self.monster_sprites.add(monster)

            for npc in self.NPCs:
                self.all_sprites.add(npc)
                self.NPC_sprites.add(npc)

            for tile in self.tiles:
                self.all_sprites.add(tile)
                self.tile_sprites.add(tile)

            self.all_sprites.add(
                
                self.player
            )

    


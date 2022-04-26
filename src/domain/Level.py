import pygame
from domain.Monster import Monster
from domain.Player import Player

class Level:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self._init_sprites()


    def _init_sprites(self):
            self.monster = Monster(20, 50)
            self.player = Player(0, 0)

            self.all_sprites.add(
                self.monster,
                self.player
            )

    def move_player(self, dx, dy):
        self.player.rect.move_ip(dx, dy)


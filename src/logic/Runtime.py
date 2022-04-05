import pygame
from pygame.locals import *
 
pygame.init()
 
HEIGHT = 600
WIDTH = 800

 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peli")

run = True

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.quit()

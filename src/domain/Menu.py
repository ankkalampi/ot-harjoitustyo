import pygame
import os
import domain.Globals
import domain.SaveLoad
from domain.Initvalues import *

dirname = os.path.dirname(__file__)


def load_image(filename):
        image = pygame.image.load(
            os.path.join(dirname, "..", "assets", filename)
        )
        image.convert()

        return image


class MenuItem():
    def __init__(self, menu_image, image_rect, image, passive_image_path, active_image_path, offset):
        self.menu_image = menu_image
        self.offset = offset
        self.image = image
        self.passive_image_path = passive_image_path
        self.active_image_path = active_image_path
        self.image_rect = image_rect

    def make_active(self):
        self.image = load_image(self.active_image_path)

    def make_passive(self):
        self.image = load_image(self.passive_image_path)

    def draw(self):
        self.menu_image.blit(self.image, (self.image_rect.x ,self.offset))




class Menu:

    
    
    def __init__(self, window):

        self.menu_index = 3

        ## button images are loaded
        self.menu_image = load_image("menu_screen.png")
        self.load_button_image = load_image("load_button.png")
        self.save_button_image = load_image("save_button.png")
        self.quit_button_image = load_image("quit_button.png")
        self.start_button_image = load_image("start_button.png")
        self.window = window
    
        ## menu screen is moved to center
        self.menu_rect = self.menu_image.get_rect()
        self.menu_rect.center = (WIDTH / 2, HEIGHT / 2)

        ## button images are moved to center of menu screen, vertical offset not yet added
        self.save_button_rect = self.save_button_image.get_rect()
        self.load_button_rect = self.load_button_image.get_rect()
        self.quit_button_rect = self.quit_button_image.get_rect()
        self.start_button_rect = self.start_button_image.get_rect()

        self.save_button_rect.center = (self.menu_rect.width / 2, self.menu_rect.height / 2 )
        self.load_button_rect.center = (self.menu_rect.width / 2, self.menu_rect.height / 2 )
        self.quit_button_rect.center = (self.menu_rect.width / 2, self.menu_rect.height / 2 )
        self.start_button_rect.center = (self.menu_rect.width / 2, self.menu_rect.height / 2 )

        ## menu item objects are created from button images, vertical offset is added
        self.menu_items = []
        self.menu_items.append(MenuItem(self.menu_image, self.quit_button_rect, self.quit_button_image, "quit_button.png", "quit_button_selected.png", 450))
        self.menu_items.append(MenuItem(self.menu_image, self.load_button_rect, self.load_button_image, "load_button.png", "load_button_selected.png", 350))
        self.menu_items.append(MenuItem(self.menu_image, self.save_button_rect, self.save_button_image, "save_button.png", "save_button_selected.png", 250))
        self.menu_items.append(MenuItem(self.menu_image, self.start_button_rect, self.start_button_image, "start_button.png", "start_button_selected.png", 150))
    



    def build_menu(self):
        self.menu_image.blit(self.start_button_image, (self.start_button_rect.x ,150))
        self.menu_image.blit(self.save_button_image, (self.save_button_rect.x ,250))
        self.menu_image.blit(self.load_button_image, (self.load_button_rect.x ,350))
        self.menu_image.blit(self.quit_button_image, (self.quit_button_rect.x ,450))
        
        

        self.window.blit(self.menu_image, (self.menu_rect.x ,self.menu_rect.y))




    def start_menu(self):
        
        for menuitem in self.menu_items:
            menuitem.draw()
        
        

        self.window.blit(self.menu_image, (self.menu_rect.x ,self.menu_rect.y))
        
        
        
        

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    self.menu_items[ self.menu_index].make_passive()
                    if  self.menu_index == 3:
                        self.menu_index = 0
                        self.menu_items[ self.menu_index].make_active()
                    else:
                        self.menu_index += 1
                        self.menu_items[ self.menu_index].make_active()
                    
                if event.key == pygame.K_DOWN:
                    self.menu_items[ self.menu_index].make_passive()
                    if  self.menu_index == 0:
                        self.menu_index = 3
                        self.menu_items[ self.menu_index].make_active()
                    else:
                        self.menu_index -= 1
                        self.menu_items[ self.menu_index].make_active()
                if event.key == pygame.K_ESCAPE:
                    if domain.Globals.game_is_on:
                        self.close_menu()
                if event.key == pygame.K_RETURN:
                    print("menu index: " , self.menu_index)
                    if self.menu_index == 3:
                        domain.Globals.game_is_on = True
                        self.close_menu()
                    elif self.menu_index == 2:
                        pass
                    elif self.menu_index == 1:
                        pass
                    elif self.menu_index == 0:
                        domain.Globals.app_is_running = False
                    else:
                        pass
            if event.type == pygame.QUIT:
                domain.Globals.app_is_running = False
                        
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    domain.Globals.player.going_left = False
                if event.key == pygame.K_RIGHT:
                    domain.Globals.player.going_right = False
                if event.key == pygame.K_UP:
                    domain.Globals.player.jump = False
                if event.key == pygame.K_DOWN:
                    pass
        

    def close_menu(self):
        domain.Globals.menu_is_active = False

    def start_game():
        pass


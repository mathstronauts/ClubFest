#Road sprite for background
import pygame
import os
import random
from global_variables import *
import global_variables

class Road(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self) #must do this
        self.image = pygame.image.load("road.jpg").convert()
        self.rect = self.image.get_rect()#rectangle that enclose the sprite..defines how wide and tall
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.vx, self.vy = 0,5

#    def get_keys(self):
#        key_state = pygame.key.get_pressed()
#        if (key_state[pygame.K_UP]  and self.vy < 15):
#            self.vy +=1
#            global_variables.SIMULATION_VY  = self.vy
#        elif (key_state[pygame.K_DOWN]  and self.vy > 0):
#            self.vy -=1
#            global_variables.SIMULATION_VY  = self.vy

    def update(self):
#        self.get_keys()
        
        self.vy = global_variables.SIMULATION_VY
        self.rect.y += self.vy
        if self.rect.top > HEIGHT:
            self.rect.top = -1*HEIGHT + (self.rect.top-HEIGHT)

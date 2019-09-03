# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:43:06 2019

@author: Richard
"""
import pygame
import os
import random
from global_variables import *
import global_variables

class Laterals_RandomLane_Slower_TV(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self) #must do this
        self.image = pygame.image.load("car2.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()#rectangle that enclose the sprite..defines how wide and tall
#        self.rect.centery = random.randrange(-3000, -1000)
#        self.rect.centerx = LANE_0_COORD
        self.vx, self.vy = 0,0
        self.state = 0 #default state is zero
        self.tv_init = 1 #flag to initialize a "new" TV
        self.tv_lane = 0
        self.termination_threshold = 20 #number of TVs before termination
        self.tv_reinit_counter=0
        
    def update(self):
        if self.state ==1:
            #TV initialization
            if self.tv_init==1:
                self.vy = self.vy = global_variables.SIMULATION_VY/2
                
                self.tv_lane = random.randrange(0,2)
                if self.tv_lane == 0:
                        self.rect.centerx = LANE_0_COORD
                        global_variables.TARGET_LANE = 0
                else:
                        self.rect.centerx = LANE_1_COORD
                        global_variables.TARGET_LANE = 1
                
                self.rect.centery = random.randrange(-1000, -100)
                self.tv_init = 0
            
            #update longitudinal positon
            self.rect.centery = self.rect.centery + (global_variables.SIMULATION_VY - self.vy)
            global_variables.TARGET_Y_BOTTOM = self.rect.bottom
            
            #Update TV initialization flag and determine scenario termination
            if self.rect.top > HEIGHT: 
                self.tv_init = 1
                self.tv_reinit_counter+=1  
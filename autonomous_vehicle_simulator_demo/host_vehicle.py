# Mathstronauts inc

import pygame
import os
import random
from global_variables import *
import global_variables


class Host_Vehicle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self) #must do this
        self.image = pygame.image.load("car1.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()#rectangle that enclose the sprite..defines how wide and tall
        self.rect.bottom = HEIGHT
        self.rect.centerx = (WIDTH/2)+ (135/2) #width of a lane is 135 pixels
        self.startx_lanechage = self.rect.centerx
        self.lane = 0
        self.vx, self.vy = 0,0
        self.rel_dist = float("inf")
        self.control = "N"
        self.change_lane_status = 0

#    def get_keys(self):
#        self.vx, self.vy = 0,0
#        key_state = pygame.key.get_pressed()
#        if key_state[pygame.K_LEFT] or key_state[pygame.K_a]:
#            self.vx = -SIMULATION_VX
#        if key_state[pygame.K_RIGHT] or key_state[pygame.K_d]:
#            self.vx = SIMULATION_VX   

    def update(self):
#        self.get_keys()
        #lateral motions
#        self.vx = global_variables.SIMULATION_VX
            
#        if global_variables.SIMULATION_CONTROL == b'L':
#            self.rect.centerx = self.startx_lanechage - LANE_WIDTH
#            self.startx_lanechage = self.rect.centerx
#            self.lane += 1
#            global_variables.HOST_LANE = self.lane
#        elif global_variables.SIMULATION_CONTROL == b'R':
#            self.rect.centerx = self.startx_lanechage + LANE_WIDTH
#            self.startx_lanechage = self.rect.centerx
#            self.lane -= 1
#            global_variables.HOST_LANE = self.lane
            
        
        
        if global_variables.SIMULATION_CONTROL == b'L' and self.change_lane_status == 0:
            self.change_lane_status = 1
            self.startx_lanechage = self.rect.centerx
            self.lane += 1
            global_variables.HOST_LANE = self.lane
        elif global_variables.SIMULATION_CONTROL == b'R' and self.change_lane_status == 0:
            self.change_lane_status = -1
            self.startx_lanechage = self.rect.centerx
            self.lane -= 1
            global_variables.HOST_LANE = self.lane
        
        if self.change_lane_status == 1:
            self.vx = -5
        elif self.change_lane_status == -1:
            self.vx = 5
        else:
            self.vx = 0
            
#        #update lateral position w/ lane change    
        self.rect.centerx = self.rect.centerx + self.vx
        if self.rect.centerx < self.startx_lanechage - LANE_WIDTH and self.change_lane_status == 1:
            self.rect.centerx = self.startx_lanechage - LANE_WIDTH
            self.change_lane_status = 0
        elif self.rect.centerx > self.startx_lanechage + LANE_WIDTH and self.change_lane_status == -1:
            self.rect.centerx = self.startx_lanechage + LANE_WIDTH
            self.change_lane_status = 0
            
            
        #prevent vehicle from leaving road    
        if self.rect.left < (WIDTH/2) - 135:
            self.rect.left = (WIDTH/2) - 135
        elif self.rect.right > (WIDTH/2) + 135:
            self.rect.right = (WIDTH/2) + 135
            
        #lane assignment    
        if self.rect.centerx <= (WIDTH/2) + 135 and self.rect.centerx >= (WIDTH/2) and self.change_lane_status == 0:
            self.lane = 0 
            global_variables.HOST_LANE = 0
        elif self.rect.centerx >= (WIDTH/2) - 135 and self.rect.centerx <= (WIDTH/2) and self.change_lane_status == 1:
            self.lane = 1
            global_variables.HOST_LANE = 1
        
        global_variables.HOST_X_CENTER = self.rect.centerx
        
#        print "Host Vehicle: " + str(global_variables.TARGET_Y_BOTTOM)
        self.rel_dist = self.rect.top - global_variables.TARGET_Y_BOTTOM

        print self.change_lane_status
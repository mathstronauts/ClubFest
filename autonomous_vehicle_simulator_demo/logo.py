# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:56:13 2019

@author: Richard
"""

import pygame
import os
import random
from global_variables import *
import global_variables

class Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self) #must do this
        self.image = pygame.image.load("Mathstronauts Official Logo 240x83.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()#rectangle that enclose the sprite..defines how wide and tall
        self.rect.center = ((600-270)/2, HEIGHT/2)
        self.vx, self.vy = 0,5
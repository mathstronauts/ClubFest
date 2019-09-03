# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 08:17:12 2019

@author: Richard
"""

import pygame
import random
import os
from global_variables import *
import global_variables
from Simulation import Road
from logo import Logo
from laterals_scenario import *
from host_vehicle import *
import serial
import time

#initialize serial communication
try:
    if arduino_port.isOpen() == True:
        arduino_port.close()
    
    arduino_port = serial.Serial('com7', 115200)
    
    if arduino_port.isOpen() == False:
        arduino_port.open()

except:
    arduino_port = serial.Serial('com7', 115200)
    
    if arduino_port.isOpen() == False:
        arduino_port.open()

#initialize simulation
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Mathstronauts Autonomous Vehicle Simulator")
clock = pygame.time.Clock()

#create sprites
road_1 = Road()
road_2 = Road()
road_2.rect.center = (WIDTH/2, -1*(HEIGHT/2))
host = Host_Vehicle()
laterals_randomLane_slower = Laterals_RandomLane_Slower_TV()
logo = Logo()
logo2 = Logo()
logo2.rect.centerx=1200-(600-270)/2

#create sprite groups        
all_sprites = pygame.sprite.Group()
road_background = pygame.sprite.Group()
cars = pygame.sprite.Group()
targets = pygame.sprite.Group()

#add sprites to the appropriate sprite groups
all_sprites.add(host)
all_sprites.add(road_1)
all_sprites.add(road_2)

road_background.add(road_1)
road_background.add(road_2)
road_background.add(logo)
road_background.add(logo2)
cars.add(host)
targets.add(laterals_randomLane_slower)

#game looop
running = True
laterals_randomLane_slower.state=1
time.sleep(5)

while running:
    
    #Process input (events)
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False
            arduino_port.close()
    
    
    #update
    if laterals_randomLane_slower.state == 1:
        laterals_randomLane_slower.update()
        
    host.update()
    road_background.update()
#    all_sprites.update()
    
    #send simulation signals
    
    arduino_port.write("{},{}, {}, {},{}\n".format(host.lane,\
                       global_variables.SIMULATION_VY,global_variables.TARGET_LANE,\
                       host.rel_dist,global_variables.TARGET_VY).encode('utf-8'))
    arduino_port.flush()
    arduino_port.flush()
    arduino_port.flushInput()
    arduino_port.flushOutput()
    global_variables.SIMULATION_CONTROL= arduino_port.read()
    
#    print serial_data + 5
 

    #draw/render
    screen.fill(CREAM)
    road_background.draw(screen)
    targets.draw(screen)
    cars.draw(screen)
    pygame.display.flip()
    
    clock.tick(FPS)
    
pygame.quit()
    

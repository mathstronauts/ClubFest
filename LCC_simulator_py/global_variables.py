WIDTH = 1200
HEIGHT = 900
FPS =30

#Simulation parameters
global SIMULATION_VX
global SIMULATION_VY
global SIMULATION_CONTROL
global LANE_WIDTH
global LANE_0_COORD
global LANE_1_COORD
SIMULATION_VX = 5
SIMULATION_VY = 15
SIMULATION_CONTROL = "N"
LANE_WIDTH = 135
LANE_0_COORD=(WIDTH/2) + (135/2)
LANE_1_COORD=(WIDTH/2) - (135/2)

# Host Vehicle Parameters
global HOST_VX
global HOST_VY
global HOST_X_CENTER
global HOST_Y_CENTER
global HOST_LANE

HOST_VX = 0
HOST_VY = 0
HOST_X_CENTER = LANE_0_COORD
HOST_LANE = 0


global TARGET_Y_BOTTOM #rear of vehicle/side of pedestrian facing vehicle
global TARGET_VY
global TARGET_LANE 

TARGET_Y_BOTTOM = 0
TARGET_VY = 0
TARGET_LANE = 0



#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CREAM = (100,100,92)


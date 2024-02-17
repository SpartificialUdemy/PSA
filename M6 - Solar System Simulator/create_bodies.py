from simulation import add_solar_system_body, solar_system_bodies
from colors import *

# Use this guide to add the bodies to the simulator
'''
name - Name of the Solar System Body 
color - Color of the Solar System Body
x - Initial x-Position of Body in Astronomical Units (AU)
y - Initial y-Position of Body (default all set to 0)
mass - Mass of the Solar System Body in Kg
y_vel - Initial velocity of the Body in m/s (-ve sign for counter-clockwise motion)
sun - Set this to 'True' for the body at the center of the Simulator
'''

# Create Solar System Bodies for the Simulator
add_solar_system_body(
    name = "Sun", 
    color = YELLOW_COLOR, 
    x = 0, 
    y = 0, 
    mass = 1.989e30, 
    radius = 30, 
    y_vel = 0, 
    sun=True
)
add_solar_system_body(
    name = "Mercury", 
    color = GRAY_COLOR, 
    x = 0.39, 
    y = 0, 
    mass = 0.33e24, 
    radius = 6, 
    y_vel = -47.4e3
)
add_solar_system_body(
    name = "Venus", 
    color = YELLOWISH_WHITE_COLOR, 
    x = 0.72,
    y = 0, 
    mass = 4.87e24, 
    radius = 14, 
    y_vel = -35e3
)
add_solar_system_body(
    name = "Earth", 
    color = BLUE_COLOR, 
    x = -1, 
    y = 0, 
    mass = 5.97e24, 
    radius = 15, 
    y_vel = 29.8e3
)
add_solar_system_body(
    name = "Mars", 
    color = RED_COLOR, 
    x = -1.52, 
    y = 0, 
    mass = 0.642e24, 
    radius = 8, 
    y_vel = 24.1e3
)



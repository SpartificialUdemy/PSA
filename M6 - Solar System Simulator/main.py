"""Imports"""

# Standard Library Imports
import math
from random import randint

# Third-party Library Imports
import pygame as pg

# Local Imports
from simulation import get_screen_size, create_pygame_window, set_simulation_fonts, simulator
from stars import generate_stars
from parameters import SIMULATION_FPS, TRACK_ORBIT
from create_bodies import solar_system_bodies
from colors import *

"""Solar System Simulator using PyGame"""

# Initialize Pygame
pg.init()

# Simulation Setup
WIDTH, HEIGHT = get_screen_size()
WINDOW = create_pygame_window(WIDTH, HEIGHT)
NAME_FONT, DISTANCE_FONT, PAUSE_FONT = set_simulation_fonts()

# Generate the Background Stars for Simulation
stars_list = generate_stars(num_stars = 450, width = WIDTH, height = HEIGHT)

# Run the Simulation
simulator(
    simulation_fps = SIMULATION_FPS,
    window = WINDOW,
    width = WIDTH,
    height = HEIGHT,
    name_font = NAME_FONT,
    dist_font = DISTANCE_FONT,
    pause_font = PAUSE_FONT,
    stars_list = stars_list,
    track = TRACK_ORBIT
)

# Quit the Pygame
pg.quit()


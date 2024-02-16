"""Imports"""

# Standard Library Imports
import math
from random import randint

# Third-party Library Imports
import pygame as pg

# Local Imports
from simulation import simulation_parameters, simulator
from stars import generate_stars
from parameters import SIMULATION_FPS, TRACK_ORBIT
from create_bodies import solar_system_bodies
from colors import *

"""Solar System Simulator using PyGame"""

# Initialize Pygame
pg.init()

# Get the Simulation Parameters
WIDTH, HEIGHT, WINDOW, NAME_TEXT, DIST_TEXT = simulation_parameters()

# Generate the Background Stars for Simulation
stars_list = generate_stars(num_stars = 450, width = WIDTH, height = HEIGHT)

# Run the Simulation
simulator(
    simulation_fps = SIMULATION_FPS,
    window = WINDOW,
    width = WIDTH,
    height = HEIGHT,
    name_text = NAME_TEXT,
    dist_text = DIST_TEXT,
    stars_list = stars_list,
    track = TRACK_ORBIT
)

# Quit the Pygame
pg.quit()


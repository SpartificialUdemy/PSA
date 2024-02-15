# Libraries
import pygame as pg
import math
from random import randint

# Initialize Pygame
pg.init()

# Create Window
screen_info = pg.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Solar System Simulator')

# Colors
BLACK = (0, 0, 0)

# Stars List with Color, Center and Radius Information
stars_list = [
    {
        'color' : (randint(190, 255), randint(190, 255), randint(190, 255)),
        'center' : (randint(5, WIDTH-5), randint(5, HEIGHT-5)),
        'radius' : (randint(1, 2))
    }
    for star in range(450)
]

# Function to draw stars on the pygame window
def draw_stars(stars_list):
    for star in stars_list:
        pg.draw.circle(WINDOW, star['color'], star['center'], star['radius'])

# Create Simulation
run=True
while run:

    WINDOW.fill(BLACK)
    draw_stars(stars_list)
    
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            run=False
    
    pg.display.update()


# Quit the Pygame
pg.quit()


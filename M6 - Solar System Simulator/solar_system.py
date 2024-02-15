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
WINDOW = pg.display.set_mode((WIDTH-150, HEIGHT-150))
pg.display.set_caption('Solar System Simulator')

# Colors
BLACK = (0, 0, 0)

# Create Simulation
run=True
while run:

    WINDOW.fill(BLACK)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run=False
    
    pg.display.update()


# Quit the Pygame
pg.quit()


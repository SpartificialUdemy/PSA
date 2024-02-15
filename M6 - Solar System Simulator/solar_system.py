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
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
YELLOWISH_WHITE = (255, 255, 246)
BLUE = (0, 0, 255)
RED = (188, 39, 50)

# Class Solar System Bodies
class SolarSystemBodies:

    AU = 1.496e11
    SCALE = 285/AU
    G = 6.6743e-11

    # Constructor
    def __init__(self, name, color, x, y, mass, radius):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius

    # Method 1 - Draw the bodies on the Simulator
    def draw_body(self, WINDOW):
        x = self.x*SolarSystemBodies.SCALE + WIDTH//2
        y = self.y*SolarSystemBodies.SCALE + HEIGHT//2
        pg.draw.circle(surface=WINDOW, color=self.color, center=(x, y), radius=self.radius)

    # Method 2 - Calculate the Gravitational Force
    def gravitational_force(self, ss_body):
        x_diff = ss_body.x - self.x
        y_diff = ss_body.y - self.y
        distance = math.sqrt(x_diff**2 + y_diff**2)
        g_force = self.G * self.mass * ss_body.mass / distance**2
        theta = math.atan2(y_diff/x_diff)
        f_x = g_force * math.cos(theta)
        f_y = g_force * math.sin(theta)
        return f_x, f_y

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

sun = SolarSystemBodies("Sun", YELLOW, 0, 0, 1.989e30, 30)
mercury = SolarSystemBodies("Mercury", GRAY, 0.39*SolarSystemBodies.AU, 0, 0.33e24, 6)
venus = SolarSystemBodies("Venus", YELLOWISH_WHITE, 0.72*SolarSystemBodies.AU, 0, 4.87e24, 14)
earth = SolarSystemBodies("Earth", BLUE, 1*SolarSystemBodies.AU, 0, 5.97e24, 15)
mars = SolarSystemBodies("Mars", RED, 1.52*SolarSystemBodies.AU, 0, 0.642e24, 8)

while run:

    WINDOW.fill(BLACK)
    draw_stars(stars_list)
    
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            run=False
    ss_bodies = [sun, mercury, venus, earth, mars]
    for body in ss_bodies:
        body.draw_body(WINDOW)
    pg.display.update()


# Quit the Pygame
pg.quit()


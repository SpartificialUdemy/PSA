import pygame as pg
from solarsystem import SolarSystemBodies
from stars import draw_stars
from colors import BLACK_COLOR

def simulation_parameters(simulation_fps=60, track_orbit=True):

    # Get screen information
    screen_info = pg.display.Info()
    WIDTH = screen_info.current_w
    HEIGHT = screen_info.current_h

    # Create Pygame window
    WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Solar System Simulator')

    # Fonts to Display on Simulator
    NAME_TEXT = pg.font.SysFont(name='TimesRoman', size=18, bold=True)
    DIST_TEXT = pg.font.SysFont(name='Sans', size=18, bold=True)

    return WIDTH, HEIGHT, WINDOW, NAME_TEXT, DIST_TEXT

ss_bodies = []  # Define the list outside the function
def add_solar_system_body(name, color, x, y, mass, radius, y_vel, sun=False):
    body = SolarSystemBodies(name, color, x, y, mass, radius, y_vel, sun)
    ss_bodies.append(body)
    return ss_bodies

def _simulate_bodies(window, width, height, name_text, dist_text, ss_bodies, track_orbit=True):
    for body in ss_bodies:
        body.update_position(ss_bodies)
        body.draw(window, width, height, name_text, dist_text, track=track_orbit)
    pg.display.update()

def simulator(simulation_fps, window, width, height, name_text, dist_text, stars_list, track):
    run = True
    paused = False
    clock = pg.time.Clock()

    while run:
        clock.tick(simulation_fps)
        window.fill(BLACK_COLOR)
        draw_stars(window, stars_list)

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                elif event.key == pg.K_SPACE:
                    paused = not paused

        if not paused:
            _simulate_bodies(window, width, height, name_text, dist_text, ss_bodies, track)
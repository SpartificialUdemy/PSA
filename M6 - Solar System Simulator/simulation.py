import pygame as pg
from solar_system import SolarSystemBodies
from stars import draw_stars
from colors import BLACK_COLOR

def simulation_parameters():
    """
    Initialize parameters for the Solar System Simulator.

    Returns:
    - WIDTH (int): Width of the Pygame window.
    - HEIGHT (int): Height of the Pygame window.
    - WINDOW (pygame.Surface): Pygame window surface.
    - NAME_TEXT (pygame.font.Font): Font for displaying celestial body names.
    - DIST_TEXT (pygame.font.Font): Font for displaying distance information.
    """
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

solar_system_bodies = []  # List to store all the solar system bodies
def add_solar_system_body(name, color, x, y, mass, radius, y_vel, sun=False):
    """
    Add a celestial body to the solar system.

    Parameters:
    - name (str): Name of the celestial body.
    - color (tuple): RGB tuple representing the color of the celestial body.
    - x (float): Initial x-coordinate of the celestial body.
    - y (float): Initial y-coordinate of the celestial body.
    - mass (float): Mass of the celestial body.
    - radius (float): Radius of the celestial body (circle radius on Simulator).
    - y_vel (float): Initial vertical velocity of the celestial body.
    - sun (bool): Whether the celestial body is the sun (default is False).

    Returns:
    - solar_system_bodies (list): List of SolarSystemBodies objects representing the solar system bodies.
    """
    body = SolarSystemBodies(name, color, x, y, mass, radius, y_vel, sun)
    solar_system_bodies.append(body)
    return solar_system_bodies

def _simulate_bodies(window, width, height, name_text, dist_text, solar_system_bodies, track_orbit=True):
    """
    Simulate the movement and draw the celestial bodies in the solar system.

    Parameters:
    - window (pygame.Surface): Pygame window surface.
    - width (int): Width of the Pygame window.
    - height (int): Height of the Pygame window.
    - name_text (pygame.font.Font): Font for displaying celestial body names.
    - dist_text (pygame.font.Font): Font for displaying distance information.
    - solar_system_bodies (list): List of SolarSystemBodies objects representing the solar system bodies.
    - track_orbit (bool): Whether to track the orbits of celestial bodies (default is True).

    Returns:
    None
    """
    for body in solar_system_bodies:
        body.update_position(solar_system_bodies)
        body.draw(window, width, height, name_text, dist_text, track=track_orbit)
    pg.display.update()

def simulator(simulation_fps, window, width, height, name_text, dist_text, stars_list, track):
    """
    Run the solar system simulation.

    Parameters:
    - simulation_fps (int): Frames per second for the simulation.
    - window (pygame.Surface): Pygame window surface.
    - width (int): Width of the Pygame window.
    - height (int): Height of the Pygame window.
    - name_text (pygame.font.Font): Font for displaying celestial body names.
    - dist_text (pygame.font.Font): Font for displaying distance information.
    - stars_list (list): List of star coordinates for the background.
    - track (bool): Whether to track the orbits of celestial bodies.

    Returns:
    None
    """
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
            _simulate_bodies(window, width, height, name_text, dist_text, solar_system_bodies, track)
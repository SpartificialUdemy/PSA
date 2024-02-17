import pygame as pg
from solar_system import SolarSystemBodies
from stars import draw_stars
from colors import BLACK_COLOR, WHITE_COLOR

def get_screen_size():
    """
    Get screen size for the Solar System Simulator.

    Returns:
    - WIDTH (int): Width of the Pygame window.
    - HEIGHT (int): Height of the Pygame window.
    """
    screen_info = pg.display.Info()
    WIDTH = screen_info.current_w
    HEIGHT = screen_info.current_h
    return WIDTH, HEIGHT

def create_pygame_window(width, height):
    """
    Create Pygame window for the Solar System Simulator.

    Parameters:
    - width (int): Width of the Pygame window.
    - height (int): Height of the Pygame window.

    Returns:
    - WINDOW (pygame.Surface): Pygame window surface.
    """
    WINDOW = pg.display.set_mode((width, height))
    pg.display.set_caption('Solar System Simulator')
    return WINDOW

def set_simulation_fonts(body_font_name, body_font_size, 
                         distance_font_name, distance_font_size,  
                         pause_font_name, pause_font_size):
    """
    Set fonts for the Solar System Simulator.

    Parameters:
    - body_font_name (str): Name of the font for celestial body names.
    - body_font_size (int): Size of the font for celestial body names.
    - distance_font_name (str): Name of the font for distance information.
    - distance_font_size (int): Size of the font for distance information.
    - pause_font_name (str): Name of the font for pause text on the simulator.
    - pause_font_size (int): Size of the font for pause text on the simulator.

    Returns:
    - name_font (pg_font.Font): Font for displaying celestial body names.
    - distance_font (pg_font.Font): Font for displaying distance information.
    - pause_font (pg_font.Font): Font for displaying the pause text on the simulator.
    """
    name_font = pg.font.SysFont(name=body_font_name, size=body_font_size, bold=True)
    distance_font = pg.font.SysFont(name=distance_font_name, size=distance_font_size, bold=True)
    pause_font = pg.font.SysFont(name=pause_font_name, size=pause_font_size, bold=True)  

    return name_font, distance_font, pause_font


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

def simulate_bodies(window, width, height, name_font, dist_font, pause_font, solar_system_bodies, track_orbit=True):
    """
    Simulate the movement and draw the celestial bodies in the solar system.

    Parameters:
    - window (pygame.Surface): Pygame window surface.
    - width (int): Width of the Pygame window.
    - height (int): Height of the Pygame window.
    - name_font (pygame.font.Font): Font for displaying celestial body names.
    - dist_font (pygame.font.Font): Font for displaying distance information.
    - pause_font (pygame.font.Font): Font for displaying the pause text.
    - solar_system_bodies (list): List of SolarSystemBodies objects representing the solar system bodies.
    - track_orbit (bool): Whether to track the orbits of celestial bodies (default is True).

    Returns:
    None
    """
    for body in solar_system_bodies:
        body.update_position(solar_system_bodies)
        body.draw(window, width, height, name_font, dist_font, pause_font, track=track_orbit)


def draw_pause_text(window, width, pause_font, pad_text):
    """
    Draw the pause text onto the window.

    Parameters:
    - window (pygame.Surface): Pygame window surface.
    - width (int): Width of the Pygame window.
    - pad_text (int): Padding to Add on Pause text.

    Returns:
    None
    """ 
    pause_text = pause_font.render('|| Pause',True, WHITE_COLOR)
    text_x = width - pause_text.get_width() - pad_text
    text_y = pad_text
    window.blit(pause_text, (text_x, text_y))

def handle_events(event, run, paused):
    """
    Handle Pygame events related to the simulation.

    Parameters:
    - event (pygame.event.Event): Pygame event object.
    - run (bool): Flag to continue the simulation.
    - paused (bool): Flag indicating whether the simulation is paused.

    Returns:
    Tuple[bool, bool]: Updated values of 'run' and 'paused'.
    """
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            run = False
        elif event.key == pg.K_SPACE:
            paused = not paused
    return run, paused

def simulate_and_update(window, width, height, name_font, dist_font, pause_font, solar_system_bodies, track, static_surface):
    """
    Simulate the movement and update the window.

    Parameters:
    - window (pygame.Surface): Pygame window surface.
    - width (int): Width of the Pygame window.
    - height (int): Height of the Pygame window.
    - name_font (pygame.font.Font): Font for displaying celestial body names.
    - dist_font (pygame.font.Font): Font for displaying distance information.
    - pause_font (pygame.font.Font): Font for displaying pause text.
    - solar_system_bodies (list): List of SolarSystemBodies objects representing the solar system bodies.
    - track (bool): Whether to track the orbits of celestial bodies (default is True).
    - static_surface (pygame.Surface): Surface to hold the static state.

    Returns:
    None
    """
    simulate_bodies(window, width, height, name_font, dist_font, pause_font, solar_system_bodies, track)
    static_surface.blit(window, (0, 0))
    pg.display.update()

def display_paused_state(window, static_surface, width, height, pause_font):
    """
    Display the paused state.

    Parameters:
    - window (pygame.Surface): Pygame window surface.
    - static_surface (pygame.Surface): Surface containing the static state.
    - width (int): Width of the Pygame window.
    - height (int): Height of the Pygame window.

    Returns:
    None
    """
    window.blit(static_surface, (0, 0))
    draw_pause_text(window, width, pause_font, 50)
    pg.display.update()

def simulator(simulation_fps, window, width, height, name_font, dist_font, pause_font, stars_list, track):
    """
    Run the solar system simulation.

    Parameters:
    - simulation_fps (int): Frames per second for the simulation.
    - window (pygame.Surface): Pygame window surface.
    - width (int): Width of the Pygame window.
    - height (int): Height of the Pygame window.
    - name_font (pygame.font.Font): Font for displaying celestial body names.
    - dist_font (pygame.font.Font): Font for displaying distance information.
    - pause_font (pygame.font.Font): Font for displaying pause text on simulator.
    - stars_list (list): List of star coordinates for the background.
    - track (bool): Whether to track the orbits of celestial bodies.

    Returns:
    None
    """

    run = True
    paused = False
    clock = pg.time.Clock()

    static_surface = pg.Surface((width, height))

    while run:
        clock.tick(simulation_fps)
        window.fill(BLACK_COLOR)
        draw_stars(window, stars_list)

        for event in pg.event.get():
            run, paused = handle_events(event, run, paused)

        if not paused:
            simulate_and_update(window, width, height, name_font, dist_font, pause_font, \
                                solar_system_bodies, track, static_surface)
        else:
            display_paused_state(window, static_surface, width, height, pause_font)

        pg.display.update()
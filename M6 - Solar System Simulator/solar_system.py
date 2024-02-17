from colors import NAME_TEXT_COLOR, DIST_TEXT_COLOR, SUN_NAME_COLOR, SUN_TEXT_COLOR
from parameters import SIMULATION_SCALE
import pygame as pg
import math

# Class Info
"""
Represents a celestial body in our solar system.

Class Attributes:
- AU (float): Astronomical Unit, average distance from the Sun to Earth.
- SCALE (float): Simulation scale factor.
- G (float): Gravitational constant.
- TIME_STEP (float): Time step for simulation updates.

Attributes:
- name (str): Name of the celestial body.
- color (tuple): RGB tuple representing the color of the celestial body.
- x (float): Current x-coordinate of the celestial body.
- y (float): Current y-coordinate of the celestial body.
- mass (float): Mass of the celestial body.
- simulator_radius (float): Radius of the celestial body in the simulator.
- sun (bool): Indicates whether the celestial body is the Sun (default is False).
- distance_to_sun (float): Distance to the Sun (used for tracking orbit).
- x_vel (float): Current x-component of velocity.
- y_vel (float): Current y-component of velocity.
- orbit (list): List of positions representing the orbit path.

Methods:
- __init__: Initializes a celestial body with specified parameters.
- _draw_body: Draws the celestial body on the Pygame window.
- _track_orbit: Draws the orbit path of the celestial body.
- draw: Combines _draw_body and _track_orbit for display.
- _gravitational_force: Calculates gravitational force between two celestial bodies.
- update_position: Updates the position of the celestial body based on gravitational forces.

"""

# Celestial Body in our Solar System
class SolarSystemBodies:

    AU = 1.496e11
    SCALE = SIMULATION_SCALE/AU
    G = 6.6743e-11
    TIME_STEP = 24*3600

    def __init__(self, name, color, x, y, mass, simulator_radius, y_vel, sun=False):
        """
        Initialize a celestial body with specified parameters.

        Parameters:
        - name (str): Name of the celestial body.
        - color (tuple): RGB tuple representing the color of the celestial body.
        - x (float): Initial x-coordinate of the celestial body.
        - y (float): Initial y-coordinate of the celestial body.
        - mass (float): Mass of the celestial body.
        - simulator_radius (float): Radius of the celestial body in the simulator.
        - y_vel (float): Initial vertical velocity of the celestial body.
        - sun (bool): Whether the celestial body is the Sun (default is False).

        Returns:
        None
        """
        self.name = name
        self.color = color
        self.x = x*self.AU
        self.y = y
        self.mass = mass
        self.simulator_radius = simulator_radius

        self.sun = sun
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = y_vel
        self.orbit = []

    def _draw_body(self, WINDOW, WIDTH, HEIGHT, NAME_FONT, DIST_FONT):
        """
        Draws the celestial body on the Pygame window.

        Parameters:
        - WINDOW (pygame.Surface): Pygame window surface.
        - WIDTH (int): Width of the Pygame window.
        - HEIGHT (int): Height of the Pygame window.
        - NAME_FONT (pygame.font.Font): Font for displaying celestial body names.
        - DIST_FONT (pygame.font.Font): Font for displaying distance information.

        Returns:
        None
        """
        x = self.x*self.SCALE + WIDTH//2
        y = self.y*self.SCALE + HEIGHT//2
        pg.draw.circle(surface=WINDOW, color=self.color, center=(x, y), radius=self.simulator_radius)

        if not self.sun:
            name_text = NAME_FONT.render(self.name, True, NAME_TEXT_COLOR)
            WINDOW.blit(name_text, (x-40, y-55))
            dist_text = DIST_FONT.render(f"{round(self.distance_to_sun/(3e8*60), 3)} lt-min", True, DIST_TEXT_COLOR)
            WINDOW.blit(dist_text, (x-40, y-35))
        else:
            name_text = NAME_FONT.render(self.name, True, SUN_NAME_COLOR)
            WINDOW.blit(name_text, (x-40, y-78))
            dist_text = DIST_FONT.render(f"{round(self.x/3e8, 3), round(self.y/3e8, 3)} lt-sec", True, SUN_TEXT_COLOR)
            WINDOW.blit(dist_text, (x-40, y-55))

    def _track_orbit(self, WINDOW, WIDTH, HEIGHT):
        """
        Draws the orbit path of the celestial body on the Pygame window.

        Parameters:
        - WINDOW (pygame.Surface): Pygame window surface.
        - WIDTH (int): Width of the Pygame window.
        - HEIGHT (int): Height of the Pygame window.

        Returns:
        None
        """
        if len(self.orbit) > 1:
            centered_points = []
            for (x, y) in self.orbit:
                x = x*self.SCALE + WIDTH//2
                y = y*self.SCALE + HEIGHT//2
                centered_points.append((x, y))
            pg.draw.lines(surface=WINDOW, color=self.color, closed=False, points=centered_points, width=2)

    def draw(self, WINDOW, WIDTH, HEIGHT, NAME_FONT, DIST_FONT, PAUSE_FONT, track=True):
        """
        Combines _draw_body and _track_orbit for display.

        Parameters:
        - WINDOW (pygame.Surface): Pygame window surface.
        - WIDTH (int): Width of the Pygame window.
        - HEIGHT (int): Height of the Pygame window.
        - NAME_FONT (pygame.font.Font): Font for displaying celestial body names.
        - DIST_FONT (pygame.font.Font): Font for displaying distance information.
        - PAUSE_FONT (pygame.font.Font): Font for displaying the pause text.
        - track (bool): Whether to track the orbits of celestial bodies (default is True).

        Returns:
        None
        """
        self._draw_body(WINDOW, WIDTH, HEIGHT, NAME_FONT, DIST_FONT)
        if track:
            self._track_orbit(WINDOW, WIDTH, HEIGHT)

    def _gravitational_force(self, solar_system_body):
        """
        Calculates gravitational force between two celestial bodies.

        Parameters:
        - solar_system_body (SolarSystemBodies): Other celestial body.

        Returns:
        Tuple (float, float): Components of gravitational force.
        """
        x_diff = solar_system_body.x - self.x
        y_diff = solar_system_body.y - self.y
        distance = math.sqrt(x_diff**2 + y_diff**2)
        if solar_system_body.sun:
            self.distance_to_sun = distance
        g_force = self.G * self.mass * solar_system_body.mass / distance**2
        theta = math.atan2(y_diff, x_diff)
        f_x = g_force * math.cos(theta)
        f_y = g_force * math.sin(theta)
        return f_x, f_y

    def update_position(self, solar_system_bodies):
        """
        Updates the position of the celestial body based on gravitational forces.

        Parameters:
        - solar_system_bodies (list): List of SolarSystemBodies objects representing the solar system bodies.

        Returns:
        None
        """
        net_fx, net_fy = 0, 0
        for body in solar_system_bodies:
            if self != body:
                f_x, f_y = self._gravitational_force(body)
                net_fx += f_x
                net_fy += f_y
        self.x_vel += net_fx / self.mass * self.TIME_STEP
        self.y_vel += net_fy / self.mass * self.TIME_STEP
        self.x += self.x_vel * self.TIME_STEP
        self.y += self.y_vel * self.TIME_STEP
        self.orbit.append((self.x, self.y))
from colors import NAME_TEXT_COLOR, DIST_TEXT_COLOR, SUN_NAME_COLOR, SUN_TEXT_COLOR
from parameters import SIMULATION_SCALE
import pygame as pg
import math

# Celestial Body in our Solar System
class SolarSystemBodies:
    """
    Class Constants:
        - AU (float): Astronomical Unit, representing the average distance from the Earth to the Sun in meters.
        - SCALE (float): Scaling factor to convert astronomical units to pixels for simulation display.
        - G (float): Gravitational constant in m^3 kg^-1 s^-2.
        - TIME_STEP (float): Time step for simulation in seconds.
    """
    AU = 1.496e11
    SCALE = SIMULATION_SCALE/AU
    G = 6.6743e-11
    TIME_STEP = 24*3600

    def __init__(self, name, color, x, y, mass, simulator_radius, y_vel, sun=False):
        """
        Represents a celestial body in the solar system.

        Attributes:
            name (str): The name of the body.
            color (tuple): RGB color tuple.
            x (float): Initial X-coordinate.
            y (float): Initial Y-coordinate.
            mass (float): Mass of the body.
            radius (float): Radius of the Simulator body.
            sun (bool): True if the body is the sun.
            distance_to_sun (float): Distance to the sun (initialized to 0).
            x_vel (float): Initial horizontal velocity (initialized to 0).
            y_vel (float): Initial vertical velocity.
            orbit (list): List to store orbit coordinates.
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

    def _draw_body(self, WINDOW, WIDTH, HEIGHT, NAME_TEXT, DIST_TEXT):
        """
        Draw the celestial body on the simulator window.

        Args:
            WINDOW (pygame.Surface): The Pygame surface representing the simulator window.

        Returns:
            None
        """

        x = self.x*self.SCALE + WIDTH//2
        y = self.y*self.SCALE + HEIGHT//2
        pg.draw.circle(surface=WINDOW, color=self.color, center=(x, y), radius=self.simulator_radius)

        if not self.sun:
            name_text = NAME_TEXT.render(self.name, True, NAME_TEXT_COLOR)
            WINDOW.blit(name_text, (x-40, y-55))
            dist_text = DIST_TEXT.render(f"{round(self.distance_to_sun/(3e8*60), 3)} lt-min", True, DIST_TEXT_COLOR)
            WINDOW.blit(dist_text, (x-40, y-35))
        else:
            name_text = NAME_TEXT.render(self.name, True, SUN_NAME_COLOR)
            WINDOW.blit(name_text, (x-40, y-78))
            dist_text = DIST_TEXT.render(f"{round(self.x/3e8, 3), round(self.y/3e8, 3)} lt-sec", True, SUN_TEXT_COLOR)
            WINDOW.blit(dist_text, (x-40, y-55))

    def _track_orbit(self, WINDOW, WIDTH, HEIGHT):
        """
        Track and draw the orbit of the celestial body on the simulator window.

        Args:
            WINDOW (pygame.Surface): The Pygame surface representing the simulator window.

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

    def draw(self, WINDOW, WIDTH, HEIGHT, NAME_TEXT, DIST_TEXT, track=True):
        """
        Draw the celestial body and its orbit on the simulator window.

        Args:
            WINDOW (pygame.Surface): The Pygame surface representing the simulator window.
            track (bool, optional): If True, the orbit of the celestial body will be drawn. Default is True.

        Returns:
            None
        """
        self._draw_body(WINDOW, WIDTH, HEIGHT, NAME_TEXT, DIST_TEXT)
        if track:
            self._track_orbit(WINDOW, WIDTH, HEIGHT)

    def _gravitational_force(self, ss_body):
        """
        Calculate the gravitational force between this celestial body and another.

        Args:
            ss_body (SolarSystemBodies): Another celestial body for which gravitational force is calculated.

        Returns:
            Tuple[float, float]: The components of the gravitational force in the x and y directions.
        """
        x_diff = ss_body.x - self.x
        y_diff = ss_body.y - self.y
        distance = math.sqrt(x_diff**2 + y_diff**2)
        if ss_body.sun:
            self.distance_to_sun = distance
        g_force = self.G * self.mass * ss_body.mass / distance**2
        theta = math.atan2(y_diff, x_diff)
        f_x = g_force * math.cos(theta)
        f_y = g_force * math.sin(theta)
        return f_x, f_y

    def update_position(self, ss_bodies):
        """
        Update the position of the celestial body based on gravitational interactions.

        Args:
            ss_bodies (List[SolarSystemBodies]): List of other celestial bodies in the solar system.

        Returns:
            None
        """
        net_fx, net_fy = 0, 0
        for ss_body in ss_bodies:
            if self != ss_body:
                f_x, f_y = self._gravitational_force(ss_body)
                net_fx += f_x
                net_fy += f_y
        self.x_vel += net_fx / self.mass * self.TIME_STEP
        self.y_vel += net_fy / self.mass * self.TIME_STEP
        self.x += self.x_vel * self.TIME_STEP
        self.y += self.y_vel * self.TIME_STEP
        self.orbit.append((self.x, self.y))
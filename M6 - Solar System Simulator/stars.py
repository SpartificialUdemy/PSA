from random import randint
import pygame as pg

def generate_stars(num_stars, width, height):
    """
    Generate a list of stars with random positions and colors.

    Parameters:
    - num_stars (int): Number of stars to generate.
    - width (int): Width of the Pygame window.
    - height (int): Height of the Pygame window.

    Returns:
    list: List of star dictionaries, each containing color, center coordinates, and radius.
    """
    stars_list = [
        {
            'color': (randint(190, 255), randint(190, 255), randint(190, 255)),
            'center': (randint(5, width-5), randint(5, height-5)),
            'radius': (randint(1, 2))
        }
        for _ in range(num_stars)
    ]
    return stars_list

# Draw stars on the pygame window
def draw_stars(WINDOW, stars_list):
    """
    Draw stars on the Pygame window.

    Parameters:
    - WINDOW (pygame.Surface): Pygame window surface.
    - stars_list (list): List of star dictionaries, each containing color, center coordinates, and radius.

    Returns:
    None
    """
    for star in stars_list:
        pg.draw.circle(WINDOW, star['color'], star['center'], star['radius'])
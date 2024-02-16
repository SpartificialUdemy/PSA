from random import randint
import pygame as pg

def generate_stars(num_stars, width, height):
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
    Draw stars on the simulator window.

    Args:
        stars_list (List[Dict[str, Union[Tuple[int, int, int], Tuple[int, int], int]]]): List of dictionaries representing stars.
            Each dictionary must contain 'color' (RGB tuple), 'center' (center coordinates tuple), and 'radius' (integer).

    Returns:
        None
    """
    for star in stars_list:
        pg.draw.circle(WINDOW, star['color'], star['center'], star['radius'])
import matplotlib.pyplot as plt
import numpy as np
import json

def read_json_config(file_path):
    """
    Read a JSON configuration file and return the configuration data.

    Parameters:
    - file_path (str): The path to the JSON configuration file.

    Returns:
    - dict: A dictionary containing the configuration data.
    """
    # Load the JSON file for Configuration
    with open(file_path, 'r') as file:
        config_data = json.load(file)
    return config_data

def accn(G, M_sun, r):
    """
    Calculate the gravitational acceleration of Earth due to the mass of the Sun.

    Parameters:
    - G (float): Universal Gravitational Constant.
    - M_sun (float): Mass of the Sun in kilograms.
    - r (numpy.ndarray): Position vector representing the distance from the Sun to Earth.

    Returns:
    - numpy.ndarray: Acceleration vector of Earth due to the gravitational force from the Sun.

    Formula:
    - The gravitational acceleration (a) is calculated using the formula:
        a = (-G * M_sun / |r|^3) * r_from_sun_to_earth

    where:
    - G is the Universal Gravitational Constant,
    - M_sun is the mass of the Sun,
    - |r| is the magnitude of the position vector r, and
    - r_from_sun_to_earth is the unit vector pointing from the Sun to Earth.

    Note:
    - The negative sign indicates that the acceleration is directed towards the Sun.
    """
    return (-G * M_sun / np.linalg.norm(r)**3) * r

def euler_method(G, M_sun, r, v, accn, dt):
    """
    Perform numerical simulation using the Euler method for solving ordinary differential equations (ODEs).

    Equations:
    1. ODE for Position:
        dr/dt = v
        r_new = r_old + v_old * dt

    2. ODE for Velocity:
        dv/dt = a
        v_new = v_old + a(r_old) * dt

    Parameters:
    - G (float): Universal Gravitational Constant.
    - M_sun (float): Mass of the Sun in kilograms.
    - r (numpy.ndarray): Array representing the position vector at each time step.
    - v (numpy.ndarray): Array representing the velocity vector at each time step.
    - accn (function): Function to calculate acceleration at a given position.
    - dt (float): Time step for the simulation.

    This function updates the position and velocity arrays (r and v) with simulated data based on the Euler method.

    Note:
    - The provided arrays r and v should be initialized with the initial conditions of the simulation.
    """

    # For each time step, apply Euler Integration
    for i in range(1, len(r)):
        r[i] = r[i-1] + v[i-1] * dt
        v[i] = v[i-1] + accn(G, M_sun, r[i-1]) * dt

def rk4_method(G, M_sun, r, v, accn, dt):
    """
    Perform numerical simulation using the Runge-Kutta (4th Order) method for solving ordinary differential equations (ODEs).

    Equations:
    1. ODE for Position:
        dr/dt = v
        r_new = r_old + dt/6 * (k1r + 2*k2r + 2*k3r + k4r)

    2. ODE for Velocity:
        dv/dt = a
        v_new = v_old + dt/6 * (k1v + 2*k2v + 2*k3v + k4v)

    Method to calculate the steps:
    ------------------------------
    Step 1: k1
        k1v = accn(r[i-1])
        k1r = v[i-1]

    Step 2: k2, dt/2 using step 1
        k2v = accn(r[i-1] + k1r * dt/2)
        k2r = v[i-1] + k1v * dt/2

    Step 3: k3, dt/2 using step 2
        k3v = accn(r[i-1] + k2r * dt/2)
        k3r = v[i-1] + k2v * dt/2

    Step 4: k4, dt using step 3
        k4v = accn(r[i-1] + k3r * dt)
        k4r = v[i-1] + k3v * dt

    Parameters:
    - G (float): Universal Gravitational Constant.
    - M_sun (float): Mass of the Sun in kilograms.
    - r (numpy.ndarray): Array representing the position vector at each time step.
    - v (numpy.ndarray): Array representing the velocity vector at each time step.
    - accn (function): Function to calculate acceleration at a given position.
    - dt (float): Time step for the simulation.

    This function updates the position and velocity arrays (r and v) with simulated data based on the Runge-Kutta (4th Order) method.

    Note:
    - The provided arrays r and v should be initialized with the initial conditions of the simulation.
    """

    # For each time step, apply Runge-Kutta (4th Order)
    for i in range(1, len(r)):
        # Step 1:- 0
        k1v = accn(G, M_sun, r[i-1])
        k1r = v[i-1]

        # Step 2:- dt/2 using step 1
        k2v = accn(G, M_sun, r[i-1] + k1r * dt/2)
        k2r = v[i-1] + k1v * dt/2

        # Step 3:- dt/2 using step 2
        k3v = accn(G, M_sun, r[i-1] + k2r * dt/2)
        k3r = v[i-1] + k2v * dt/2

        # Step 4:- dt using step 3
        k4v = accn(G, M_sun, r[i-1] + k3r * dt)
        k4r = v[i-1] + k3v * dt

        # Get the Velocity and Position Vectors for a given Time Step
        v[i] = v[i-1] + dt/6*(k1v + 2*k2v + 2*k3v + k4v)
        r[i] = r[i-1] + dt/6*(k1r + 2*k2r + 2*k3r + k4r)

def numerical_integration(G, M_sun, r, v, accn, dt, method):
    """
    Apply numerical integration to simulate the motion of a celestial body using the specified method.

    Parameters:
    - G (float): Universal Gravitational Constant.
    - M_sun (float): Mass of the Sun in kilograms.
    - r (numpy.ndarray): Array representing the position vector at each time step.
    - v (numpy.ndarray): Array representing the velocity vector at each time step.
    - accn (function): Function to calculate acceleration at a given position.
    - dt (float): Time step for the simulation.
    - method (str): Integration method, either "euler" or "rk4".

    Raises:
    - Exception: If the provided method is neither "euler" nor "rk4".

    Returns:
    - None: Updates the provided position (r) and velocity (v) arrays in-place.
    """

    if method.lower() == 'euler':
        euler_method(G, M_sun, r, v, accn, dt)
    elif method.lower() == 'rk4':
        rk4_method(G, M_sun, r, v, accn, dt)
    else:
        raise Exception(f'Invalid method. Choose either "euler" or "rk4". Provided method: {method}')

def at_aphelion(r, v):
    """
    Determine the Aphelion position and associated parameters from simulated data.

    Parameters:
    - r (numpy.ndarray): Simulated data array for the positions of the planet.
    - v (numpy.ndarray): Simulated data array for the velocities of the planet.

    Returns:
    Tuple[int, float, float]: A tuple containing:
        - arg_aphelion (int): The index at which the planet is at its Aphelion.
        - vel_aphelion (float): The velocity of the planet at its Aphelion.
        - pos_aphelion (float): The position of the planet at its Aphelion.
    """
    # Get the total size of all the position vectors in r array
    sizes = np.array([np.linalg.norm(position) for position in r])
    pos_aphelion = np.max(sizes)
    arg_aphelion = np.argmax(sizes)
    vel_aphelion = np.linalg.norm(v[arg_aphelion])
    return arg_aphelion, vel_aphelion, pos_aphelion

def plot_simulated_data(r, method_integration, arg_aphelion,
                        vel_aphelion, pos_aphelion, name_planet, color_peri, color_ap):
    """
    Generate a 3D plot from simulated data representing the orbit of a planet.

    Parameters:
    - r (numpy.ndarray): Simulated data for the position of the planet.
    - method_integration (str): The numerical integration method used ("euler" or "rk4").
    - arg_aphelion (int): The index at which the planet is at its Aphelion.
    - vel_aphelion (float): The velocity of the planet at its Aphelion.
    - pos_aphelion (float): The position of the planet at its Aphelion.
    - name_planet (str): The name of the Planet.
    - color_peri (str): The color of the marker at Perihelion.
    - color_ap (str): The color of the marker at Aphelion.
    """

    # Setup the Figure and Axis for the Subplot
    plt.style.use('dark_background')
    plt.figure(figsize=(7, 12))
    plt.subplot(projection='3d')

    # Add Suptitle
    suptitle_str = 'RK4' if method_integration.lower() == 'rk4' else 'Euler'
    plt.suptitle(suptitle_str + ' Method', color='r', fontsize=18, weight='bold')

    # Add Title
    title_str = f'At Aphelion, the {name_planet} is {round(pos_aphelion/1e9, 1)} million km away from the Sun\nMoving at the speed of {round(vel_aphelion/1e3, 1)} km/s.'
    plt.title(title_str, fontsize=14, color='orange')

    # Plot the Orbit, Sun, Earth at Perihelion and Aphelion
    plt.plot(r[:, 0], r[:, 1], color='tab:pink', lw=2, label='Orbit')
    plt.scatter(0, 0, color='yellow', s=1000, label='Sun')
    plt.scatter(r[0,0], r[0,1], s=200, label=f'{name_planet} at its Perihelion', color=color_peri)
    plt.scatter(r[arg_aphelion,0], r[arg_aphelion,1], s=200,
                label=f'{name_planet} at its Aphelion', color=color_ap)

    # Add Legend and Customize it
    legend = plt.legend(loc='lower right', frameon=False)
    for i in range(1, 4):
        legend.legend_handles[i]._sizes = [150] if i == 1 else [80]

    # Turn off the axis and Display the result
    plt.axis('off')
    plt.show()

# Imports
from utils import read_json_config, accn, numerical_integration, at_aphelion, plot_simulated_data
import numpy as np

def setup_simulation(config):
    # Access configuration values
    planet_name = config['planet_info']['name'] 
    color_at_perihelion = config['planet_info']['perihelion_color']
    color_at_aphelion = config['planet_info']['aphelion_color']
    initial_position = np.array(config['initial_conditions']['position_at_perihelion'])*1e9 # m
    initial_velocity = np.array(config['initial_conditions']['velocity_at_perihelion'])*1e3 # m/s
    time_step = config['time_settings']['time_step'] # sec
    max_time = config['time_settings']['simulation_time']*24*3600 # sec
    method_integration = config['numerical_integration']['method'] 

    # Time array for numerical solution
    t = np.arange(0, max_time, time_step)

    # Initialize arrays to store positions and velocities at all time steps
    r = np.empty(shape=(len(t), 2))
    v = np.empty(shape=(len(t), 2))

    # Set initial conditions for position and velocity
    r[0], v[0] = np.array([initial_position, 0]), np.array([0, -initial_velocity])

    return planet_name, color_at_perihelion, color_at_aphelion, r, v, t, time_step, method_integration
 
# Read config.json
config = read_json_config("config.json")

# Constants
G = 6.6743e-11    
M_SUN = 1.989e30  # kg

# Setup simulation
planet_name, color_at_perihelion, color_at_aphelion, \
      r, v, t, time_step, method_integration = setup_simulation(config)

# Call numerical integration
numerical_integration(G, M_SUN, r, v, accn, time_step, method=method_integration,)

# Get data of Earth at its Aphelion
arg_aphelion, vel_aphelion, pos_aphelion = at_aphelion(r, v)

# Plot the simulated data
plot_simulated_data(r, method_integration, arg_aphelion, vel_aphelion, pos_aphelion, 
                    planet_name, color_at_perihelion, color_at_aphelion)

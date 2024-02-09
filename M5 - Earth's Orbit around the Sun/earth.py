# Imports
import argparse
from utils import read_json_config, accn, numerical_integration, at_aphelion, plot_simulated_data
import numpy as np

def setup_simulation(config):
    # Access configuration values
    initial_position = np.array(config['initial_conditions']['r_0'])
    initial_velocity = np.array(config['initial_conditions']['v_0'])
    time_step = config['time_settings']['dt']
    max_time = config['time_settings']['t_max']
    method_integration = config['numerical_integration']['method']

    # Time array for numerical solution
    t = np.arange(0, max_time, time_step)

    # Initialize arrays to store positions and velocities at all time steps
    r = np.empty(shape=(len(t), 2))
    v = np.empty(shape=(len(t), 2))

    # Set initial conditions for position and velocity
    r[0], v[0] = initial_position, initial_velocity

    return r, v, t, time_step, method_integration

# Read config.json
config = read_json_config("config.json")

# Constants
G = 6.6743e-11    
M_SUN = 1.989e30  # kg

# Setup simulation
r, v, t, time_step, method_integration = setup_simulation(config)

# Call numerical integration
numerical_integration(G, M_SUN, r, v, accn, time_step, method=method_integration)

# Get data of Earth at its Aphelion
arg_aphelion, vel_aphelion, pos_aphelion = at_aphelion(r, v)

# Plot the simulated data
plot_simulated_data(r, method_integration, arg_aphelion, vel_aphelion, pos_aphelion)

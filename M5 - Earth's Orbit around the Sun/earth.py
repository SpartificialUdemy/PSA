'''
Problem Statement
------------------
- Create a simulation to track the orbit of the Earth around the Sun for a period of 1 year.
- Use Euler and Runge - Kutta method of 4th order (RK4) for this task.
- Find the distance from Earth to Sun at Apogee using Euler and RK4 method and compare it with the original.

Given Equations
----------------
Accn of Earth due to Gravity of the Sun 
--> a = (-GM / |r|^3) * r_vec

ODE for Position
--> dr/dt = v 

ODE for Velocity
--> dv/dt = a 

Initial Condition
-----------------
--> Earth is at its Perihelion (closest to Sun)
'''

# Imports
import matplotlib.pyplot as plt
import numpy as np

# Constants
G = 6.6743e-11
M_sun = 1.989e30 # kg

# Initial Position and Velocity
r_0 = np.array([147.1e9, 0]) # m
v_0 = np.array([0, -30.29e3]) # m/s

# Time steps and total time for simulation
dt = 3600 # secs
t_max = 3.154e7 # secs

# Time array to be used in numerical solution
t = np.arange(0, t_max, dt)


# Initialize arrays to store positions and velocities at all the time steps
r = np.empty(shape=(len(t), 2))
v = np.empty(shape=(len(t), 2))

# Set the Initial conditions for position and velociity
r[0], v[0] = r_0, v_0

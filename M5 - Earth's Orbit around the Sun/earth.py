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

# Define the function that gets us the accn vector when passed in the position vector
def accn(r):
    return (-G*M_sun / np.linalg.norm(r)**3) * r

# Euler Integration
def euler_method(r, v, accn, dt):
    """
    Equations for euler method
    ---------------------------
    ODE for Position
    --> dr/dt = v 
    --> r_new = r_old + v_old*dt

    ODE for Velocity
    --> dv/dt = a 
    --> v_new = v_old + a(r_old)*dt

    Parameters
    ----------
    r: empty array for position of size t
    v: empty array for velocity of size t
    a: func to calculate the accn at give position
    dt: time step for the simulation

    This function will update the empty arrays for r and v with the simulated data
    """

    for i in range(1, len(t)):
        r[i] = r[i-1] + v[i-1] * dt
        v[i] = v[i-1] + accn(r[i-1]) * dt


# RK4 Integration
def rk4_method(r, v, accn, dt):
    """
    Equations for euler method
    ---------------------------
    ODE for Position
    --> dr/dt = v 
    --> r_new = r_old + dt/6(k1r + 2*k2r + 2*k3r + k4r)

    ODE for Velocity
    --> dv/dt = a 
    --> v_new = v_old + dt/6(k1v + 2*k2v + 2*k3v + k4v)

    Method to calculate the steps
    -----------------------------
    Step 1:- 0
    k1v = accn(r[i-1])
    k1r = v[i-1]

    Step 2:- dt/2 using step 1
    k2v = accn(r[i-1] + k1r * dt/2)
    k2r = v[i-1] + k1v * dt/2 

    Step 3:- dt/2 using step 2
    k3v = accn(r[i-1] + k2r * dt/2)
    k3r = v[i-1] + k2v * dt/2       

    Step 4:- dt using step 3
    k4v = accn(r[i-1] + k3r * dt)
    k4r = v[i-1] + k3v * dt

    Parameters
    ----------
    r: empty array for position of size t
    v: empty array for velocity of size t
    a: func to calculate the accn at give position
    dt: time step for the simulation

    This function will update the empty arrays for r and v with the simulated data
    """

    for i in range(1, len(r)):
        # Step 1:- 0
        k1v = accn(r[i-1])
        k1r = v[i-1]

        # Step 2:- dt/2 using step 1
        k2v = accn(r[i-1] + k1r * dt/2)
        k2r = v[i-1] + k1v * dt/2 

        # Step 3:- dt/2 using step 2
        k3v = accn(r[i-1] + k2r * dt/2)
        k3r = v[i-1] + k2v * dt/2       

        # Step 4:- dt using step 3
        k4v = accn(r[i-1] + k3r * dt)
        k4r = v[i-1] + k3v * dt

        # Update the r and v
        v[i] = v[i-1] + dt/6*(k1v + 2*k2v + 2*k3v + k4v)
        r[i] = r[i-1] + dt/6*(k1r + 2*k2r + 2*k3r + k4r)

def numerical_integration(r, v, accn, dt, method='euler'):
    """
    This function will apply the numerical_integration based on the method choosen
    If the method is euler or rk4, the respective method will be implemented
    Else it will raise an Exception

    Parameters
    ----------
    r: empty array for position of size t
    v: empty array for velocity of size t
    a: func to calculate the accn at give position
    dt: time step for the simulation
    method: either "euler" or "rk4"
    """
    if method.lower()=='euler':
        euler_method(r, v, accn, dt)
    elif method.lower()=='rk4':
        rk4_method(r, v, accn, dt)
    else:
        raise Exception(f'You can either choose "euler" or "rk4". Your current input for method is:- {method}')

# Call the numerical integration
numerical_integration(r, v, accn, dt, method='lmao')

# Find the point at which Earth is at its Aphelion
sizes = np.array([np.linalg.norm(position) for position in r])
pos_aphelion = np.max(sizes)
arg_aphelion = np.argmax(sizes)
vel_aphelion = np.linalg.norm(v[arg_aphelion])

print(pos_aphelion/1e9, vel_aphelion/1e3)
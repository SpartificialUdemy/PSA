# 1) Problem Statement

* Create a simulation to track the orbit of the Earth around the Sun for a period of 1 year.
* Use Euler and Runge - Kutta method of 4th order (RK4) for this task.
* Find the distance from Earth to Sun at Apogee using Euler and RK4 method and compare it with the original.

## 1.1) Given Equations

* Accn of Earth due to Gravity of the Sun 
    * $a = -\frac{GM}{|r|^3}\times\vec{r}$

* ODE for Position
    * $\frac{dr}{dt} = v$ 

* ODE for Velocity
   * $\frac{dv}{dt} = a$

## 1.2) Initial Condition
* Earth is at its Perihelion (closest to Sun)

## 1.3) Simulated Output
<img src="earth_orbit.png" alt="Orbit of the Earth" width=50%>

---

# 2) Setup to run for any Planet
1. Clone the Repository:- `https://github.com/SpartificialUdemy/PSA.git`
2. Change into the project directory:- cd "M5 - Earth's Orbit around the Sun"
4. Install `requirements.txt`:- pip install -r requirements.txt

# 3) Useage
1. Change the Simulation Configuration thorough [`config.json`](https://github.com/SpartificialUdemy/PSA/blob/main/M5%20-%20Earth's%20Orbit%20around%20the%20Sun/config.json)
2. Run through terminal:- `python earth.py`


# Problem Statement

* Create a simulation to track the orbit of the Earth around the Sun for a period of 1 year.
* Use Euler and Runge - Kutta method of 4th order (RK4) for this task.
* Find the distance from Earth to Sun at Apogee using Euler and RK4 method and compare it with the original.

### Given Equations

* Accn of Earth due to Gravity of the Sun 
    * $a = -\frac{GM}{|r|^3}\times\vec{r}$

* ODE for Position
    * $\frac{dr}{dt} = v$ 

* ODE for Velocity
 * $\frac{dr}{dt} = v$

### Initial Condition
* Earth is at its Perihelion (closest to Sun)

# Setup
1. `git clone <link>`
2. Update the `config.json` file 
3. Run `earth.py`


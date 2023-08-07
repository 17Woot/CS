# this is good, array for displacement and velocity vs time for a spring mass system with friction, need to animate spring using this
import numpy as np
from scipy.integrate import solve_ivp

g = 9.81 
k = 40
m = 1
b = 1

x0 = 0
x_dot0 = 0

def spring_mass_friction_ODE(t,y):
    return(y[1], g - k*y[0]/m - b*y[1]/m)

sol = solve_ivp(spring_mass_friction_ODE, [0, 5], (x0, x_dot0), 
                t_eval=np.linspace(0,5,5*30))

x, x_dot = sol.y
t = sol.t





from sympy import *
from sympy.physics.mechanics import *
init_vprinting()

# Define symbols
m, g, k, t = symbols('m g k t')
x = dynamicsymbols('x')

# take derivatives
x_dot = x.diff(t)
x_dddot = x_dot.diff(t)

# Lagrangian 

T = 1/2 * m * x_dot**2
V = -m*g*x + 1/2 * k * x**2
L = T - V

# Solve Euler-Lagrange equation
eqn = diff(diff(L, x_dot), t) - diff(L, x)
sln = solve(eqn, x_dddot)[0]
Eq(x_dddot, sln)



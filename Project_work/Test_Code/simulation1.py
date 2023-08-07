import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# initialisation
tstart = 0.0
tstop = 60.0
increment = 0.1

# initial conditions
x_init = [0,0]

t  = np.arange(tstart, tstop+1, increment)

# Function that returns dx/dt 
def mydiff(x, t):
    c = 4 # damping constant
    k = 2 # spring constant
    m = 20 # mass
    F = 5 # external force

    dx1dt = x[1]
    dx2dt = (F - c*x[1] - k*x[0])/m

    dxdt = [dx1dt, dx2dt]
    return dxdt

# solve ODE
x = odeint(mydiff, x_init, t)

x1 = x[:,0]
x2 = x[:,1]

# plot results
plt.plot(t,x1)
plt.plot(t,x2)
plt.title('Mass-Spring-Damper System')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend(['x1(t)=position','x2(t)=velocity'],loc='best')
plt.grid()
plt.show()

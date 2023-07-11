import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


k = 1
m = 1
def f(x, u, t):
    return -k/m*x

x_graph = []
t_graph = []
u_graph = []
y_graph = []

def func(x_0, u_0, t_0, h):
    for i in range(1, 1000):
        m1 = h*u_0
        k1 = h*f(x_0, u_0, t_0)
        m2 = h*(u_0 + 0.5*k1)
        k2 = h*f(x_0+0.5*m1, u_0+0.5*k1, t_0+0.5*h)
        m3 = h*(u_0 + 0.5*k2)
        k3 = h*f(x_0+0.5*m2, u_0+0.5*k2, t_0+0.5*h)
        m4 = h*(u_0 + k3)
        k4 = h*f(x_0+m3, u_0+k3, t_0+h)
        x_0 += (m1 + 2*m2 + 2*m3 + m4)/6
        u_0 += (k1 + 2*k2 + 2*k3 + k4)/6
        t_0 += h
        x_graph.append(x_0)
        t_graph.append(t_0)
        u_graph.append(u_0)
        y_graph.append(0)
    return x_0



print(func(0, 5, np.pi, 0.01))

fig, ax = plt.subplots()

ax.set(xlim=(-5.1, 5.1), ylim=(-1,1))
# ax.grid()
def animate(i):
    l1.set_data(x_graph[:i],y_graph[:i])
    sin_x = []
    sin_y = []
    for j in np.linspace(-5,x_graph[i],250):
        sin_x.append(j)
        sin_y.append(0.15*np.sin((j+5)*(2*np.pi)*10/(x_graph[i]+5)))
    l2.set_data(sin_x, sin_y)
    return l1,l2,

l1, = ax.plot([],[], 'o',markevery=[-1])
l2, = ax.plot([],[], '-')


ani = animation.FuncAnimation(fig, animate, frames=len(t_graph),interval =0.5, blit=True)
fig.show()

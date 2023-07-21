import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def hooke_law_spring_force(k, x):
    return -k * x

def update(frame):
    mass_position = amplitude * np.sin(frame * angular_frequency)
    spring_force = hooke_law_spring_force(spring_constant, mass_position)

    mass.set_ydata(mass_position)
    force_arrow.set_positions((0, mass_position), (0, mass_position - spring_force))

    return mass, force_arrow,

if __name__ == "__main__":
    spring_constant = 1.0
    mass = 1.0
    angular_frequency = 0.1
    amplitude = 2.0

    x_values = np.linspace(-amplitude - 1, amplitude + 1, 100)
    force_values = hooke_law_spring_force(spring_constant, x_values)

    fig, ax = plt.subplots()
    ax.set_xlim(-amplitude - 1, amplitude + 1)
    ax.set_ylim(-amplitude - 1, amplitude + 1)

    spring, = ax.plot([0, 0], [0, 0], lw=2, color='b')
    mass, = ax.plot(0, 0, 'ro', markersize=10)
    force_arrow = ax.arrow(0, 0, 0, 0, width=0.05, color='g', head_width=0.2, head_length=0.1)

    spring.set_xdata([0, 0])
    spring.set_ydata([amplitude, -amplitude])

    animation = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

    plt.xlabel("Displacement (x)")
    plt.ylabel("Position")
    plt.title("Hooke's Law Animation")
    plt.grid()
    plt.show()

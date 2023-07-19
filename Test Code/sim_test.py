import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class MassSpringDamper:
    def __init__(self, mass, spring_constant, damping_coefficient):
        self.mass = mass
        self.spring_constant = spring_constant
        self.damping_coefficient = damping_coefficient

        self.position = 0.0
        self.velocity = 0.0

    def update(self, force, delta_time):
        acceleration = (force - self.damping_coefficient * self.velocity - self.spring_constant * self.position) / self.mass
        self.velocity += acceleration * delta_time
        self.position += self.velocity * delta_time

# Simulation parameters
mass = 1.0         # Mass of the object (kg)
spring_constant = 10.0  # Spring constant (N/m)
damping_coefficient = 0.5  # Damping coefficient (Ns/m)
initial_position = 1.0  # Initial position of the mass (m)
initial_velocity = 0.0  # Initial velocity of the mass (m/s)

# Create the mass-spring-damper system
system = MassSpringDamper(mass, spring_constant, damping_coefficient)
system.position = initial_position
system.velocity = initial_velocity

# Set up the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position (m)')
ax.set_title('Mass-Spring-Damper System Animation')
ax.grid(True)

# Lists to store the results
positions = []
times = []

# Animation update function
def update(frame):
    global system
    force = 0.0  # You can apply external forces here if needed

    system.update(force, 0.01)
    positions.append(system.position)
    times.append(frame * 0.01)

    line.set_data(times, positions)
    return line,

# Animation initialization function
def init():
    line.set_data([], [])
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True, interval=10)

plt.show()

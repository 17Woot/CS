import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Parameters of the mass-spring-damper system
mass = 1.0  # Mass (kg)
stiffness = 10.0  # Spring constant (N/m)
damping = 0.5  # Damping coefficient (Ns/m)

# Time properties
total_time = 10.0  # Total animation time (s)
dt = 0.02  # Time step (s)
num_steps = int(total_time / dt)

# Initial conditions
initial_displacement = 1.0  # Initial displacement (m)
initial_velocity = 0.0  # Initial velocity (m/s)

# Function to calculate the acceleration (second-order ODE)
def acceleration(x, v):
    return -(stiffness * x + damping * v) / mass

# Initialize arrays to store position and velocity data
positions = np.zeros(num_steps)
velocities = np.zeros(num_steps)

# Function to update the position and velocity arrays
def update_position_velocity(step):
    if step == 0:
        positions[step] = initial_displacement
        velocities[step] = initial_velocity
    else:
        acceleration_value = acceleration(positions[step - 1], velocities[step - 1])
        velocities[step] = velocities[step - 1] + acceleration_value * dt
        positions[step] = positions[step - 1] + velocities[step] * dt

# Create the main application window
root = tk.Tk()
root.title("Mass-Spring-Damper System")

# Create a frame for the animation
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel("Displacement (m)")
ax.set_ylabel("Time (s)")
ax.set_aspect('equal')

# Create the spring line and mass point
spring_line, = ax.plot([], [], lw=1)
mass_point, = ax.plot([], [], 'bo', ms=10)

# Update function for the animation
def update(step):
    update_position_velocity(step)
    spring_line.set_data([0, positions[step]], [0, 0])
    mass_point.set_data([positions[step]], [0])
    return spring_line, mass_point

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, blit=True, interval=dt*1000)

# Create a canvas for the animation and add it to the frame
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Function to start or restart the animation
def start_animation():
    ani.event_source.start()

# Function to stop the animation
def stop_animation():
    ani.event_source.stop()

# Create start and stop buttons
start_button = tk.Button(root, text="Start", command=start_animation)
start_button.pack(side=tk.LEFT, padx=5, pady=5)
stop_button = tk.Button(root, text="Stop", command=stop_animation)
stop_button.pack(side=tk.LEFT, padx=5, pady=5)

# Start the main event loop
root.mainloop()

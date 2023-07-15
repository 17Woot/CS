import tkinter as tk
from tkinter import ttk
import pygame
from pygame.locals import *
import numpy as np
from scipy.integrate import odeint

def start_simulation():
    # Get the variable values from the entries
    c = float(c_entry.get())
    k = float(k_entry.get())
    m = float(m_entry.get())
    F = float(F_entry.get())
    
    # Close the menu window
    menu_window.destroy()
    
    # Run the simulation with the variables
    run_simulation(c, k, m, F)

def run_simulation(c, k, m, F):
    # Your simulation code here

    tstart = 0.0
    tstop = 60.0
    increment = 0.01

    # initial conditions
    x_init = [0,0]

    t  = np.arange(tstart, tstop+1, increment)

    # Function that returns dx/dt 
    def mydiff(x, t):
        c = 2 # damping constant
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

    ###########################################
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mass-Spring-Damper System Simulation")
    clock = pygame.time.Clock()
    current_time_step = 0

    scaling_factor = 100  # Adjust the scaling factor as needed

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Simulation logic
        
        # Inside the simulation logic section

        # Get the current position and velocity
        current_position = x1[current_time_step]
        current_velocity = x2[current_time_step]

        # Update the time step
        current_time_step += 1

        # Perform any necessary calculations or updates based on the current state
        # For example, you can apply user inputs, external forces, or modify the system parameters dynamically.

        # Calculate the next state of the system using the provided differential equation
        next_position, next_velocity = mydiff([current_position, current_velocity], 0)

        # Update the arrays (optional)
        x1 = np.append(x1, next_position)
        x2 = np.append(x2, next_velocity)


        # Drawing code
        # Inside the drawing code section

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the mass
        mass_radius = 20
        mass_x = int(width / 2)
        mass_y = int(height / 2) + int(current_position * scaling_factor)  # Adjust the scaling factor as needed
        pygame.draw.circle(screen, (0, 0, 255), (mass_x, mass_y), mass_radius)

        # Draw the spring (optional)
        spring_start = (mass_x, int(height / 2))
        spring_end = (mass_x, mass_y)
        spring_color = (0, 255, 0)
        spring_width = 5
        pygame.draw.line(screen, spring_color, spring_start, spring_end, spring_width)

        # Draw the damper (optional)
        # ...

        # Update the screen
        pygame.display.update()



# Create the menu window
menu_window = tk.Tk()
menu_window.title("Variable Menu")

# Create the variable entries
c_label = ttk.Label(menu_window, text="Damping Constant (c):")
c_label.pack()
c_entry = ttk.Entry(menu_window)
c_entry.pack()

k_label = ttk.Label(menu_window, text="Spring Constant (k):")
k_label.pack()
k_entry = ttk.Entry(menu_window)
k_entry.pack()

m_label = ttk.Label(menu_window, text="Mass (m):")
m_label.pack()
m_entry = ttk.Entry(menu_window)
m_entry.pack()

F_label = ttk.Label(menu_window, text="External Force (F):")
F_label.pack()
F_entry = ttk.Entry(menu_window)
F_entry.pack()

# Create the start button
start_button = ttk.Button(menu_window, text="Start", command=start_simulation)
start_button.pack()

# Run the menu window
menu_window.mainloop()

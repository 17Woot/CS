import tkinter as tk
from tkinter import ttk
import pygame
from pygame.locals import *
import numpy as np
from scipy.integrate import odeint

def start_simulation():
    # Get the variable values from the sliders
    c = c_slider.get()
    k = k_slider.get()
    m = m_slider.get()
    F = F_slider.get()
    
    # Hide the menu window
    menu_window.withdraw()
    
    # Run the simulation with the variables
    run_simulation(c, k, m, F)

def run_simulation(c, k, m, F):
    # Simulation parameters
    tstart = 0.0
    tstop = 60.0
    increment = 0.01

    # initial conditions
    x_init = [0, 0]

    t = np.arange(tstart, tstop + 1, increment)

    # Function that returns dx/dt 
    def mydiff(x, t):
        dx1dt = x[1]
        dx2dt = (F - c * x[1] - k * x[0]) / m
        dxdt = [dx1dt, dx2dt]
        return dxdt

    # solve ODE
    x = odeint(mydiff, x_init, t)

    x1 = x[:, 0]
    x2 = x[:, 1]

    ###########################################
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mass-Spring-Damper System Simulation")
    clock = pygame.time.Clock()
    current_time_step = 0

    scaling_factor = 100  # Adjust the scaling factor as needed

    # Button function to go back to the menu
    def back_to_menu():
        pygame.quit()
        menu_window.deiconify()

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
        screen.fill((36, 37, 38))  # Use the specified color for the background

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

        # Draw the button to go back to the menu
        back_button_rect = pygame.Rect(10, 10, 100, 30)
        pygame.draw.rect(screen, (255, 0, 0), back_button_rect)
        back_button_font = pygame.font.Font(None, 20)
        back_button_text = back_button_font.render("Back", True, (255, 255, 255))
        screen.blit(back_button_text, (20, 20))

        # Check if the back button is clicked
        if pygame.mouse.get_pressed()[0] and back_button_rect.collidepoint(pygame.mouse.get_pos()):
            back_to_menu()

        # Update the screen
        pygame.display.update()


# Create the menu window
menu_window = tk.Tk()
menu_window.title("Variable Menu")
menu_window.configure(background="#242526")

# Create the variable sliders
c_label = ttk.Label(menu_window, text="Damping Constant (c):", background="#242526", foreground="white")
c_label.pack()
c_slider = ttk.Scale(menu_window, from_=0, to=10, length=200, orient=tk.HORIZONTAL)
c_slider.pack()

k_label = ttk.Label(menu_window, text="Spring Constant (k):", background="#242526", foreground="white")
k_label.pack()
k_slider = ttk.Scale(menu_window, from_=0, to=10, length=200, orient=tk.HORIZONTAL)
k_slider.pack()

m_label = ttk.Label(menu_window, text="Mass (m):", background="#242526", foreground="white")
m_label.pack()
m_slider = ttk.Scale(menu_window, from_=0, to=10, length=200, orient=tk.HORIZONTAL)
m_slider.pack()

F_label = ttk.Label(menu_window, text="External Force (F):", background="#242526", foreground="white")
F_label.pack()
F_slider = ttk.Scale(menu_window, from_=0, to=10, length=200, orient=tk.HORIZONTAL)
F_slider.pack()

# Create the start button
start_button = ttk.Button(menu_window, text="Start", command=start_simulation)
start_button.pack()

# Run the menu window
menu_window.mainloop()

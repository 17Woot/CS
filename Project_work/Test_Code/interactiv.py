import pygame
from pygame.locals import *
import numpy as np
from scipy.integrate import odeint

# Pygame initialization
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mass-Spring-Damper System Simulation")
clock = pygame.time.Clock()

# Simulation parameters
tstart = 0.0
tstop = 100
increment = 0.3

# Initial conditions
x_init = [0, 0]

# Function that returns dx/dt
def mydiff(x, t):
    c = 1  # damping constant
    k = 3  # spring constant
    m = 10  # mass
    F = 5  # external force

    dx1dt = x[1]
    dx2dt = (F - c * x[1] - k * x[0]) / m

    dxdt = [dx1dt, dx2dt]
    return dxdt

# Solve ODE
t = np.arange(tstart, tstop + increment, increment)
x = odeint(mydiff, x_init, t)

x1 = x[:, 0]
x2 = x[:, 1]

# Simulation loop
current_time_step = 0
scaling_factor = 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Simulation logic
    if current_time_step < len(t):
        # Get the current position
        current_position = x1[current_time_step]

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the mass
        mass_radius = 20
        mass_x = int(width / 2)
        mass_y = int(height / 2) + int(current_position * scaling_factor)
        pygame.draw.circle(screen, (0, 0, 255), (mass_x, mass_y), mass_radius)

        # Draw the spring (optional)
        spring_start = (mass_x, int(height / 2))
        spring_end = (mass_x, mass_y)
        spring_color = (0, 255, 0)
        spring_width = 5
        pygame.draw.line(screen, spring_color, spring_start, spring_end, spring_width)

        # Update the screen
        pygame.display.update()

        current_time_step += 1

    clock.tick(60)

pygame.quit()

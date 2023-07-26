import pygame
import numpy as np
from scipy.integrate import solve_ivp

# System parameters
g = 9.81 
k = 40
m = 5
b = 0.8

x0 = 0
x_dot0 = 0

def spring_mass_friction_ODE(t, y):
    return y[1], g - k * y[0] / m - b * y[1] / m

sol = solve_ivp(spring_mass_friction_ODE, [0, 10], (x0, x_dot0), 
                t_eval=np.linspace(0, 10, 1000))

x, x_dot = sol.y
t = sol.t

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spring-Mass Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Spring and mass parameters
spring_length = 200
mass_radius = 20

# Main animation loop
clock = pygame.time.Clock()

running = True
i = 0
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000.0  # Convert to seconds

    if elapsed_time >= 10:
        running = False  # End the simulation after 10 seconds

    screen.fill(WHITE)

    # Calculate interpolation factor
    total_time = t[-1]  # Last time point
    interpolation_factor = elapsed_time / total_time

    # Interpolate mass position
    i = int(interpolation_factor * len(t))  # Update i based on the interpolation factor
    i = min(i, len(t) - 1)  # Limit i to the last index of the array
    y = spring_length + x[i] * 50  # Scale for visualization

    # Draw spring
    spring_start = (width // 2, 0)
    spring_end = (width // 2, y)
    pygame.draw.line(screen, BLACK, spring_start, spring_end, 5)

    # Draw mass
    mass_pos = (width // 2, y + mass_radius)
    pygame.draw.circle(screen, BLACK, mass_pos, mass_radius)

    pygame.display.flip()

    clock.tick(60)  # Set the desired frame rate

pygame.quit()

import pygame
import sys

# Pygame initialization
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mass Damper System")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Mass settings
mass_radius = 20
mass_color = blue
mass_start_x = screen_width // 2
mass_start_y = 100
mass_position = [mass_start_x, mass_start_y]
mass_velocity = [0, 0]  # Initial velocity of the mass

# Spring settings
spring_width = 5
spring_color = black
spring_length = 200
spring_constant = 0.1  # Spring constant

# Damping settings
damping_factor = 0.98  # Damping factor

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(white)

    # Update mass position and velocity due to spring and gravity
    gravity = 0.5  # Gravity constant
    spring_displacement = mass_position[1] - mass_start_y  # Calculate the displacement from the equilibrium position
    spring_force = -spring_constant * spring_displacement
    gravity_force = mass_radius * gravity
    mass_acceleration = (spring_force - gravity_force) / mass_radius
    mass_velocity[1] += mass_acceleration
    mass_velocity[1] *= damping_factor
    mass_position[1] += mass_velocity[1]

    # Draw spring
    spring_top = (mass_start_x, mass_start_y)
    spring_bottom = (mass_start_x, mass_position[1] + mass_radius)
    pygame.draw.line(screen, spring_color, spring_top, spring_bottom, spring_width)

    # Draw mass
    pygame.draw.circle(screen, mass_color, (int(mass_position[0]), int(mass_position[1])), mass_radius)

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

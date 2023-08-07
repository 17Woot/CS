import pygame
import numpy as np
from scipy.integrate import solve_ivp

class Simulation:
    def __init__(self, gravity=9.81, spring_constant=40, mass=1, friction=1):
        # System parameters
        self.g = gravity
        self.k = spring_constant
        self.m = mass
        self.b = friction

        # Initial conditions
        self.x0 = 0
        self.x_dot0 = 0

        # Set up Pygame
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Spring-Mass Animation")
        self.clock = pygame.time.Clock()
        self.running = True
        self.spring_length = 200
        self.mass_radius = 20
        self.start_time = pygame.time.get_ticks()
        self.velocity_timer = 0  # Timer to track how long velocity remains close to zero
        self.velocity_threshold = 0.01  # Define a threshold close to zero for the velocity

        sol = solve_ivp(self.spring_mass_friction_ODE, [0, 100], (self.x0, self.x_dot0),
                        t_eval=np.linspace(0, 100, 1000))

        self.x, self.x_dot = sol.y
        self.t = sol.t

    def spring_mass_friction_ODE(self, t, y):
        return y[1], self.g - self.k * y[0] / self.m - self.b * y[1] / self.m

    def interpolate_mass_position(self, elapsed_time):
        total_time = self.t[-1]  # Last time point
        interpolation_factor = elapsed_time / total_time
        i = int(interpolation_factor * len(self.t))  # Update i based on the interpolation factor
        i = min(i, len(self.t) - 1)  # Limit i to the last index of the array
        y = self.spring_length + self.x[i] * 50  # Scale for visualization
        return y

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Calculate elapsed time
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self.start_time) / 1000.0  # Convert to seconds

            self.screen.fill((255, 255, 255))

            # Interpolate mass position
            y = self.interpolate_mass_position(elapsed_time)

            # Draw spring
            spring_start = (self.width // 2, 0)
            spring_end = (self.width // 2, y)
            pygame.draw.line(self.screen, (0, 0, 0), spring_start, spring_end, 5)

            # Draw mass
            mass_pos = (self.width // 2, y + self.mass_radius)
            pygame.draw.circle(self.screen, (0, 0, 0), mass_pos, self.mass_radius)

            # Check if velocity is close to zero and update the timer
            if abs(self.x_dot[-1]) < self.velocity_threshold:
                self.velocity_timer += self.clock.get_time() / 1000.0
            else:
                self.velocity_timer = 0  # Reset the timer if velocity is not close to zero

            # If velocity remains close to zero for 2 seconds, end the simulation
            if self.velocity_timer >= 2:
                self.running = False

            pygame.display.flip()

            self.clock.tick(60)  # Set the desired frame rate

        pygame.quit()

if __name__ == "__main__":
    gravity = 9.81
    spring_constant = 20
    mass = 2
    friction = 0.8

    sim = Simulation(gravity=gravity, spring_constant=spring_constant, mass=mass, friction=friction)
    sim.run()

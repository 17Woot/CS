import pygame
from pygame.locals import *
import numpy as np
from scipy.integrate import odeint

class CLS_Simulation():
    def __init__(self, c, k, m, f):
        # Simulation parameters
        self.tstart = 0.0
        self.tstop = 10
        self.increment = 0.2

        # Initial conditions
        self.x_init = [0, 0]

        # Simulation variables
        self.x1 = None # position
        self.x2 = None # velocity
        self.current_time_step = 0
        self.c = c
        self.k = k
        self.m = m
        self.f = f
        

        # Pygame initialization
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mass-Spring-Damper System Simulation")
        self.clock = pygame.time.Clock()

        self.scaling_factor = 100


    def mydiff(self, x, t):
        c = self.c
        k = self.k
        m = self.m
        F = self.f

        dx1dt = x[1]
        dx2dt = (F - c * x[1] - k * x[0]) / m

        dxdt = [dx1dt, dx2dt]
        return dxdt

    def run(self):
        # Solve ODE
        t = np.arange(self.tstart, self.tstop + 1, self.increment)
        x = odeint(self.mydiff, self.x_init, t)  # Pass the arguments

        self.x1 = x[:, 0]
        self.x2 = x[:, 1]

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.simulation_logic()
            self.draw()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def simulation_logic(self):
        if self.current_time_step < len(self.x1):
            current_position = self.x1[self.current_time_step]
            current_velocity = self.x2[self.current_time_step]

            self.current_time_step += 1

            next_position, next_velocity = self.mydiff([current_position, current_velocity], 0)

            self.x1 = np.append(self.x1, next_position)
            self.x2 = np.append(self.x2, next_velocity)
        

    def draw(self):
        self.screen.fill((255, 255, 255))

        mass_radius = 20
        mass_x = int(self.width / 2)
        mass_y = int(self.height / 2) + int(self.x1[self.current_time_step] * self.scaling_factor)
        pygame.draw.circle(self.screen, (0, 0, 255), (mass_x, mass_y), mass_radius)

        spring_start = (mass_x, int(self.height / 2))
        spring_end = (mass_x, mass_y)
        spring_color = (0, 255, 0)
        spring_width = 5
        pygame.draw.line(self.screen, spring_color, spring_start, spring_end, spring_width)

    


# Create an instance of the MassSpringDamperSimulation class
if __name__ == "__main__":
    sim = CLS_Simulation(0.5, 1, 10, 1)
    sim.run()

import pygame
from pygame.locals import *
import numpy as np
from scipy.integrate import odeint
import tkinter as tk
from tkinter import ttk

class CLS_Simulation:
    def __init__(self):
        self.tstart = 0.0
        self.tstop = 100
        self.increment = 0.03

        self.x_init = [0, 0]
        self.x1 = None
        self.x2 = None
        self.current_time_step = 0

        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mass-Spring-Damper System Simulation")
        self.clock = pygame.time.Clock()

        self.scaling_factor = 100

    def mydiff(self, x, t):
        c = self.c_slider.get()
        k = self.k_slider.get()
        m = self.m_slider.get()
        F = self.F_slider.get()

        dx1dt = x[1]
        dx2dt = (F - c * x[1] - k * x[0]) / m

        dxdt = [dx1dt, dx2dt]
        return dxdt

    def set_variables(self, c, k, m, F):
        self.c_slider.set(c)
        self.k_slider.set(k)
        self.m_slider.set(m)
        self.F_slider.set(F)

    def run_simulation(self):
        t = np.arange(self.tstart, self.tstop + 1, self.increment)
        x = odeint(self.mydiff, self.x_init, t)

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
            self.clock.tick(120)

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

class MenuWindow(tk.Tk):
    def __init__(self, simulation):
        super().__init__()
        self.title("Simulation Variables")

        self.simulation = simulation

        self.c_slider = self.create_slider("Damping Constant (c):", 0, 10)
        self.k_slider = self.create_slider("Spring Constant (k):", 0, 10)
        self.m_slider = self.create_slider("Mass (m):", 0, 10)
        self.F_slider = self.create_slider("External Force (F):", 0, 10)

        self.start_button = ttk.Button(self, text="Start", command=self.start_simulation)
        self.start_button.pack()

    def create_slider(self, label_text, from_, to):
        label = ttk.Label(self, text=label_text)
        label.pack()

        slider = ttk.Scale(self, from_=from_, to=to, length=200, orient=tk.HORIZONTAL)
        slider.pack()

        return slider

    def start_simulation(self):
        self.withdraw()
        self.simulation.run_simulation()

simulation = CLS_Simulation()
menu_window = MenuWindow(simulation)
menu_window.mainloop()

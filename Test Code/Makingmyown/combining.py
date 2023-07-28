import customtkinter as ctk
import tkinter as tk
import multiprocessing
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

        sol = solve_ivp(self.spring_mass_friction_ODE, [0, 10], (self.x0, self.x_dot0),
                        t_eval=np.linspace(0, 10, 1000))

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

            if elapsed_time >= 10:
                self.running = False  # End the simulation after 10 seconds

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

            pygame.display.flip()

            self.clock.tick(60)  # Set the desired frame rate

        pygame.quit()


class CLS_Var_window(): # This class is used to create a window for the variables
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Variables")
        self.root.geometry("550x375")
        self.root.resizable(False, False)

        self.c_val = tk.DoubleVar()

        self.c_slider = ctk.CTkSlider(self.root, from_=0, to=1,  variable = self.c_val)
        self.c_slider.grid(row=0, column=1)
        self.c_slider.configure(number_of_steps=10)

        self.c_label = ctk.CTkLabel(self.root, text="Damping Constant")
        self.c_label.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.c_label.grid(row=0, column=0)

        self.c_value = ctk.CTkLabel(self.root, textvariable= self.c_val)
        self.c_value.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.c_value.grid(row=0, column=2)

        self.k_val = tk.IntVar()

        self.k_slider = ctk.CTkSlider(self.root, from_=0, to=10, variable = self.k_val)
        self.k_slider.grid(row=1, column=1)
        self.k_slider.configure(number_of_steps=10)

        self.k_label = ctk.CTkLabel(self.root, text="Spring Constant")
        self.k_label.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.k_label.grid(row=1, column=0)

        self.k_value = ctk.CTkLabel(self.root, textvariable= self.k_val)
        self.k_value.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.k_value.grid(row=1, column=2)

        self.m_val = tk.IntVar()

        self.m_slider = ctk.CTkSlider(self.root, from_=0, to=10, variable = self.m_val)
        self.m_slider.grid(row=2, column=1)
        self.m_slider.configure(number_of_steps=10)

        self.m_label = ctk.CTkLabel(self.root, text="Mass")
        self.m_label.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.m_label.grid(row=2, column=0)

        self.m_value = ctk.CTkLabel(self.root, textvariable= self.m_val)
        self.m_value.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.m_value.grid(row=2, column=2)

        self.g_val = tk.IntVar()

        self.g_slider = ctk.CTkSlider(self.root, from_=0, to=15, variable = self.g_val)
        self.g_slider.grid(row=3, column=1)
        self.g_slider.configure(number_of_steps=10)

        self.g_label = ctk.CTkLabel(self.root, text="Gravity")
        self.g_label.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.g_label.grid(row=3, column=0)

        self.g_value = ctk.CTkLabel(self.root, textvariable= self.g_val)
        self.g_value.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.g_value.grid(row=3, column=2)



        self.btn_start = ctk.CTkButton(self.root, text="Start", command=lambda: self.mt_run())
        self.btn_start.configure(font=ctk.CTkFont(size=20))
        self.btn_start.grid(row=4, column=0)

        self.btn_reset = ctk.CTkButton(self.root, text="Reset", command=lambda: self.mt_reset())
        self.btn_reset.configure(font=ctk.CTkFont(size=20))
        self.btn_reset.grid(row=4, column=1)

        self.btn_quit = ctk.CTkButton(self.root, text="Quit", command=lambda: self.mt_quit())
        self.btn_quit.configure(font=ctk.CTkFont(size=20))
        self.btn_quit.grid(row=4, column=2)

        self.c_slider.set(0.5)
        self.k_slider.set(4)
        self.m_slider.set(2)
        self.g_slider.set(9.81)



        self.root.mainloop()

    def mt_run(self):
        gravity = self.g_slider.get()
        spring_constant = self.k_slider.get()
        mass = self.m_slider.get()
        friction = self.c_slider.get()

        # Create a new process for running the simulation
        simulation_process = multiprocessing.Process(target=self.run_simulation, args=(gravity, spring_constant, mass, friction))
        simulation_process.start()

    def run_simulation(self, gravity, spring_constant, mass, friction):
        sim = Simulation(gravity=gravity, spring_constant=spring_constant, mass=mass, friction=friction)

        # Initialize Pygame inside the process
        pygame.init()

        # Run the simulation
        sim.run()

        # When the simulation is finished, return to the main variable menu
        pygame.quit()
        self.root.deiconify()
        self.root.focus_set()
    
    def mt_reset(self):
        self.c_slider.set(0)
        self.k_slider.set(0)
        self.m_slider.set(0)
        self.g_slider.set(0)

    def mt_quit(self):
        self.root.destroy()

if __name__ == "__main__":
    OBJ = CLS_Var_window()
    OBJ.root.mainloop()
        

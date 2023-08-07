import pygame 
import numpy as np
from scipy.integrate import solve_ivp
from pygame_widgets.slider import Slider 

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

        
        @property
        def gravity(self):
            return self.gravity

        @gravity.setter
        def gravity(self, value):
            self.gravity = value

        @property
        def spring_constant(self):
            return self.k

        @spring_constant.setter
        def spring_constant(self, value):
            self.k = value

        @property
        def mass(self):
            return self.m

        @mass.setter
        def mass(self, value):
            self.m = value

        @property
        def friction(self):
            return self.b

        @friction.setter
        def friction(self, value):
            self.b = value

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
    
    def create_sliders(self):
        slider_x = 100
        slider_width = 300
        slider_y_increment = 30

        # Gravity Slider
        self.gravity_slider = Slider(self.screen, slider_x, 50, slider_width, 20, min=0, max=20, step=0.1)
        self.gravity_slider.getValue = lambda: self.g  # Set initial value

        # Spring Constant Slider
        self.spring_const_slider = Slider(self.screen, slider_x, 50 + slider_y_increment, slider_width, 20,
                                          min=0, max=100, step=1)
        self.spring_const_slider.getValue = lambda: self.k  # Set initial value

        # Mass Slider
        self.mass_slider = Slider(self.screen, slider_x, 50 + 2 * slider_y_increment, slider_width, 20,
                                  min=0, max=10, step=0.1)
        self.mass_slider.getValue = lambda: self.m  # Set initial value

        # Friction Slider
        self.friction_slider = Slider(self.screen, slider_x, 50 + 3 * slider_y_increment, slider_width, 20,
                                      min=0, max=1, step=0.01)
        self.friction_slider.getValue = lambda: self.b  # Set initial value

    def update_parameters(self):
        self.g = self.gravity_slider.getValue()
        self.k = self.spring_const_slider.getValue()
        self.m = self.mass_slider.getValue()
        self.b = self.friction_slider.getValue()

    def spring_mass_friction_ODE(self, t, y):
        return y[1], self.g - self.k * y[0] / self.m - self.b * y[1] / self.m

    def interpolate_mass_position(self, elapsed_time):
        total_time = self.t[-1]  # Last time point
        interpolation_factor = elapsed_time / total_time
        i = int(interpolation_factor * len(self.t))  # Update i based on the interpolation factor
        i = min(i, len(self.t) - 1)  # Limit i to the last index of the array
        y = self.spring_length + self.x[i] * 50  # Scale for visualization
        return y
    
    def draw_slider(self, x, y, width, height, value, min_val, max_val, label):
        pygame.draw.rect(self.screen, (200, 200, 200), (x, y, width, height))
        slider_width = int((value - min_val) / (max_val - min_val) * (width - 4))
        pygame.draw.rect(self.screen, (100, 100, 100), (x + 2, y + 2, slider_width, height - 4))
        font = pygame.font.Font(None, 24)
        text = font.render(f"{label}: {value:.2f}", True, (0, 0, 0))
        self.screen.blit(text, (x, y + height + 5))

    def run(self):
        self.create_sliders()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update_parameters()
            self.draw_slider(50, 50, 200, 20, self.g, 0, 20, "Gravity")
            self.draw_slider(50, 80, 200, 20, self.k, 0, 100, "Spring Constant")
            self.draw_slider(50, 110, 200, 20, self.m, 0, 10, "Mass")
            self.draw_slider(50, 140, 200, 20, self.b, 0, 1, "Friction")

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

if __name__ == "__main__":
    gravity = 9.81
    spring_constant = 15
    mass = 5
    friction = 0.5

    sim = Simulation(gravity=gravity, spring_constant=spring_constant, mass=mass, friction=friction)
    sim.run()

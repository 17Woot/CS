from project_var_men import *
from project_simulation import * 

class CLS_SimulationController():
    def __init__(self):
        self.running = False

    def start_simulation(self, c, k, m, f):
        if not self.running:
            self.running = True
            self.sim = CLS_Simulation(c, k, m, f)
            self.sim.run()
            self.running = False

if __name__ == "__main__":
    controller = CLS_SimulationController()
    var_window = CLS_Var_window()

    while True:
        if var_window.simulation_requested:
            var_window.simulation_requested = False
            controller.start_simulation(var_window.c, var_window.k, var_window.m, var_window.f)
        var_window.root.update()
   


        
    

    

    


        




            
            

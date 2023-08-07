import customtkinter as ctk
import tkinter as tk
from project_simulation import CLS_Simulation


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
        self.root.destroy()
        gravity = self.g_slider.get()
        spring_constant = self.k_slider.get()
        mass = self.m_slider.get()
        friction = self.c_slider.get()
        Sim_object = CLS_Simulation(gravity, spring_constant, mass, friction)
        Sim_object.run()
        


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

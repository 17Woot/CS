import customtkinter as ctk
import tkinter as tk

class CLS_Var_window(): # This class is used to create a window for the variables
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Variables")
        self.root.geometry("450x300")
        self.root.resizable(False, False)

        self.c_val = tk.IntVar()

        self.c_slider = ctk.CTkSlider(self.root, from_=0, to=10, variable = self.c_val)
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

        self.f_val = tk.IntVar()

        self.f_slider = ctk.CTkSlider(self.root, from_=0, to=10, variable = self.f_val)
        self.f_slider.grid(row=3, column=1)
        self.f_slider.configure(number_of_steps=10)

        self.f_label = ctk.CTkLabel(self.root, text="Force")
        self.f_label.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.f_label.grid(row=3, column=0)

        self.f_value = ctk.CTkLabel(self.root, textvariable= self.f_val)
        self.f_value.configure(font=ctk.CTkFont(size=20), padx=10, pady=10)
        self.f_value.grid(row=3, column=2)



        self.btn_start = ctk.CTkButton(self.root, text="Start", command=lambda: self.mt_run)
        self.btn_start.configure(font=ctk.CTkFont(size=20))
        self.btn_start.grid(row=4, column=0)

        self.root.mainloop()   

    def mt_run(self):
        self.c = self.c_val.get()
        self.k = self.k_val.get()
        self.m = self.m_val.get()
        self.f = self.f_val.get()

        

        


         

        


if __name__ == "__main__":
    OBJ = CLS_Var_window()

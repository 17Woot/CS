from tkinter import *
from tkinter import messagebox
from project_db import CLS_db
from project_validation import CLS_Validator
from project_simulation import CLS_Simulation
import customtkinter as ctk

# main menu for normal users
class CLS_Menu():
    def __init__(self):
        self.validator = CLS_Validator()
        self.db = CLS_db()
        self.root = ctk.CTk()
        self.root.title("Spring.io")
        self.root.geometry("750x400")
        self.root.resizable(False, False)
        self.dark = "#242526"
        self.root.config(bg=self.dark)


        self.title_frame = Frame(self.root, bg=self.dark)
        self.title_frame.pack(padx=10, pady=(40, 20))

        self.frame1 = Frame(self.root, bg=self.dark)
        self.frame1.pack(padx=10, pady=(0, 20))

        self.title_label = Label(self.title_frame, text="Spring.io", font=ctk.CTkFont(size=40, weight="bold"))
        self.title_label.pack(padx=10, pady=(20, 20))
        self.title_label.configure(bg=self.dark, fg="white")

        self.btn_start = Button(self.frame1, width=20, text="Start", font=ctk.CTkFont(size=20), command=lambda: self.mt_start_pressed())
        self.btn_start.pack(padx=10, pady=(10, 10))

        self.btn_exit = Button(self.frame1, width=20, text="Exit", font=ctk.CTkFont(size=20), command=self.root.destroy)
        self.btn_exit.pack(padx=10, pady=(10, 10))

        self.root.mainloop()

    def mt_start_pressed(self):
        self.root.destroy()
        OBJ_Sim = CLS_Simulation()
        OBJ_Sim.start()
        












if __name__ == "__main__":
    CLS_Menu()





from tkinter import *
from tkinter import messagebox
from project_db import CLS_db
from project_validation import CLS_Validator

# main menu for normal users
class CLS_Menu():
    def __init__(self, parent):
        super().__init__(parent)
        self.validator = CLS_Validator()
        self.db = CLS_db()
        self.root = Tk()
        self.root.title("Admin Menu")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(background="light grey")

        self.frame1 = Frame(self.root, bg="light grey")


        self.root.mainloop()





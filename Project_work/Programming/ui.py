################################################
# name: Reece Wootley                          #
# date: 04/05/2023                             #
# ui for menu                                  #
################################################

from log_in import *
from myvalidation import *
from database import *
from tkinter import *
from Themesfile import *

class Ui(object): # create ui object
    def __init__(self):
        self.validator = Validator()
        self.log_in = LogIn()
        self.database = Database()

        self.root = Tk()  # create root
        self.root.title("Main Menu")  # set title
        self.root.geometry("500x500")  # set size
        self.root.resizable(False, False)  # make not resizable
        self.root.configure(background="white")  # set background colour

        self.username_label = Label(self.root, text="Username:", bg="white", font=t1.font)
        self.username_label.grid(row=1, column=1, padx=10, pady=10)

        self.username_entry = Entry(self.root, width=20, font=t1.font)
        self.username_entry.grid(row=1, column=2, padx=10, pady=10)

        self.password_label = Label(self.root, text="Password:", bg="white", font=t1.font)
        self.password_label.grid(row=2, column=1, padx=10, pady=10)

        self.password_entry = Entry(self.root, width=20, show="*", font=t1.font)
        self.password_entry.grid(row=2, column=2, padx=10, pady=10)

        self.log_in_button = Button(self.root, width=10, text="Log In", command=self.log_in_button_pressed, font=t1.font)
        self.log_in_button.grid(row=3, column=1, padx=10, pady=10)

        self.clear_button = Button(self.root, width=10, text="Clear", command=self.clear_button_pressed, font=t1.font)
        self.clear_button.grid(row=3, column=2, padx=10, pady=10)

        self.exit_button = Button(self.root, width=10, text="Exit", command=self.root.destroy, font=t1.font)
        self.exit_button.grid(row=3, column=3, padx=10, pady=10)

        self.root.mainloop()  # run root




    def log_in_button_pressed(self):
        l = LogIn()


    def clear_button_pressed(self):
        pass



if __name__ == "__main__":
    # create gui object
    t1 = Themes("arial", 12, "black", "white")
    win = Ui()



################################################
# name: Reece Wootley                          #
# date: 04/05/2023                             #
# all gui processes happen in this module      #
# created before using database                #
################################################

from tkinter import *
from tkinter import messagebox

from Programming.Old_versions.log_in0 import *
from Programming.myvalidation import *
from Programming.myencryption import *

class Gui(object): # create gui object
    def __init__(self):
        self.validator = Validator()
        self.encryption = Encryption()
        self.log_in = LogIn()
        self.root = Tk()
        self.root.title("Log In")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(background="light grey")

        # create widgets

        # place username label and entry box in middle of screen
        self.username_label = Label(self.root, text="Username:", bg="white")
        self.username_label.grid(row=1, column=1, padx=10, pady=10)


        self.username_entry = Entry(self.root, width=20)

        self.username_entry.grid(row=1, column=1, padx=10, pady=10)


        self.password_label = Label(self.root, text="Password:", bg="white")
        self.password_label.grid(row=1, column=1, padx=10, pady=10)


        self.password_entry = Entry(self.root, width=20, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)


        self.log_in_button = Button(self.root, width=10, text="Log In", command=self.log_in_button_pressed)
        self.log_in_button.grid(row=1, column=4, padx=10, pady=10)


        self.clear_button = Button(self.root, width=10, text="Clear", command=self.clear_button_pressed)
        self.clear_button.grid(row=1, column=2, padx=10, pady=10)

        self.exit_button = Button(self.root,width=10, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=1, column=1, padx=10, pady=10)

        print(self.root.grid_size())
        self.root.mainloop()

    def log_in_button_pressed(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.log_in.log_in(username, password): # if log in is successful show error box
            messagebox.showinfo("Success", "Log in successful")
        else:
            messagebox.showerror("Error", "Incorrect username or password")
            return False

    def clear_button_pressed(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def exit_button_pressed(self):
        self.root.destroy()



if __name__ == "__main__":
    # create gui object
    win = Gui()






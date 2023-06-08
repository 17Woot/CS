################################################
# name: Reece Wootley                          #
# date: 08/06/023                              #
# main menu module                             #
################################################
from tkinter import *
from tkinter import messagebox
from myvalidation import Validator
from database import Db

class Main_menu():
    def __init__(self):
        self.validator = Validator()
        self.database = Db()

        self.root = Tk()  # create root
        self.root.title("Main menu")  # set title
        self.root.geometry("500x500")  # set size
        self.root.resizable(False, False)  # make not resizable
        self.root.configure(background="white")  # set background colour
        self.root.mainloop()



if __name__ == "__main__":
    win = Main_menu()
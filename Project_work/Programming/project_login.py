from project_validation import CLS_Validator
from project_db import CLS_db
from tkinter import *
from tkinter import messagebox
from project_admin import CLS_AdminMenu
from project_menu import CLS_Menu




class CLS_LogIn():  # create log in object
    def __init__(self,):
        self.validator = CLS_Validator()
        self.db = CLS_db()
        self.root = Tk()
        self.root.title("Log In")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(background="light grey")

        # create widgets in a frame 

        # place username label and entry box in middle of screen
        self.frame = Frame(self.root, bg="light grey")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.topframe = Frame(self.frame, bg="light grey")
        self.topframe.place(in_=self.frame, anchor="n", relx=.5, rely=.5)

        self.mainframe = Frame(self.frame, bg="light grey")
        self.mainframe.place(in_=self.frame, anchor="center", relx=.5, rely=.5)

        # topframe widgets

        self.text = Text(self.topframe, bg="light grey")
        self.text.place(in_=self.topframe, anchor="center", relx=.5, rely=.5)
        self.t = Label(self.text, text="Log In", font=("Arial", 20), bg="light grey")

        # mainframe widgets
        self.username_label = Label(self.mainframe, text="Username:", bg="white")
        self.username_label.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = Label(self.mainframe, text="Password:", bg="white")
        self.password_label.grid(row=2, column=1, padx=10, pady=10)

        self.username_entry = Entry(self.mainframe, width=20)
        self.username_entry.grid(row=1, column=2, padx=10, pady=10)

        self.password_entry = Entry(self.mainframe, width=20, show="*")
        self.password_entry.grid(row=2, column=2, padx=10, pady=10)

        self.btn_login = Button(self.mainframe, width=10, text="Log In", command=lambda: self.mt_login_pressed())
        self.btn_login.grid(row=3, column=1, padx=10, pady=10)

        self.btn_clear = Button(self.mainframe, width=10, text="Clear", command=lambda: self.mt_clear_button_pressed())
        self.btn_clear.grid(row=3, column=2, padx=10, pady=10)

        self.btn_exit = Button(self.mainframe, width=10, text="Exit", command=self.root.destroy)
        self.btn_exit.grid(row=3, column=3, padx=10, pady=10)

        self.root.mainloop()

    def mt_login(self):
        try:
            user = self.username_entry.get()
            password = self.password_entry.get()
            if self.validator.mt_is_valid_length_range(user, 5, 20) and self.validator.mt_is_valid_length_range(password, 5, 20): # if username and password are valid
                if self.db.mt_user_exists(user):
                    if self.db.mt_password_correct(user, password):
                        if self.db.mt_isadmin(user):
                            return 1
                        else:
                            return 2
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except:
            return False


    def mt_login_pressed(self):
        try:
            if self.mt_login():
                if self.mt_login() == 1:
                    messagebox.showinfo("Log In", "You have successfully logged in as an admin")
                    self.root.destroy()
                elif self.mt_login() == 2:
                    messagebox.showinfo("Log In", "You have successfully logged in as a user")
                    OBJ_admin = CLS_AdminMenu()
                else:
                    messagebox.showinfo("Log In", " 1.0 Incorrect username or password")
                    OBJ_menu = CLS_Menu()

            else:
                messagebox.showinfo("Log In", "1.1Incorrect username or password")
        except:
            return False





    def mt_clear_button_pressed(self):
        try:
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
        except:
            return False
            

    def mt_exit_button_pressed(self):
        try:
            self.root.destroy()
        except:
            return False

if __name__ == '__main__':
    OBJ_login = CLS_LogIn()



        




        



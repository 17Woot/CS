from project_validation import CLS_Validator
from project_db import CLS_db
from tkinter import *
from tkinter import messagebox
from project_admin import CLS_AdminMenu
from project_menu import CLS_Menu
import customtkinter as ctk




class CLS_LogIn():  # create log in object
    def __init__(self,):
        self.validator = CLS_Validator()
        self.db = CLS_db()
        self.root = ctk.CTk()
        self.root.title("Log In")
        self.root.geometry("750x550")
        self.root.resizable(False, False)
        self.dark = "#242526"
        self.root.config(bg=self.dark)

        # create frames in a root
        self.title_frame = Frame(self.root, bg=self.dark)
        self.title_frame.pack(padx=10, pady=(40, 20))

        self.frame1 = Frame(self.root, bg=self.dark)
        self.frame1.pack(padx=10, pady=(0, 20))


        # create widgets in frames

        self.title_label = Label(self.title_frame, text="Spring.io", font=ctk.CTkFont(size=40, weight="bold"))
        self.title_label.pack(padx=10, pady=(20, 20))
        self.title_label.configure(bg=self.dark, fg="white")



        self.username = StringVar()
        self.username_label = Label(self.frame1, text="Username", font=ctk.CTkFont(size=20)).pack(padx=10, pady=(10, 10))
        self.username_entry = Entry(self.frame1, textvariable=self.username, font=ctk.CTkFont(size=20)).pack(padx=10, pady=(10, 10))

        self.password = StringVar()
        self.password_label = Label(self.frame1, text="Password", font=ctk.CTkFont(size=20)).pack(padx=10,pady=(10, 10))
        self.password_entry = Entry(self.frame1, textvariable=self.password, font=ctk.CTkFont(size=20)).pack(padx=10,pady=(10, 10))

        self.btn_login = Button(self.frame1, width=10, text="Log In", font=ctk.CTkFont(size=20), command=lambda: self.mt_login_pressed())
        #self.btn_login.configure(bg="white", fg="black",)
        self.btn_login.pack(padx=10, pady=(10, 10))

        self.btn_clear = Button(self.frame1, width=10, text="Clear", font=ctk.CTkFont(size=20), command=lambda: self.mt_clear_button_pressed())
        self.btn_clear.pack(padx=10, pady=(10, 10))

        self.btn_exit = Button(self.frame1, width=10, text="Exit", font=ctk.CTkFont(size=20), command=self.root.destroy)
        self.btn_exit.pack(padx=10, pady=(10, 10))

        self.root.mainloop()

    def mt_login(self):
        try:
            user = self.username
            password = self.password
            if self.validator.mt_is_valid_length_range(user, 5, 20) and self.validator.mt_is_valid_length_range(
                    password, 5, 20):  # if username and password are valid
                if self.db.mt_user_exists(user):
                    if self.db.mt_password_correct(user, password):
                        if self.db.mt_isadmin(user):
                            return 1
                        else:
                            return 2
                    else:
                        messagebox.showinfo("Log In", "3.0")
                        return False
                else:
                    messagebox.showinfo("Log In", "3.1")
                    return False
            else:
                messagebox.showinfo("Log In", "3.2")
                return False
        except:
            return False

    def mt_login_pressed(self):
        try:
            if self.mt_login():
                if self.mt_login() == 1:
                    messagebox.showinfo("Log In", "You have successfully logged in as an admin")
                    self.root.destroy()
                    OBJ_admin = CLS_AdminMenu()
                elif self.mt_login() == 2:
                    messagebox.showinfo("Log In", "You have successfully logged in as a user")
                    self.root.destroy()
                    OBJ_menu = CLS_Menu()

                else:
                    messagebox.showinfo("Log In", " 1.0 Incorrect username or password")


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



        




        



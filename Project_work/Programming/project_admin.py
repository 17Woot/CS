# admin menu class
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from project_db import CLS_db
from project_validation import CLS_Validator
import customtkinter as ctk

class CLS_AdminMenu():
    def __init__(self):
        self.validator = CLS_Validator()
        self.db = CLS_db()
        self.root = ctk.CTk()
        self.root.title("Admin Menu")
        self.root.geometry("450x350")
        self.root.resizable(False, False)
        self.dark = "#242526"
        self.root.config(bg=self.dark)

        # create frames in a root
        self.title_frame = Frame(self.root, bg=self.dark)
        self.title_frame.pack(padx=10, pady=(40, 20))

        self.frame1 = Frame(self.root, bg=self.dark)
        self.frame1.pack(padx=10, pady=(0, 20))

        # create widgets in frames

        self.title_label = Label(self.title_frame, text="Admin Menu", font=ctk.CTkFont(size=40, weight="bold"))
        self.title_label.pack(padx=10, pady=(20, 20))
        self.title_label.configure(bg=self.dark, fg="white")

        self.username_label = Label(self.frame1, text="Username:", bg="white")
        self.username_label.grid(row=1, column=1, padx=10, pady=(20, 10))

        self.password_label = Label(self.frame1, text="Password:", bg="white")
        self.password_label.grid(row=2, column=1, padx=10, pady=(10, 10))

        self.username_entry = Entry(self.frame1, width=20)
        self.username_entry.grid(row=1, column=2, padx=10, pady=(20, 10))

        self.password_entry = Entry(self.frame1, width=20, show="*")
        self.password_entry.grid(row=2, column=2, padx=10, pady=(10, 10))

        self.btn_register = Button(self.frame1, width=10, text="Register", command=lambda: self.mt_register_pressed())
        self.btn_register.grid(row=3, column=1, padx=10, pady=10)

        self.btn_clear = Button(self.frame1, width=10, text="Clear", command=lambda: self.mt_clear_button_pressed())
        self.btn_clear.grid(row=3, column=2, padx=10, pady=10)

        self.btn_exit = Button(self.frame1, width=10, text="Exit", command=self.root.destroy)
        self.btn_exit.grid(row=3, column=3, padx=10, pady=10)

        self.btn_delete = Button(self.frame1, width=10, text="Delete", command=lambda: self.mt_delete_pressed())
        self.btn_delete.grid(row=4, column=2, padx=10, pady=10)

        self.root.mainloop()


    def mt_delete_pressed(self):
        try:
            user = self.username_entry.get()
            if self.validator.mt_is_valid_length_range(user, 5, 20):
                if askyesno("Delete", "Are you sure you want to delete this user?"):
                    if self.mt_delete(user):
                        messagebox.showinfo("Success", "User deleted")
                    else:
                        messagebox.showinfo("Error", "2.1 User not deleted")
                else:
                    messagebox.showinfo("Error", "2.2 User not deleted")
            else:
                messagebox.showinfo("Error", "2.3 User not deleted")
        except:
            messagebox.showinfo("Error", "2.4 User not deleted")




    def mt_delete(self, user):
        try:
            if self.db.mt_delete_user(user):
                return True
            else:
                return False
        except:
            return False




    def mt_register(self, user, password):
        try:
            if self.db.mt_add_user(user, password):
                return True
            else:
                return False
        except:
            return False

    def mt_register_pressed(self):
        try:
            user = self.username_entry.get()
            password = self.password_entry.get()
            if self.validator.mt_is_valid_length_range(user, 5, 20) and self.validator.mt_is_valid_length_range(password, 5, 20): # if username and password are valid
                if self.mt_register(user, password):
                    messagebox.showinfo("Success", " 1.0 User registered")
                else:
                    messagebox.showinfo("Error", " 1.1 User not registered")
            else:
                messagebox.showinfo("Error", "1.2 User not registered")
        except:
            messagebox.showinfo("Error", "1.3 User not registered")

    def mt_clear_button_pressed(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

if __name__ == "__main__":
    CLS_AdminMenu()
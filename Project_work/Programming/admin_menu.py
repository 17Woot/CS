from tkinter import *
from tkinter import messagebox
from myvalidation import Validator
from database import Db
from Themesfile import *

class Admin_menu():
    def __init__(self):
        self.validator = Validator()
        self.database = Db()

        self.root = Tk()  # create root
        self.root.title("Admin Menu")  # set title
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

        self.register_button = Button(self.root, width=10, text="Register", command=self.register_button_pressed, font=t1.font)
        self.register_button.grid(row=3, column=1, padx=10, pady=10)

        self.clear_button = Button(self.root, width=10, text="Clear", command=self.clear_button_pressed, font=t1.font)
        self.clear_button.grid(row=3, column=2, padx=10, pady=10)

        self.exit_button = Button(self.root, width=10, text="Exit", command=self.root.destroy, font=t1.font)
        self.exit_button.grid(row=3, column=3, padx=10, pady=10)

        self.root.mainloop()  # run root

    def register_button_pressed(self):
        try:
            self.register(self.username_entry.get(), self.password_entry.get())
        except:
            messagebox.showerror("Error", "Something went wrong")

    def register(self, user, password, admin_status = False):
        try:
            if self.validator.is_valid_length_range(user, 5, 20) and self.validator.is_valid_length_range(password, 5,20):
                if self.database.add_user(user, password):
                    messagebox.showinfo("Success", "User added successfully")
                else:
                    messagebox.showerror("Error", "User already exists")
            else:
                messagebox.showerror("Error", "Username or password is invalid")
        except:
            messagebox.showerror("Error", "Something went wrong")

    def clear_button_pressed(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)


if __name__ == "__main__":
    a = Admin_menu()







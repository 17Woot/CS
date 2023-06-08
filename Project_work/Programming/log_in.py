################################################
# name: Reece Wootley                          #
# date: 12/05/2023                             #
# log in module                                #
################################################


from myvalidation import *
from database import *
from tkinter import *
from Themesfile import *
from tkinter import messagebox

class log_in_ui(object): # create ui object
    def __init__(self):
        self.validator = Validator()
        self.database = Db()

        self.root = Tk()  # create root
        self.root.title("Log in")  # set title
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
        try:
            user = self.username_entry.get()
            password = self.password_entry.get()
            if self.validator.is_valid_length_range(user, 5, 20) and self.validator.is_valid_length_range(password, 5, 20):
                if self.database.user_exists(user):
                    if self.database.password_correct(user, password):
                        if self.database.admin_status(user) == True:
                            messagebox.showinfo("Success", "Welcome Admin")
                            self.root.destroy()
                        else:
                            messagebox.showinfo("Success", "Welcome")
                            self.root.destroy()

                    else:
                        messagebox.showerror("Error 1.1", "Incorrect password")
                else:
                    messagebox.showerror("Error 1.2", "User does not exist")
            else:
                messagebox.showerror("Error 1.3", "Username and password must be between 5 and 20 characters")
        except Exception as e:
            messagebox.showerror("Error 1.4", e)




    def clear_button_pressed(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)



if __name__ == "__main__":
    # create gui object
    t1 = Themes("arial", 12, "black", "white")
    win = log_in_ui()








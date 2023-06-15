from project_validation import CLS_Validator
from project_db import CLS_db
from tkinter import *
from tkinter import messagebox

class CLS_LogIn(object):  # create log in object
    def __init__(self):
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
        self.frame.grid(row=1, column=1, padx=10, pady=10)

        self.username_label = Label(self.frame, text="Username:", bg="white")
        self.username_label.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = Label(self.frame, text="Password:", bg="white")
        self.password_label.grid(row=2, column=1, padx=10, pady=10)

        self.username_entry = Entry(self.frame, width=20)
        self.username_entry.grid(row=1, column=2, padx=10, pady=10)

        self.password_entry = Entry(self.frame, width=20, show="*")
        self.password_entry.grid(row=2, column=2, padx=10, pady=10)

        self.btn_login = Button(self.frame, width=10, text="Log In", command=self.log_in_button_pressed)
        self.btn_login.grid(row=3, column=1, padx=10, pady=10)

        self.btn_clear = Button(self.frame, width=10, text="Clear", command=self.clear_button_pressed)
        self.btn_clear.grid(row=3, column=2, padx=10, pady=10)

        self.btn_exit = Button(self.frame, width=10, text="Exit", command=self.root.destroy)
        self.btn_exit.grid(row=3, column=3, padx=10, pady=10)

        self.root.mainloop()

        def mt_login(self):
            try:
                user = self.username_entry.get()
                password = self.password_entry.get()
                if self.validator.mt_is_valid_length_range(user, 5, 20) and self.validator.mt_is_valid_length_range(password, 5, 20): # if username and password are valid
                    if user == "admin" and password == "admin":
                        return True
                    elif user == "user" and password == "user":
                        return True
                    else:
                        return False
                else:
                    return False
            except:
                return False
                    


        def mt_login_pressed(self):
            try:
                if self.mt_login():
                    messagebox.showinfo("Log In", "You have successfully logged in")
                else:
                    messagebox.showinfo("Log In", "You have entered an invalid username or password")
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
    win = CLS_LogIn()


        




        



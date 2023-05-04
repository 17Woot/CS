################################################
# name: Reece Wootley                          #
# date: 04/05/2023                             #
# log in module                                #
################################################

from Programming.myvalidation import Validator
from Programming.mydatabase import User_Database
from Programming.myencryption import Encryption
from
class LogIn(object):  # create log in object
    def __init__(self):
        self.validator = Validator()
        self.database = Database()
        self.encryption = Encryption()
        self.user = User()
        self.admin = Admin()

    def log_in(self, username, password): # log in function
        if self.validator.is_valid_length_range(username, 6, 20) and self.validator.is_valid_length_range(password, 8, 20): # if username and password are valid
            if self.database.is_user(username): # if user exists
                if self.database.is_password(username, self.encryption.encrypt(password)): # if password is correct
                    if self.database.is_admin(username): # if user is admin
                        self.admin.admin_menu(username) # go to admin menu
                    else:
                        self.user.user_menu(username)
                else:
                    print("Incorrect password")
            else:
                print("User does not exist")
        else:
            print("Invalid username or password")

    def create_account(self, username, password, email): # create account function
        if self.validator.is_valid_length_range(username, 6, 20) and self.validator.is_valid_length_range(password, 8, 20) and self.validator.is_valid_email(email): # if username, password and email are valid
            if not self.database.is_user(username): # if user does not exist
                self.database.create_user(username, self.encryption.encrypt(password), email) # create user
                print("Account created")
            else:
                print("User already exists")
        else:
            print("Invalid username, password or email")

    def delete_account(self, username, password): # delete account function
        if self.validator.is_valid_length_range(username, 6, 20) and self.validator.is_valid_length_range(password, 8, 20): # if username and password are valid
            if self.database.is_user(username): # if user exists
                if self.database.is_password(username, self.encryption.encrypt(password)): # if password is correct
                    self.database.delete_user(username) # delete user
                    print("Account deleted")
                else:
                    print("Incorrect password")

            else:
                print("User does not exist")
        else:
            print("Invalid username or password")

    def change_password(self, username, old_password, new_password): # change password function
        if self.validator.is_valid_length_range(username, 6, 20) and self.validator.is_valid_length_range(old_password, 8, 20) and self.validator.is_valid_length_range(new_password, 1, 20): # if username, old password and new password are valid
            if self.database.is_user(username): # if user exists
                if self.database.is_password(username, self.encryption.encrypt(old_password)): # if old password is correct
                    self.database.change_password(username, self.encryption.encrypt(new_password)) # change password
                    print("Password changed")
                else:
                    print("Incorrect password")
            else:
                print("User does not exist")
        else:
            print("Invalid username, old password or new password")





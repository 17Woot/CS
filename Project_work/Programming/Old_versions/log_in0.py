####################################################
# name: Reece Wootley                              #
# date: 04/05/2023                                 #
# log in module without using database for testing #
####################################################

from Project_work.Programming.myvalidation import Validator
from Project_work.Programming.myencryption import Encryption


class LogIn(object):  # create log in object
    def __init__(self):
        self.validator = Validator()
        self.encryption = Encryption()

    def log_in(self, username, password): # log in function
            if self.validator.is_valid_length_range(username, 5, 20) and self.validator.is_valid_length_range(password, 8, 20): # if username and password are valid
                if username == "admin123" and password == "password": # if username and password are correct
                    return True
                elif username == "user123" and password == "password": # if username and password are correct
                    return True
                else:
                    return False
            else:
                return False




################################################
# name: Reece Wootley                          #
# date: 12/05/2023                             #
# log in module                                #
################################################
from myvalidation import Validator
from database import log_in_db


class LogIn(object):
    def __init__(self):
        self.validator = Validator()
        self.database = log_in_db()

    def log_in(self, username, password):
        if self.validator.is_valid_length_range(username, 5, 20) and self.validator.is_valid_length_range(password, 8, 20):
            if self.database.searchUser(username, password):
                return True
            else:
                return False
        else:
            return False
        
    def add_user(self, username, password):
        if self.validator.is_valid_length_range(username, 5, 20) and self.validator.is_valid_length_range(password, 8, 20):
            if self.database.add_user(username, password):
                return True
            else:
                return False
        else:
            return False
        

       

    



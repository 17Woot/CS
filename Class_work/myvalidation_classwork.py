################################################
# name: Reece Wootley                          #
# date: 04/05/2023                             #
# validation module to crate a validator object#
################################################

import re
class Validator(object):  # create validator object
    def __init__(self):
        pass

    def isValid_length(self,text, length): # is length valid using try except
        try:
            if len(text) == length:
                return True
            else:
                return False
        except:
            return False



    def is_valid_length_range(self,text, min_length, max_length): # is length in range using try except
        try:
            if len(text) >= min_length and len(text) <= max_length:
                return True
            else:
                return False
        except:
            return False

    def is_valid_email(self,email): # is email valid using try except
        try:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return True
            else:
                return False
        except:
            return False  # if email is not valid return false

    def is_string(self,text): # is string valid using try except
        try:
            if isinstance(text, str):
                return True
            else:
                return False
        except:
            return False



    def is_number(self,text): # is number valid using try except
        try:
            if isinstance(text, int):
                return True
            else:
                return False
        except:
            return False

    def is_valid_date(self,text):
        try:
            if re.match(r"^\d{1,2}/\d{1,2}/\d{4}$", text):
                return True
            else:
                return "nope"
        except:
            return "nope"



if __name__ == '__main__':
    pass




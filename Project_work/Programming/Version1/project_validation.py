import re


class CLS_Validator(object):  # create validator object
    def __init__(self):
        pass

    def mt_isValid_length(self, text, length):  # is length valid using try except
        try:
            if len(text) == length:
                return True
            else:
                return False
        except:
            return False

    def mt_is_valid_length_range(self, text, min_length, max_length):  # is length in range using try except
        try:
            text = str(text)
            if min_length <= len(text) <= max_length:
                return True
            else:
                return False
        except:
            return False

    def mt_is_valid_email(self, email):  # is email valid using try except
        pass

    def mt_is_string(self, text):  # is string valid using try except
        try:
            if isinstance(text, str):
                return True
            else:
                return False
        except:
            return False

    def mt_is_number(self, text):  # is number valid using try except
        try:
            if isinstance(text, int):
                return True
            else:
                return False
        except:
            return False


if __name__ == '__main__':
    pass

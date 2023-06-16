################################################
# name: Reece Wootley                          #
# date: 04/05/2023                             #
# data encryption module                       #
################################################

import hashlib
class Encryption(object):  # create encryption object
    def __init__(self):
        pass

    def encrypt_text(self, text): # encrypt text using sha256
        return hashlib.sha256(text.encode()).hexdigest()

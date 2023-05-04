################################################
# name: Reece Wootley                          #
# date: 04/05/2023                             #
# unittest for validation module               #
################################################


import unittest
from myvalidation import Validator
from unittest import TestCase

class TestValidator(TestCase):
    def setUp(self):
        self.validator = Validator()
        self.text = "hello"
        self.length = 5
        self.min_length = 3
        self.max_length = 7
        self.email = "reece@gmail.com"
        self.number = 5

    def test_is_valid_length(self):
        result = self.validator.isValid_length(self.text, self.length)
        self.assertTrue(result)

    def test_is_valid_length_range(self):
        result = self.validator.is_valid_length_range(self.text, self.min_length, self.max_length)
        self.assertTrue(result)

    def test_is_valid_email(self):
        result = self.validator.is_valid_email(self.email)
        self.assertTrue(result)

    def test_is_string(self):
        result = self.validator.is_string(self.text)
        self.assertTrue(result)

    def test_is_number(self):
        result = self.validator.is_number(self.number)
        self.assertTrue(result)

    def tearDown(self):
        del self.validator
        del self.text
        del self.length
        del self.min_length
        del self.max_length
        del self.email
        del self.number

if __name__ == '__main__':
    unittest.main()





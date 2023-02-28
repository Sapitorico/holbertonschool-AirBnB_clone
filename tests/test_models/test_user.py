#!/usr/bin/python3
""" unittest for class User"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ tests """
    def test_user(self):
        """ test """
        my_user = User()
        self.assertIsInstance(my_user, User)
        self.assertIsInstance(my_user, BaseModel)
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")


if __name__ == '__main__':
    unittest.main()

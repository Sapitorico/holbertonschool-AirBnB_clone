#!/usr/bin/python3
""" unittest from class State """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ State tets """
    def test_state(self):
        """ test """
        my_state = State()
        self.assertIsInstance(my_state, State)
        self.assertIsInstance(my_state, BaseModel)
        self.assertTrue(hasattr(my_state, "name"))
        self.assertEqual(my_state.name, "")


if __name__ == '__main__':
    unittest.main()
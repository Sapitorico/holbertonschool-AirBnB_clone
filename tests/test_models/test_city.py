#!/usr/bin/python3
""" unittest for  City """
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ City tests """
    def test_city(self):
        """ test """
        my_city = City()
        self.assertIsInstance(my_city, City)
        self.assertIsInstance(my_city, BaseModel)
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertTrue(hasattr(my_city, "name"))
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")


if __name__ == '__main__':
    unittest.main()

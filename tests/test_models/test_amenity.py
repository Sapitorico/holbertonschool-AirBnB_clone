#!/usr/bin/python3
""" unittest from class Amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ tests """
    def test_Amenity(self):
        """ test """
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
        self.assertIsInstance(my_amenity, BaseModel)
        self.assertTrue(hasattr(my_amenity, "name"))
        self.assertEqual(my_amenity.name, "")


if __name__ == '__main__':
    unittest.main()

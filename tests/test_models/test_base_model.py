#!/usr/bin/python3
""" unittest from parent class BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ field to tests """
    def test_type_of_instances(self):
        """ test type of instances """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()

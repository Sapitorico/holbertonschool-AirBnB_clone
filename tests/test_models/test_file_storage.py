#!/usr/bin/python3
""" unittest from parent class fileStorage """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import os.path
import json


class TestFileStorage(unittest.TestCase):
    """ field to tests from FileStorage """
    def test_attributes(self):
        """ test attributes """
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)
        self.assertIsInstance(my_model._FileStorage__file_path, str)
        self.assertIsInstance(my_model._FileStorage__objects, dict)

    def test_all(self):
        """ test all """
        my_model = FileStorage()
        self.assertIsInstance(my_model.all(), dict)

    def test_new(self):
        """ test new """
        my_model = FileStorage()
        my_model.new(BaseModel())
        self.assertIsInstance(my_model._FileStorage__objects, dict)

    def test_save(self):
        """ test save """
        my_model = FileStorage()
        my_model.new(BaseModel())
        my_model.save()
        self.assertIsInstance(my_model._FileStorage__objects, dict)
        self.assertTrue(os.path.exists(my_model._FileStorage__file_path))

    def test_reload(self):
        """ test reload """
        my_model = FileStorage()
        my_model.new(BaseModel())
        my_model.save()
        my_model.reload()
        self.assertIsInstance(my_model._FileStorage__objects, dict)
        self.assertTrue(os.path.exists(my_model._FileStorage__file_path))


if __name__ == '__main__':
    unittest.main()

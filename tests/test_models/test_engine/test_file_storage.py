#!/usr/bin/python3
""" unittest from parent class fileStorage """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test environment"""
        if os.path.isfile(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new method"""
        model = BaseModel()
        self.storage.new(model)
        self.assertEqual(self.storage.all(), {'BaseModel.' + model.id: model})

    def test_save(self):
        """Test the save method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.isfile(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test the reload method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertIn('BaseModel.' + model.id, self.storage.all())


if __name__ == '__main__':
    unittest.main()

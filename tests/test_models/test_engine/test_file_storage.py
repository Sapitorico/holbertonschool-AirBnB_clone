#!/usr/bin/python3
""" unittest from parent class fileStorage """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os.path


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Set up the FileStorage instance"""
        self.storage = FileStorage()

    def tearDown(self):
        """Delete the FileStorage instance"""
        del self.storage

    def test_all(self):
        """Test the all method"""
        self.assertEqual(len(self.storage.all()), 0)
        model1 = BaseModel()
        model2 = BaseModel()
        self.storage.new(model1)
        self.storage.new(model2)
        self.assertEqual(len(self.storage.all()), 2)

    def test_new(self):
        """Test the new method"""
        self.assertEqual(len(self.storage.all()), 0)
        model = BaseModel()
        self.storage.new(model)
        self.assertEqual(len(self.storage.all()), 1)

    def test_save(self):
        """Test the save method"""
        from models import storage
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))
        model = BaseModel()
        storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_reload(self):
        """Test the reload method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        self.assertNotEqual(len(self.storage.all()), 0)


if __name__ == '__main__':
    unittest.main()

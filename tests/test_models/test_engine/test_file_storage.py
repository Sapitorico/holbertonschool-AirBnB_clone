#!/usr/bin/python3
""" unittest from parent class fileStorage """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage """

    def setUp(self):
        """ Setup test """
        self.file_storage = FileStorage()

    def tearDown(self):
        """ Delete file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes(self):
        """ Test __objects, __file_path """
        self.assertEqual(type(self.file_storage._FileStorage__objects), dict)
        self.assertEqual(type(self.file_storage._FileStorage__file_path), str)

    def test_all(self):
        """ Test all method """
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        """ Test new method """
        my_model = BaseModel()
        self.assertEqual(len(self.file_storage.all()), 1)
        self.assertIn("BaseModel." + my_model.id, self.file_storage.all())

    def test_save(self):
        """ Test save method """
        my_model = BaseModel()
        self.file_storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + my_model.id, f.read())

    def test_reload(self):
        """ Test reload method """
        my_model = BaseModel()
        self.file_storage.save()
        objects = self.file_storage.all()
        self.assertEqual(len(objects), 2)
        for key in objects.keys():
            self.assertTrue(isinstance(objects[key], BaseModel))

    def test_reload_2(self):
        """ Test reload method """
        my_model = BaseModel()
        self.file_storage.new(my_model)
        self.file_storage.save()
        with open(self.file_storage._FileStorage__file_path, "r") as f:
            data = json.load(f)
        data["BaseModel.1234"] = {"id": "1234", "__class__": "BaseModel", "name": "test"}
        with open(self.file_storage._FileStorage__file_path, "w") as f:
            json.dump(data, f)
        self.file_storage.reload()
        self.assertIn("BaseModel.1234", self.file_storage.all())
        obj = self.file_storage.all()["BaseModel.1234"]
        self.assertEqual(obj.id, "1234")
        self.assertEqual(obj.name, "test")

    def test_file_path(self):
        """ Test __file_path attribute """
        self.assertEqual(self.file_storage._FileStorage__file_path, "file.json")



if __name__ == '__main__':
    unittest.main()

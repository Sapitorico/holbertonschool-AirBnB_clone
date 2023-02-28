#!/usr/bin/python3
""" unittest from parent class BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ field to tests """
    def test_type_of_instances(self):
        """ test instances """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """ test str """
        my_model = BaseModel()
        string = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(string, str(my_model))
        self.assertIsInstance(string, str)
        self.assertIsInstance(my_model, BaseModel)

    def test_save(self):
        """ test save """
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model, BaseModel)
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_save_2(self):
        from models import storage
        obj = BaseModel()
        obj.name = "test"
        obj.save()
        obj2 = storage.all()["BaseModel." + obj.id]
        self.assertEqual(obj2.name, "test")

    def test_to_dict(self):
        """ test to_dict """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        my_model.name = "sapito"
        my_model.my_number = 21
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["name"], "sapito")
        self.assertEqual(my_model_dict["my_number"], 21)
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual
        (my_model_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual
        (my_model_dict["updated_at"], my_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()

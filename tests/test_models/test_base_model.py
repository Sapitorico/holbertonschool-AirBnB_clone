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

    def test_id(self):
        """ test id """
        my_model = BaseModel()
        my_model1 = BaseModel()
        self.assertNotEqual(my_model.id, my_model1.id)

    def test_created_at(self):
        """ test created_at """
        my_model = BaseModel()
        my_model1 = BaseModel()
        self.assertNotEqual(my_model.created_at, my_model1.created_at)

    def test_updated_at(self):
        """ test updated_at """
        my_model = BaseModel()
        my_model1 = BaseModel()
        self.assertNotEqual(my_model.updated_at, my_model1.updated_at)

    def test_str(self):
        """ test str """
        my_model = BaseModel()
        my_model.name = "sapito"
        my_model.my_number = 21
        string = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(string, str(my_model))

    def test_to_dict(self):
        """ test to_dict """
        my_model = BaseModel()
        my_model.name = "sapito"
        my_model.my_number = 21
        my_model.save()
        new_dict = my_model.to_dict()
        self.assertEqual(new_dict['__class__'], 'BaseModel')
        self.assertEqual(type(new_dict['created_at']), str)
        self.assertEqual(type(new_dict['updated_at']), str)

    def test_kwargs(self):
        """ test kwargs """
        my_model = BaseModel()
        my_model.name = "sapito"
        my_model.my_number = 89
        my_model.save()
        new_dict = my_model.to_dict()
        my_model1 = BaseModel(**new_dict)
        self.assertNotEqual(my_model, my_model1)
        self.assertEqual(my_model.id, my_model1.id)
        self.assertEqual(my_model.created_at, my_model1.created_at)
        self.assertEqual(my_model.updated_at, my_model1.updated_at)
        self.assertEqual(my_model.name, my_model1.name)
        self.assertEqual(my_model.my_number, my_model1.my_number)

    def test_save(self):
        """ test save """
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
""" unittest from parent class BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        string = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), string)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(
            datetime.strptime(model_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f'),
            datetime)
        self.assertIsInstance(
            datetime.strptime(model_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'),
            datetime)

    def test_kwargs_instantiation(self):
        kwargs = {'id': '123', 'created_at': '2022-02-28T15:00:00.000000', 'updated_at': '2022-02-28T15:00:00.000000', 'name': 'test'}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, '123')
        self.assertEqual(
            model.created_at,
            datetime.strptime('2022-02-28T15:00:00.000000', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(
            model.updated_at,
            datetime.strptime('2022-02-28T15:00:00.000000', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(model.name, 'test')

    def test_save(self):
        """ Test save method """
        my_model = BaseModel()
        my_model.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + my_model.id, f.read())


if __name__ == '__main__':
    unittest.main()

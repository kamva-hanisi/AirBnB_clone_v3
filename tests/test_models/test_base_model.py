#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model_instance = BaseModel()

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_instance_creation(self):
        self.assertIsNotNone(self.base_model_instance.id)
        self.assertIsInstance(self.base_model_instance.created_at, datetime)
        self.assertIsInstance(self.base_model_instance.updated_at, datetime)

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model_instance.id, self.base_model_instance.__dict__)
        self.assertEqual(str(self.base_model_instance), expected_str)

    def test_save_method(self):
        initial_updated_at = self.base_model_instance.updated_at
        self.base_model_instance.save()
        self.assertNotEqual(initial_updated_at,
                            self.base_model_instance.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.base_model_instance.id,
            '__class__': 'BaseModel',
            'created_at': self.base_model_instance.created_at.isoformat(),
            'updated_at': self.base_model_instance.updated_at.isoformat()
        }
        self.assertEqual(self.base_model_instance.to_dict(), expected_dict)

    def test_kwargs_initialization(self):
        kwargs = {
            'id': 'test-id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'custom_attr': 'test_value'
        }
        base_model_instance = BaseModel(**kwargs)
        self.assertEqual(base_model_instance.id, kwargs['id'])
        self.assertEqual(base_model_instance.custom_attr, 'test_value')

    def test_invalid_args_initialization(self):
        with self.assertRaises(TypeError):
            BaseModel('invalid_arg')


if __name__ == '__main__':
    unittest.main()

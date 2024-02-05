#!/usr/bin/python3
"""Unit tests for the City module.
"""
import unittest
from models.city import City
from models import storage
from datetime import datetime


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city_instance = City()

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_instance_creation(self):
        self.assertIsNotNone(self.city_instance.id)
        self.assertIsInstance(self.city_instance.created_at, datetime)
        self.assertIsInstance(self.city_instance.updated_at, datetime)
        self.assertEqual(self.city_instance.state_id, "")
        self.assertEqual(self.city_instance.name, "")

    def test_str_representation(self):
        expected_str = "[City] ({}) {}".format(
            self.city_instance.id, self.city_instance.__dict__)
        self.assertEqual(str(self.city_instance), expected_str)

    def test_save_method(self):
        initial_updated_at = self.city_instance.updated_at
        self.city_instance.save()
        self.assertNotEqual(initial_updated_at,
                            self.city_instance.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.city_instance.id,
            '__class__': 'City',
            'created_at': self.city_instance.created_at.isoformat(),
            'updated_at': self.city_instance.updated_at.isoformat(),
        }
        self.assertEqual(self.city_instance.to_dict(), expected_dict)

    def test_kwargs_initialization(self):
        kwargs = {
            'id': 'test-id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'state_id': 'test-state-id',
            'name': 'Test City'
        }
        city_instance = City(**kwargs)
        self.assertEqual(city_instance.id, kwargs['id'])
        self.assertEqual(city_instance.state_id, kwargs['state_id'])
        self.assertEqual(city_instance.name, kwargs['name'])

    def test_invalid_args_initialization(self):
        with self.assertRaises(TypeError):
            City('invalid_arg')


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Defines unittests for amenity model"""
import unittest
from models.amenity import Amenity
from models import storage
from datetime import datetime


class TestAmenity(unittest.TestCase):
    amenity_name = "Test"

    def setUp(self):
        self.amenity_instance = Amenity()
        self.amenity_instance.name = TestAmenity.amenity_name

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_instance_creation(self):
        self.assertIsNotNone(self.amenity_instance.id)
        self.assertIsInstance(self.amenity_instance.created_at, datetime)
        self.assertIsInstance(self.amenity_instance.updated_at, datetime)
        self.assertEqual(self.amenity_instance.name, TestAmenity.amenity_name)

    def test_str_representation(self):
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity_instance.id, self.amenity_instance.__dict__)
        self.assertEqual(str(self.amenity_instance), expected_str)

    def test_save_method(self):
        initial_updated_at = self.amenity_instance.updated_at
        self.amenity_instance.save()
        self.assertNotEqual(initial_updated_at,
                            self.amenity_instance.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.amenity_instance.id,
            '__class__': 'Amenity',
            'created_at': self.amenity_instance.created_at.isoformat(),
            'updated_at': self.amenity_instance.updated_at.isoformat(),
            'name': self.amenity_instance.name
        }

        self.assertEqual(self.amenity_instance.to_dict(), expected_dict)

    def test_kwargs_initialization(self):
        kwargs = {
            'id': 'test-id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'Test Amenity'
        }
        amenity_instance = Amenity(**kwargs)
        self.assertEqual(amenity_instance.id, kwargs['id'])
        self.assertEqual(amenity_instance.name, kwargs['name'])

    def test_invalid_args_initialization(self):
        with self.assertRaises(TypeError):
            Amenity('invalid_arg')


if __name__ == '__main__':
    unittest.main()

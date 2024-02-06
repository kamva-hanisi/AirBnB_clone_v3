#!/usr/bin/python3
"""Unit tests for the Place module.
"""
import unittest
from models.place import Place
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place_instance = Place()

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_instance_creation(self):
        self.assertIsNotNone(self.place_instance.id)
        self.assertIsInstance(self.place_instance.created_at, datetime)
        self.assertIsInstance(self.place_instance.updated_at, datetime)
        self.assertEqual(self.place_instance.city_id, "")
        self.assertEqual(self.place_instance.user_id, "")
        self.assertEqual(self.place_instance.name, "")
        self.assertEqual(self.place_instance.description, "")
        self.assertEqual(self.place_instance.number_rooms, 0)
        self.assertEqual(self.place_instance.number_bathrooms, 0)
        self.assertEqual(self.place_instance.max_guest, 0)
        self.assertEqual(self.place_instance.price_by_night, 0)
        self.assertEqual(self.place_instance.latitude, 0.0)
        self.assertEqual(self.place_instance.longitude, 0.0)
        self.assertEqual(self.place_instance.amenity_ids, [])

    def test_str_representation(self):
        expected_str = "[Place] ({}) {}".format(
            self.place_instance.id, self.place_instance.__dict__)
        self.assertEqual(str(self.place_instance), expected_str)

    def test_save_method(self):
        initial_updated_at = self.place_instance.updated_at
        self.place_instance.save()
        self.assertNotEqual(initial_updated_at,
                            self.place_instance.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.place_instance.id,
            '__class__': 'Place',
            'created_at': self.place_instance.created_at.isoformat(),
            'updated_at': self.place_instance.updated_at.isoformat(),
        }
        self.assertEqual(self.place_instance.to_dict(), expected_dict)

    def test_kwargs_initialization(self):
        kwargs = {
            'id': 'test-id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'city_id': 'test-city-id',
            'user_id': 'test-user-id',
            'name': 'Test Place',
            'description': 'Test Description',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenity_ids': ['amenity1', 'amenity2']
        }
        place_instance = Place(**kwargs)
        self.assertEqual(place_instance.id, kwargs['id'])
        self.assertEqual(place_instance.city_id, kwargs['city_id'])
        self.assertEqual(place_instance.user_id, kwargs['user_id'])
        self.assertEqual(place_instance.name, kwargs['name'])
        self.assertEqual(place_instance.description, kwargs['description'])
        self.assertEqual(place_instance.number_rooms, kwargs['number_rooms'])
        self.assertEqual(place_instance.number_bathrooms,
                         kwargs['number_bathrooms'])
        self.assertEqual(place_instance.max_guest, kwargs['max_guest'])
        self.assertEqual(place_instance.price_by_night,
                         kwargs['price_by_night'])
        self.assertEqual(place_instance.latitude, kwargs['latitude'])
        self.assertEqual(place_instance.longitude, kwargs['longitude'])
        self.assertEqual(place_instance.amenity_ids,
                         kwargs['amenity_ids'])

    def test_invalid_args_initialization(self):
        with self.assertRaises(TypeError):
            Place('invalid_arg')


if __name__ == '__main__':
    unittest.main()

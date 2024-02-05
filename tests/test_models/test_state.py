#!/usr/bin/python3
"""Unit tests for the State module.
"""
import unittest
from models.state import State
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):

    def setUp(self):
        self.state_instance = State()

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_instance_creation(self):
        self.assertIsNotNone(self.state_instance.id)
        self.assertIsInstance(self.state_instance.created_at, datetime)
        self.assertIsInstance(self.state_instance.updated_at, datetime)
        self.assertEqual(self.state_instance.name, "")

    def test_str_representation(self):
        expected_str = "[State] ({}) {}".format(
            self.state_instance.id, self.state_instance.__dict__)
        self.assertEqual(str(self.state_instance), expected_str)

    def test_save_method(self):
        initial_updated_at = self.state_instance.updated_at
        self.state_instance.save()
        self.assertNotEqual(initial_updated_at, self.state_instance.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.state_instance.id,
            '__class__': 'State',
            'created_at': self.state_instance.created_at.isoformat(),
            'updated_at': self.state_instance.updated_at.isoformat(),
        }
        self.assertEqual(self.state_instance.to_dict(), expected_dict)

    def test_kwargs_initialization(self):
        kwargs = {
            'id': 'test-id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'Test State'
        }
        state_instance = State(**kwargs)
        self.assertEqual(state_instance.id, kwargs['id'])
        self.assertEqual(state_instance.name, kwargs['name'])

    def test_invalid_args_initialization(self):
        with self.assertRaises(TypeError):
            State('invalid_arg')


if __name__ == '__main__':
    unittest.main()

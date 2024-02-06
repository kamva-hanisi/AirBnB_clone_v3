#!/usr/bin/python3
"""Unit tests for the User module.
"""
import unittest
from models.user import User
from models import storage
from datetime import datetime


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user_instance = User()

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_instance_creation(self):
        self.assertIsNotNone(self.user_instance.id)
        self.assertIsInstance(self.user_instance.created_at, datetime)
        self.assertIsInstance(self.user_instance.updated_at, datetime)
        self.assertEqual(self.user_instance.email, "")
        self.assertEqual(self.user_instance.password, "")
        self.assertEqual(self.user_instance.first_name, "")
        self.assertEqual(self.user_instance.last_name, "")

    def test_str_representation(self):
        expected_str = "[User] ({}) {}".format(
            self.user_instance.id, self.user_instance.__dict__)
        self.assertEqual(str(self.user_instance), expected_str)

    def test_save_method(self):
        initial_updated_at = self.user_instance.updated_at
        self.user_instance.save()
        self.assertNotEqual(initial_updated_at, self.user_instance.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.user_instance.id,
            '__class__': 'User',
            'created_at': self.user_instance.created_at.isoformat(),
            'updated_at': self.user_instance.updated_at.isoformat(),
        }
        self.assertEqual(self.user_instance.to_dict(), expected_dict)

    def test_kwargs_initialization(self):
        kwargs = {
            'id': 'test-id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'email': 'test@example.com',
            'password': 'test_password',
            'first_name': 'Test',
            'last_name': 'User'
        }
        user_instance = User(**kwargs)
        self.assertEqual(user_instance.id, kwargs['id'])
        self.assertEqual(user_instance.email, kwargs['email'])
        self.assertEqual(user_instance.password, kwargs['password'])
        self.assertEqual(user_instance.first_name, kwargs['first_name'])
        self.assertEqual(user_instance.last_name, kwargs['last_name'])

    def test_invalid_args_initialization(self):
        with self.assertRaises(TypeError):
            User('invalid_arg')


if __name__ == '__main__':
    unittest.main()

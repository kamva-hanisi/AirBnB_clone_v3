#!/usr/bin/python3
"""Unit tests for the Review module.
"""
import unittest
from models.review import Review
from models import storage
from datetime import datetime


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review_instance = Review()

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_instance_creation(self):
        self.assertIsNotNone(self.review_instance.id)
        self.assertIsInstance(self.review_instance.created_at, datetime)
        self.assertIsInstance(self.review_instance.updated_at, datetime)
        self.assertEqual(self.review_instance.place_id, "")
        self.assertEqual(self.review_instance.user_id, "")
        self.assertEqual(self.review_instance.text, "")

    def test_str_representation(self):
        expected_str = "[Review] ({}) {}".format(
            self.review_instance.id, self.review_instance.__dict__)
        self.assertEqual(str(self.review_instance), expected_str)

    def test_save_method(self):
        initial_updated_at = self.review_instance.updated_at
        self.review_instance.save()
        self.assertNotEqual(initial_updated_at,
                            self.review_instance.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            'id': self.review_instance.id,
            '__class__': 'Review',
            'created_at': self.review_instance.created_at.isoformat(),
            'updated_at': self.review_instance.updated_at.isoformat(),
        }
        self.assertEqual(self.review_instance.to_dict(), expected_dict)

    def test_kwargs_initialization(self):
        kwargs = {
            'id': 'test-id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'place_id': 'test-place-id',
            'user_id': 'test-user-id',
            'text': 'Test Review Text'
        }
        review_instance = Review(**kwargs)
        self.assertEqual(review_instance.id, kwargs['id'])
        self.assertEqual(review_instance.place_id, kwargs['place_id'])
        self.assertEqual(review_instance.user_id, kwargs['user_id'])
        self.assertEqual(review_instance.text, kwargs['text'])

    def test_invalid_args_initialization(self):
        with self.assertRaises(TypeError):
            Review('invalid_arg')


if __name__ == '__main__':
    unittest.main()

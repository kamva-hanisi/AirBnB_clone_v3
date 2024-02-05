#!/usr/bin/python3
"""Defines unittests for FileStorage model"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.place import Place
from models.user import User


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_storage_instance = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method(self):
        all_objects = self.file_storage_instance.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        test_base_model = BaseModel()
        self.file_storage_instance.new(test_base_model)
        key = '{}.{}'.format(test_base_model.__class__.__name__, test_base_model.id)
        self.assertIn(key, self.file_storage_instance.all())

    def test_save_method(self):
        test_base_model = BaseModel()
        self.file_storage_instance.new(test_base_model)
        self.file_storage_instance.save()
        with open(FileStorage._FileStorage__file_path, 'r') as json_file:
            data = json.load(json_file)
            key = '{}.{}'.format(test_base_model.__class__.__name__, test_base_model.id)
            self.assertIn(key, data)

    def test_reload_method(self):
        test_base_model = BaseModel()
        self.file_storage_instance.new(test_base_model)
        self.file_storage_instance.save()

        new_file_storage_instance = FileStorage()
        new_file_storage_instance.reload()

        key = '{}.{}'.format(test_base_model.__class__.__name__, test_base_model.id)
        self.assertIn(key, new_file_storage_instance.all())

    def test_reload_method_invalid_class_name(self):
        # Test reloading with an invalid class name in the file
        invalid_data = {"InvalidClass.123": {"key": "value"}}
        with open(FileStorage._FileStorage__file_path, 'w') as json_file:
            json.dump(invalid_data, json_file)

        self.file_storage_instance.reload()
        self.assertNotEqual(self.file_storage_instance.all(), {})

    def test_reload_method_multiple_models(self):
        # Test reloading with multiple models
        user_instance = User()
        state_instance = State()
        self.file_storage_instance.new(user_instance)
        self.file_storage_instance.new(state_instance)
        self.file_storage_instance.save()

        new_file_storage_instance = FileStorage()
        new_file_storage_instance.reload()

        user_key = '{}.{}'.format(user_instance.__class__.__name__, user_instance.id)
        state_key = '{}.{}'.format(state_instance.__class__.__name__, state_instance.id)
        self.assertIn(user_key, new_file_storage_instance.all())
        self.assertIn(state_key, new_file_storage_instance.all())


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unit tests for the HBNBCommand module.
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.mock_stdout.close()

    def test_quit_command(self):
        with patch('sys.stdout', self.mock_stdout):
            self.assertTrue(self.hbnb_cmd.onecmd('quit'))
        self.assertEqual(self.mock_stdout.getvalue(), "")

    def test_create_command(self):
        with patch('sys.stdout', self.mock_stdout):
            self.hbnb_cmd.onecmd('create BaseModel')
        modelId = self.mock_stdout.getvalue().strip()
        self.assertTrue(modelId)

    def test_show_command(self):
        with patch('sys.stdout', self.mock_stdout):
            self.hbnb_cmd.onecmd('show BaseModel 1234-5678')
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_command(self):
        with patch('sys.stdout', self.mock_stdout):
            self.hbnb_cmd.onecmd('destroy BaseModel 1234-5678')
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_all_command(self):
        with patch('sys.stdout', self.mock_stdout):
            self.hbnb_cmd.onecmd('all')
        output = self.mock_stdout.getvalue().strip()
        self.assertTrue(output)

    def test_update_command(self):
        with patch('sys.stdout', self.mock_stdout):
            self.hbnb_cmd.onecmd('update BaseModel 1234-5678 name "New Name"')
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()

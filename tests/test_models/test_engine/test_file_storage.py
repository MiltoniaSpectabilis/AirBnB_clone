#!/usr/bin/python3
"""
Test cases for file_storage.py
"""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def test_file_path_attr(self):
        """Tests '__file_path' class attribute"""
        storage_instance = FileStorage()
        self.assertTrue(hasattr(storage_instance, '_FileStorage__file_path'))
        self.assertTrue(storage_instance._FileStorage__file_path, "file.json")
        self.assertIsInstance(storage_instance._FileStorage__file_path, str)

    def test_all_returns_dict(self):
        """
        Tests if the all() method returns a dictionary.
        """
        storage_instance = FileStorage()
        all_objects = storage_instance.all()
        self.assertIsInstance(all_objects, dict)

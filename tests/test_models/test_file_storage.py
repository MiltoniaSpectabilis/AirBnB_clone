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

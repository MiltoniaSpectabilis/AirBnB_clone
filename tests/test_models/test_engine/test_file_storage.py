#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""

from unittest import TestCase
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(TestCase):
    """
    Test cases for the FileStorage class methods and attributes.
    """

    def setUp(self):
        """
        Set up test environment.
        Temporarily rename the actual file.json if it exists
        to ensure a clean state for each test.
        """
        try:
            os.rename("file.json", "tmp_file.json")
        except FileNotFoundError:
            pass
        # Reset __objects before each test
        FileStorage._FileStorage__objects = {}
        # Set __file_path to the default test file name
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Tear down test environment.
        Remove the test file.json if it was created.
        Restore the actual file.json if it was renamed.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp_file.json", "file.json")
        except FileNotFoundError:
            pass
        # Ensure __objects is cleared after tests
        FileStorage._FileStorage__objects = {}

    def test_file_path_attribute(self):
        """
        Tests if __file_path attribute is set and has the correct type.
        """
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_objects_attribute(self):
        """
        Tests if __objects attribute is set and is a dictionary.
        """
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_all_method(self):
        """
        Tests the all() method to ensure it returns the __objects dictionary.
        """
        storage_instance = FileStorage()
        self.assertIsInstance(storage_instance.all(), dict)
        self.assertEqual(storage_instance.all(),
                         FileStorage._FileStorage__objects)
        self.assertIs(storage_instance.all(),
                      FileStorage._FileStorage__objects)

    def test_new_method(self):
        """
        Tests the new() method to ensure it adds an object to __objects.
        """
        storage_instance = FileStorage()
        bm = BaseModel()
        storage_instance.new(bm)
        key = f"{bm.__class__.__name__}.{bm.id}"
        self.assertIn(key, FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], bm)

    def test_save_and_reload_methods(self):
        """
        Tests the save() and reload() methods together.
        Ensures objects are correctly serialized and deserialized.
        """
        storage_instance = FileStorage()
        FileStorage._FileStorage__objects = {}

        bm1 = BaseModel()
        bm2 = BaseModel()

        storage_instance.new(bm1)
        storage_instance.new(bm2)

        storage_instance.save()

        FileStorage._FileStorage__objects = {}

        storage_instance.reload()

        self.assertGreater(len(FileStorage._FileStorage__objects), 0)
        self.assertEqual(len(FileStorage._FileStorage__objects), 2)

        for obj in FileStorage._FileStorage__objects.values():
            self.assertIsInstance(obj, BaseModel)

        key1 = f"{bm1.__class__.__name__}.{bm1.id}"
        key2 = f"{bm2.__class__.__name__}.{bm2.id}"
        self.assertIn(key1, FileStorage._FileStorage__objects)
        self.assertIn(key2, FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key1].id, bm1.id)
        self.assertEqual(FileStorage._FileStorage__objects[key2].id, bm2.id)

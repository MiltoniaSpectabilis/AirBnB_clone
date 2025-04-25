#!/usr/bin/python3
"""

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """

    """

    def test_instance_creation(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_attrs_are_assigned_on_creation(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_id_is_str(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_save(self):
        model = BaseModel()
        original_update_at = model.updated_at
        model.save()
        time.sleep(1)
        self.assertGreater(model.updated_at, original_update_at)

    def test_str_representation_of_object(self):
        model = BaseModel()
        self.assertIsInstance(str(model), str)

    def test_save_method_updates_updated_at(self):
        """
        Tests that the save() method updates the updated_at attribute.
        """
        bm = BaseModel()
        # Get the initial updated_at time
        initial_updated_at = bm.updated_at

        # Introduce a small delay to ensure the datetime changes
        time.sleep(0.01)

        # Call the save method
        bm.save()

        # Get the updated updated_at time
        updated_updated_at = bm.updated_at

        # Assert that the updated_at time has changed
        self.assertNotEqual(initial_updated_at, updated_updated_at)

        # Assert that updated_updated_at is more recent than initial_updated_at
        self.assertGreater(updated_updated_at, initial_updated_at)

        # Assert that updated_updated_at is a datetime object
        self.assertIsInstance(updated_updated_at, datetime)

    def test_to_dict_method(self):
        """
        Tests the to_dict() method to ensure it returns a dictionary
        with correct content and format.
        """
        bm = BaseModel()
        # Add a couple of custom attributes to the instance
        bm.name = "My First Model"
        bm.my_number = 89

        # Get the dictionary representation
        bm_dict = bm.to_dict()

        # 1. Test that the return type is a dictionary
        self.assertIsInstance(bm_dict, dict)

        instance_dict = bm.__dict__.copy()

        expected_keys = ['id', 'created_at', 'updated_at',
                         'name', 'my_number', '__class__']
        self.assertEqual(set(bm_dict.keys()), set(expected_keys))

        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)

        self.assertIn('__class__', bm_dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')

        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertFalse(hasattr(bm, '__class__'))

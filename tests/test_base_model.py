#!/usr/bin/python3
"""

"""
import unittest
from models.base_model import BaseModel
# from datetime import datetime
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

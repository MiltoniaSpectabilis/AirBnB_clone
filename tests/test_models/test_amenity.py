#!/usr/bin/python3
""""""
from unittest import TestCase
from models.amenity import Amenity


class TestAmenity(TestCase):
    """"""

    def test_name_attribute(self):
        """"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

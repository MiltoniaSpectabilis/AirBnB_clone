#!/usr/bin/python3
""""""
from unittest import TestCase
from models.city import City


class TestCity(TestCase):
    """"""

    def test_state_id_attribute(self):
        """"""
        city = City()
        self.assertEqual(city.state_id, "")

    def test_name_attribute(self):
        """"""
        city = City()
        self.assertEqual(city.name, "")

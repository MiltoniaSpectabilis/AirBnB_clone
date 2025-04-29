#!/usr/bin/python3
""""""

from unittest import TestCase
from models.place import Place


class TestPlace(TestCase):
    """"""

    def test_city_id_attribute(self):
        """"""
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_user_id_attribute(self):
        """"""
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_name_attribute(self):
        """"""
        place = Place()
        self.assertEqual(place.description, "")

    def test_number_rooms_attribute(self):
        """"""
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attribute(self):
        """"""
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attribute(self):
        """"""
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night(self):
        """"""
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_attribute(self):
        """"""
        place = Place()
        self.assertEqual(place.latitude, 0)

    def test_longitude_attribute(self):
        """"""
        place = Place()
        self.assertEqual(place.longitude, 0)

    def test_amenity_ids_attribute(self):
        """"""
        place = Place()
        self.assertEqual(place.amenity_ids, [])

#!/usr/bin/python3
""""""

from unittest import TestCase
from models.review import Review


class TestReview(TestCase):
    """"""

    def test_place_id_attribute(self):
        """"""
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_id_attribute(self):
        """"""
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_text_attribute(self):
        """"""
        review = Review()
        self.assertEqual(review.text, "")

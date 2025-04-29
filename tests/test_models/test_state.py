#!/usr/bin/python3
""""""

from unittest import TestCase
from models.state import State


class TestState(TestCase):
    """"""

    def test_name_attribute(self):
        """"""
        state = State()
        self.assertEqual(state.name, "")

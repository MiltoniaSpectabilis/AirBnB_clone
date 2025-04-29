#!/usr/bin/python3
""""""
from unittest import TestCase
from models.user import User


class TestUser(TestCase):
    """"""

    def test_instance_creation(self):
        """"""
        user = User()
        self.assertIsInstance(user, User)

    def test_email(self):
        """"""
        user = User()
        self.assertEqual(user.email, "")
        user.email = "jean@baudrillard.sym"
        self.assertEqual(user.email, "jean@baudrillard.sym")

    def test_password(self):
        """"""
        user = User()
        self.assertEqual(user.password, "")
        user.password = "F@tal$tr@t3gIsT"
        self.assertEqual(user.password, "F@tal$tr@t3gIsT")

    def test_first_name(self):
        """"""
        user = User()
        self.assertEqual(user.first_name, "")
        user.first_name = "jean"
        self.assertEqual(user.first_name, "jean")

    def test_last_name(self):
        """"""
        user = User()
        self.assertEqual(user.last_name, "")
        user.last_name = "baudrillard"
        self.assertEqual(user.last_name, "baudrillard")

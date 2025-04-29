#!/usr/bin/python3
"""User class representing a user of the application."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the system."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

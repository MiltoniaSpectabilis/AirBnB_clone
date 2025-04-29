#!/usr/bin/python3
"""User class representing a user of the application."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the system."""

    def __init__(self, *args, **kwargs):
        """Initializes User instance."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

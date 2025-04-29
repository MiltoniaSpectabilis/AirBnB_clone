#!/usr/bin/python3
"""User class representing a user of the application."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the system."""

    # def __init__( *args, **kwargs):
    #     """Initializes User instance."""
    #     super().__init__(*args, **kwargs)
    email = ""
    password = ""
    first_name = ""
    last_name = ""

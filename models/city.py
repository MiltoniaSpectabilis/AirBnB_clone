#!/usr/bin/python3
"""City class representing a city."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city in the system."""
    state_id = ""
    name = ""

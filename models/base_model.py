#!/usr/bin/python3
"""
Defines a base model with common attributes and methods
for other classes
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class for models, providing common attributes and methods
    for persistence
    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """
        Initializes a new BaseModel instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the 'updated_' attribute
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing object attributes
        for serialization
        """
        dic = self.__dict__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        dic['__class__'] = self.__class__.__name__
        return dic

    def __str__(self):
        """
        Returns a string representation in a specific format
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

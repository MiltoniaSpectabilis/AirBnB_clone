#!/usr/bin/python3
"""
Defines a base model with common attributes and methods
for other classes
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for models, providing common attributes and methods
    for persistence
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at':
                    setattr(self, k, datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == 'updated_at':
                    setattr(self, k, datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the 'updated_' attribute
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing object attributes
        for serialization
        """
        dic = self.__dict__.copy()
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        dic['__class__'] = self.__class__.__name__
        return dic

    def __str__(self):
        """
        Returns a string representation in a specific format
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

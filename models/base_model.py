#!/usr/bin/python3
"""
Defines a base model for objects in the project,
handling initialization, serialization, and deserialization.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class for all models in the project.

    Handles initialization with unique ID and timestamps,
    updating timestamps, and converting to a dictionary
    representation for serialization.
    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """
        Initializes a new BaseModel instance.

        Args:
            id (uuid, optional): Unique ID for the instance.
                                Defaults to a new UUID4.
            created_at (datetime, optional): Datetime of creation.
                                            Defaults to the current datetime.
            updated_at (datetime, optional): Datetime of last update.
                                            Defaults to the current datetime.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Includes all instance attributes from __dict__,
        converts datetime objects to ISO format strings,
        and adds the '__class__' key with the class name.
        """
        dic = self.__dict__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        dic['__class__'] = self.__class__.__name__
        return dic

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Format: [<class name>] (<id>) <instance attributes dictionary>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

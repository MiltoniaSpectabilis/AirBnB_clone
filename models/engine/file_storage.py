#!/usr/bin/python3
"""
FileStorage class for object serialization and deserialization.
"""

import json


class FileStorage:
    """
    Manages serialization and deserialization of objects to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        dic = {}
        for k, v in FileStorage.__objects.items():
            dic[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dic, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if file exists.
        """
        dic = {}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dic = json.load(f)

            # Move import here to break circularity
            from models.base_model import BaseModel
            from models.user import User
            # Define the mapping of class names to class objects here
            classes = {
                "BaseModel": BaseModel,
                "User": User,
            }

            for k, v in dic.items():
                cls_name = v['__class__']
                cls = classes.get(cls_name)
                obj_instance = cls(**v)
                FileStorage.__objects[k] = obj_instance
        except FileNotFoundError:
            pass

#!/usr/bin/python3
"""
    class FileStorage which takes care of
    save the data of each created instance
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ field storage class """
    """
    __file_path: stores the path to the JSON file
        that will be used to store the instance data.
    __objects: dictionary containing all the instances
        created and their corresponding key.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the representation of a json _object as a dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ add an object to the dictionary """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes the objects to a JSON file """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """ deserialize the JSON file to objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj

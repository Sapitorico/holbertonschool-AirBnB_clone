#!/usr/bin/python3
"""
class FileStorage que se encarga de
guardar los datos de cada instancia creada
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ field storage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns la representacion de un lso objetos como diccionario """
        return FileStorage.__objects

    def new(self, obj):
        """ agrega un objeto al diccionario """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializa los objetos a un archivo JSON """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """ deserializa el archivo JSON a objetos """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj

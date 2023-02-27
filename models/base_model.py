#!/usr/bin/python3
"""
    parent Class BaseModel:
        that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """ field to class """

    def __init__(self):
        """
        instances:
        id: identificador unico
        creates_at: fecha y hora exacta en la que se creo
        updated_at: fecha y hora exacta en la que se actualizo
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ representacion de la instancia en formato string """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ actualiza el atributo updated_at con la fecha y hora actual """
        self.updated_at = datetime.now()

    def to_dict(self):
        """retorna un diccionario con todas las key y value de la instancia"""
        new_dict = self.__dict__.copy()
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                new_dict[key] = value.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

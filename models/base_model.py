#!/usr/bin/python3
"""
    parent Class BaseModel:
        that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
        base class to be used in a system object storage and retrieval.
    """

    def __init__(self, *args, **kwargs):
        """
        constructor
            instances:
            id: unique identifier
            creates_at: exact date and time when it was created
            updated_at: exact date and time it was updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] =\
                        datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """ representation of the instance in string format """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the updated_at attribute with the current date and time"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """returns a dictionary with all the keys and values ​​of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                new_dict[key] = value.isoformat()
        return new_dict

#!/usr/bin/python3
"""Module base_model"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    t_format = '%Y-%m-%dT%H:%M:%S.%f'
                    self.__dict__[k] = datetime.strptime(v, t_format)
                elif k != '__class__':
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict method"""
        dic_copy = self.__dict__.copy()
        dic_copy['__class__'] = self.__class__.__name__
        dic_copy['created_at'] = self.created_at.isoformat()
        dic_copy['updated_at'] = self.updated_at.isoformat()
        return dic_copy

#!/usr/bin/python3
"""Module state"""
from datetime import datetime
from models.base_model import BaseModel
import models


class State(BaseModel):
    """Class for state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
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

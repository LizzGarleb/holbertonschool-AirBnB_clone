#!/usr/bin/python3
"""
Module review
"""
from datetime import datetime
from base_model import BaseModel
import models


class Review(BaseModel):
    """
    Class for review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor\n"""
        super().__init__(*args, **kwargs)
        models.storage.new(self)

    def __str__(self):
        """str method\n"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save method\n"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict method\n"""
        dic_copy = self.__dict__.copy()
        dic_copy['__class__'] = self.__class__.__name__
        dic_copy['created_at'] = self.created_at.isoformat()
        dic_copy['updated_at'] = self.updated_at.isoformat()
        return dic_copy

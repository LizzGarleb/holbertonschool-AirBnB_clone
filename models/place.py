#!/usr/bin/python3
"""
Module place
"""
from datetime import datetime
from base_model import BaseModel
import models


class Place(BaseModel):
    """
    Class for place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity = []

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

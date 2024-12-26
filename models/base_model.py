#!/usr/bin/python3
"""
Contains the BaseModel class
"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """The BaseModel class"""
    
    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.id = value

        if storage is None:
            storage.new(self) = self

    def __str__(self):
        """Return a string representation of the BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        self.storage = storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel class"""
        dict_representation =self.__dict__.copy()
        dict_representation["__class__"] = self.__class__.__name__
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()
        return dict_representation
    

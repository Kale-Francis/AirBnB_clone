#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """Base class for all models in AirBnB clone project"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel with unique id and timestamps"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at timestamp"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

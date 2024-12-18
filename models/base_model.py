#!/usr/bin/python
"""
Module for console

"""
import datetime
import uuid


class BaseModel (object):
    """ 
    class for BaseModel

    """
    def self_uuid(self, id):
        """
        this is a public instance attribute assigning an uuid
        """
        self.uuid = uuid.uuid4()
        self.id = str(uuid.uuid4())

    def date_time(self):
        """
        assigns datetime
        """
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        prints the class name
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        return f"[{self.__dict__}] [{self.__class__.__name__}]"
    
    def format(self):
        """
        convereted to string with isoformat()

        """
        self.updated_at = isoformat(datetime.now())
        self.created_at = isoformat(datetime.now()) 

        
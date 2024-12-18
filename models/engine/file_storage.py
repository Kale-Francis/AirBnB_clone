#!/usr/bin/python
"""
Module for storage

"""
from json import json

class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """

    def __init__(self):
        """
        private attributes
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj
    
    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        self.__objects = self.__objects
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)
    
    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass

    
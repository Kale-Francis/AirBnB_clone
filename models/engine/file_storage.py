#!/usr/bin/python3
"""
Contains the FileStrorage class
"""
import json

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    def file_path(self):
        """path to the JSON file"""
        self.file_path = str('file.json')
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        self.__objects
        with open(self.file_path, 'w') as file:
            json.dump(self.__objects, file)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        self.__objects
        with open(self.file_path, 'r') as file:
            self.__objects = json.load(file)

    
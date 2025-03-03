#!/usr/bin/python3
"""FileStorage class for serializing and deserializing instances"""
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



class FileStorage:
    """Serializes instances to a JSON file and deserializes them back"""
    
    __file_path = "file.json"  # Path to JSON file
    __objects = {}  # Dictionary storing all objects

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets a new object in __objects with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    from models.base_model import BaseModel  # Avoid circular import

                    for key, value in obj_dict.items():
                        class_name = value["__class__"]
                        if class_name == "BaseModel":
                            self.__objects[key] = BaseModel(**value)
            except Exception:
                pass  # Avoid errors if the file is empty or corrupted

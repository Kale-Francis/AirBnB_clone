#!/usr/bin/python3
"""
Contains BaseModel tests

"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json

class BaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def test_base_model(self):
        """Tests for BaseModel class"""
        self.assertIsInstance(BaseModel(), BaseModel)


    def test_id(self):
        """Tests for id attribute"""
        self.assertIsInstance(BaseModel().id, str)

    def test_created_at(self):
        """Tests for created_at attribute"""
        self.assertIsInstance(BaseModel().created_at, datetime)

    def test_updated_at(self):
        """Tests for updated_at attribute"""
        self.assertIsInstance(BaseModel().updated_at, datetime)
    
    def test_str(self):
        """Tests for __str__ method"""
        self.assertIsInstance(BaseModel().__str__(), str)

    def test_save(self):
        """Tests for save method"""
        self.assertIsInstance(BaseModel().save(), None)

    def test_to_dict(self):
        """Tests for to_dict method"""
        self.assertIsInstance(BaseModel().to_dict(), dict)

    def test_kwargs(self):
        """Tests for kwargs"""
        self.assertIsInstance(BaseModel(**{'id': '123', 'created_at': '2022-01-01T00:00:00.000000', 'updated_at': '2022-01-01T00:00:00.000000'}), BaseModel)

    def test_args(self):
        """Tests for args"""
        self.assertIsInstance(BaseModel('123', '2022-01-01T00:00:00.000000', '2022-01-01T00:00:00.000000'), BaseModel)

    def test_storage(self):
        """Tests for storage"""
        self.assertIsInstance(storage, FileStorage)

    def test_desrialize(self):
        """Tests for deserialization"""
        self.assertIsInstance(BaseModel().deserialize({'id': '123', 'created_at': '2022-01-01T00:00:00.000000', 'updated_at': '2022-01-01T00:00:00.000000'}), BaseModel)

    def test_serialization(self):
        """Tests for serialization"""
        self.assertIsInstance(BaseModel().serialize(), dict)

    def test_json(self):
        """Tests for json"""
        self.assertIsInstance(BaseModel().to_json(), str)

    def test_intergation(self):
        """Tests for integration"""
        self.assertIsInstance(BaseModel().save(), None)

if __name__ == '__main__':
    unittest.main()
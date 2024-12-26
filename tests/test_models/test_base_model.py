#!/usr/bin/python3
"""
Contains BaseModel tests

"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import sys
sys.path.append('/path/to/AIRBNB_CLONE/models')

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

if __name__ == '__main__':
    unittest.main()
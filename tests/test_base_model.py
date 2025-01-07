#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class
    """
    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel class
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)

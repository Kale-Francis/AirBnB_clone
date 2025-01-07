#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.state import State

class TestFileStorage(unittest.TestCase):
    def test_all_method(self):
        """Test all method of FileStorage"""
        storage = FileStorage()
        state = State(name="California")
        storage.new(state)
        all_objects = storage.all(State)
        self.assertIn(f"State.{state.id}", all_objects)

    def test_save_method(self):
        """Test save method of FileStorage"""
        storage = FileStorage()
        state = State(name="California")
        storage.new(state)
        storage.save()
        # Check file saved, load and check if object is saved correctly

if __name__ == "__main__":
    unittest.main()

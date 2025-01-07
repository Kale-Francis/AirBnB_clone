#!/usr/bin/python3
"""Unittest for State class"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_create_state(self):
        """Test creating a new State instance"""
        state = State(name="California")
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "California")

    def test_state_to_dict(self):
        """Test to_dict method of State"""
        state = State(name="California")
        state_dict = state.to_dict()
        self.assertIn("name", state_dict)
        self.assertEqual(state_dict["name"], "California")

if __name__ == "__main__":
    unittest.main()

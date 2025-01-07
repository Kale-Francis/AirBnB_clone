#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_create_user(self):
        """Test creating a new User instance"""
        user = User(email="test@example.com", password="123456")
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "test@example.com")

    def test_user_to_dict(self):
        """Test to_dict method of User"""
        user = User(email="test@example.com", password="123456")
        user_dict = user.to_dict()
        self.assertIn("email", user_dict)
        self.assertEqual(user_dict["email"], "test@example.com")

if __name__ == "__main__":
    unittest.main()

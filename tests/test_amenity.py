#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_create_amenity(self):
        """Test creating a new Amenity instance"""
        amenity = Amenity(name="Pool")
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "Pool")

    def test_amenity_to_dict(self):
        """Test to_dict method of Amenity"""
        amenity = Amenity(name="Pool")
        amenity_dict = amenity.to_dict()
        self.assertIn("name", amenity_dict)
        self.assertEqual(amenity_dict["name"], "Pool")

if __name__ == "__main__":
    unittest.main()

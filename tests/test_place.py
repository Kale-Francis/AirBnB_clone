#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_create_place(self):
        """Test creating a new Place instance"""
        place = Place(name="Apartment", city_id="SF", user_id="123")
        self.assertIsInstance(place, Place)
        self.assertEqual(place.name, "Apartment")
        self.assertEqual(place.city_id, "SF")

    def test_place_to_dict(self):
        """Test to_dict method of Place"""
        place = Place(name="Apartment", city_id="SF")
        place_dict = place.to_dict()
        self.assertIn("name", place_dict)
        self.assertIn("city_id", place_dict)

if __name__ == "__main__":
    unittest.main()

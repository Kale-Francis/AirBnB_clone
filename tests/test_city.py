#!/usr/bin/python3
"""Unittest for City class"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_create_city(self):
        """Test creating a new City instance"""
        city = City(name="San Francisco", state_id="CA")
        self.assertIsInstance(city, City)
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.state_id, "CA")

    def test_city_to_dict(self):
        """Test to_dict method of City"""
        city = City(name="San Francisco", state_id="CA")
        city_dict = city.to_dict()
        self.assertIn("name", city_dict)
        self.assertIn("state_id", city_dict)

if __name__ == "__main__":
    unittest.main()

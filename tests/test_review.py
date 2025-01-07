#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_create_review(self):
        """Test creating a new Review instance"""
        review = Review(text="Great place!", place_id="123", user_id="456")
        self.assertIsInstance(review, Review)
        self.assertEqual(review.text, "Great place!")

    def test_review_to_dict(self):
        """Test to_dict method of Review"""
        review = Review(text="Great place!", place_id="123")
        review_dict = review.to_dict()
        self.assertIn("text", review_dict)
        self.assertEqual(review_dict["text"], "Great place!")

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
""" unittest from class Review """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ tests """
    def test_review(self):
        """ test """
        my_review = Review()
        self.assertIsInstance(my_review, Review)
        self.assertIsInstance(my_review, BaseModel)
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertTrue(hasattr(my_review, "text"))
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")


if __name__ == '__main__':
    unittest.main()

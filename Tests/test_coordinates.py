import unittest
from Models.coordinates import Coordinates


class CoordinatesUnitTests(unittest.TestCase):
    def test_compute_distance_to_returns_expected_value(self):
        shop_location = Coordinates(47.5869, -122.3368)
        user_location = Coordinates(47.6, -122.4)
        result = shop_location.compute_distance_to(user_location)
        expected_value = 0.0645
        self.assertEqual(result, expected_value)

    def test_that_when_invalid_arguments_are_provided_compute_distance_to_raises_attribute_error(self):
        shop_location = Coordinates(0, 0)
        with self.assertRaises(AttributeError):
            shop_location.compute_distance_to("New York")

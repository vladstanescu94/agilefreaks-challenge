import unittest

from Models.UserData import UserData
from Models.Coordinates import Coordinates
from Services.UserService import UserService


class UserServiceUnitTest(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()

    def tearDown(self):
        del self.user_service

    def test_that_get_user_data_from_args_returns_expected_value(self):
        user_args = ["23.2", "12.6", "http://test.com"]
        expected_outcome = UserData(Coordinates(23.2, 12.6), "http://test.com")
        result = self.user_service.get_user_data_from_args(user_args)

        self.assertEqual(result.coordinates.latitude,
                         expected_outcome.coordinates.latitude)
        self.assertEqual(result.coordinates.longitude,
                         expected_outcome.coordinates.longitude)
        self.assertEqual(result.csv_url, expected_outcome.csv_url)

    def test_that_get_user_data_from_args_raises_index_error(self):
        user_args = []

        with self.assertRaises(IndexError):
            self.user_service.get_user_data_from_args(user_args)

import unittest

from Models.UserData import UserData
from Models.Coordinates import Coordinates
from Services.UserService import UserService


class UserServiceUnitTest(unittest.TestCase):
    def setUp(self):
        user_args = ["23.2", "12.6", "http://test.com"]
        self.user_service = UserService(user_args)

    def tearDown(self):
        del self.user_service

    def test_get_user_data_returns_expected_value(self):
        expected_outcome = UserData(Coordinates(23.2, 12.6), "http://test.com")
        result = self.user_service.get_user_data()

        self.assertEqual(result.coordinates.latitude,
                         expected_outcome.coordinates.latitude)
        self.assertEqual(result.coordinates.longitude,
                         expected_outcome.coordinates.longitude)
        self.assertEqual(result.csv_url, expected_outcome.csv_url)

    def test_get_user_data_from_args_raises_index_error(self):
        self.user_service.args = []

        with self.assertRaises(IndexError):
            self.user_service.get_user_data()

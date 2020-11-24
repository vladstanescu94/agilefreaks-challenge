import unittest

from Services.csv_service import CSVService
from Utils.custom_csv_error import CSVServiceError, CSVServiceHTTPError, CSVServiceEmptyDataError


class CSVServiceUnitTest(unittest.TestCase):
    def setUp(self):
        self.csv_service = CSVService()

    def tearDown(self):
        del self.csv_service

    def test_get_csv_data_raises_exception_when_invalid_url_provided(self):
        url = "https://raw.githubusercontent.com/vladstanescu94/agilefreaks-challenge/develop/Resources/"

        with self.assertRaises(CSVServiceHTTPError):
            self.csv_service.get_csv_data(url)

    def test_get_csv_data_raises_exception_when_empty_csv_provided(self):
        url = "https://raw.githubusercontent.com/vladstanescu94/agilefreaks-challenge/develop/Resources/coffee_shops_empty.csv"

        with self.assertRaises(CSVServiceEmptyDataError):
            self.csv_service.get_csv_data(url)

    def test_get_csv_data_returns_expected_value(self):
        url = "https://raw.githubusercontent.com/vladstanescu94/agilefreaks-challenge/develop/Resources/coffee_shops.csv"

        expected_value = [
            ["Starbucks Seattle", "47.5809", "-122.3160"],
            ["Starbucks SF", "37.5209", "-122.3340"],
            ["Starbucks Moscow", "55.752047", "37.595242"],
            ["Starbucks Seattle2", "47.5869", "-122.3368"],
            ["Starbucks Rio De Janeiro", "-22.923489", "-43.234418"],
            ["Starbucks Sydney", "-33.871843", "151.206767"]
        ]

        result = self.csv_service.get_csv_data(url)

        self.assertEqual(result, expected_value)

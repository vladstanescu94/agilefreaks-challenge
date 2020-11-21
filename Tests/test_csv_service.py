import unittest
import requests

from Models.coordinates import Coordinates
from Models.coffee_shop import CoffeeShop
from Services.csv_service import CSVService
from Utils.custom_csv_error import CSVServiceHTTPError


class CSVServiceUnitTest(unittest.TestCase):
    def setUp(self):
        url = "https://raw.githubusercontent.com/vladstanescu94/agilefreaks-challenge/develop/Resources/coffee_shops.csv"
        self.csv_service = CSVService(csv_url=url)

    def tearDown(self):
        del self.csv_service

    def test_get_csv_data_from_url_raises_missing_schema_when_invalid_url_provided(self):
        self.csv_service.csv_url = "test"
        with self.assertRaises(requests.exceptions.MissingSchema):
            self.csv_service.get_csv_data_from_url()

    def test_get_csv_data_from_url_raises_http_eror_when_no_data_found_at__provided_url(self):
        self.csv_service.csv_url = "https://raw.githubusercontent.com/vladstanescu94/agilefreaks-challenge/develop/Resources/"
        with self.assertRaises(CSVServiceHTTPError):
            self.csv_service.get_csv_data_from_url()

    def test_get_coffee_shops_returns_expected_value(self):

        expected_result = [
            CoffeeShop("Starbucks Seattle", Coordinates(47.5809, -122.3160)),
            CoffeeShop("Starbucks SF", Coordinates(37.5209, -122.3340)),
            CoffeeShop("Starbucks Moscow", Coordinates(55.752047, 37.595242)),
            CoffeeShop("Starbucks Seattle2", Coordinates(47.5869, -122.3368)),
            CoffeeShop("Starbucks Rio De Janeiro",
                       Coordinates(-22.923489, -43.234418)),
            CoffeeShop("Starbucks Sydney",
                       Coordinates(-33.871843, 151.206767)),
        ]

        result = self.csv_service.get_coffee_shops()

        for index, shop in enumerate(result):
            self.assertEqual(shop.name, expected_result[index].name)
            self.assertEqual(shop.coordinates.latitude,
                             expected_result[index].coordinates.latitude)
            self.assertEqual(shop.coordinates.longitude,
                             expected_result[index].coordinates.longitude)

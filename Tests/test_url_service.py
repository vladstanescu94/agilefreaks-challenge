import unittest
import requests

from Models.Coordinates import Coordinates
from Models.CoffeeShop import CoffeeShop
from Services.URLService import URLService


class URLServiceUnitTest(unittest.TestCase):
    def setUp(self):
        url = url = "https://raw.githubusercontent.com/vladstanescu94/agilefreaks-challenge/develop/Resources/coffee_shops.csv"
        self.url_service = URLService(url)

    def tearDown(self):
        del self.url_service

    def test_that_get_coffeee_shops_raises_missing_schema_when_invalid_url_provided(self):
        self.url_service.url = "test"
        with self.assertRaises(requests.exceptions.MissingSchema):
            self.url_service.get_coffee_shops()

    def test_that_get_coffee_shops_returns_expected_value(self):

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

        result = self.url_service.get_coffee_shops()

        for index, shop in enumerate(result):
            self.assertEqual(shop.name, expected_result[index].name)
            self.assertEqual(shop.coordinates.latitude,
                             expected_result[index].coordinates.latitude)
            self.assertEqual(shop.coordinates.longitude,
                             expected_result[index].coordinates.longitude)

import unittest

from Models.coordinates import Coordinates
from Models.coffee_shop import CoffeeShop
from Services.coffee_shop_service import CoffeeShopService


class CoffeeShopServiceUnitTest(unittest.TestCase):
    def setUp(self):
        self.coffee_shop_service = CoffeeShopService()

    def tearDown(self):
        del self.coffee_shop_service

    def test_generate_coffee_shops_returns_expected_result(self):
        csv_data = [
            ["Starbucks Seattle", "47.5809", "-122.3160"]
        ]

        expected_result = [
            CoffeeShop("Starbucks Seattle", Coordinates(47.5809, -122.3160)),
        ]

        result = self.coffee_shop_service.generate_coffee_shops(csv_data)

        self.assertEqual(result[0].name, expected_result[0].name)
        self.assertEqual(result[0].coordinates.latitude,
                         expected_result[0].coordinates.latitude)
        self.assertEqual(result[0].coordinates.longitude,
                         expected_result[0].coordinates.longitude)

    def test_get_closest_shops_to_user_returns_expected_result(self):
        user_location = Coordinates(47.6, -122.4)
        shops = [
            CoffeeShop("Starbucks Seattle", Coordinates(47.5809, -122.3160)),
            CoffeeShop("Starbucks SF", Coordinates(37.5209, -122.3340)),
            CoffeeShop("Starbucks Moscow", Coordinates(55.752047, 37.595242)),
            CoffeeShop("Starbucks Seattle2", Coordinates(47.5869, -122.3368)),
            CoffeeShop("Starbucks Rio De Janeiro",
                       Coordinates(-22.923489, -43.234418)),
            CoffeeShop("Starbucks Sydney",
                       Coordinates(-33.871843, 151.206767)),
        ]

        expected_result = [
            ("Starbucks Seattle2", 0.0645),
            ("Starbucks Seattle", 0.0861),
            ("Starbucks SF", 10.0793)
        ]

        result = self.coffee_shop_service.get_closest_shops_to_user(user_location, shops)

        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 3)

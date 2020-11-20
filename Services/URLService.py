import csv
import requests
import codecs

from contextlib import closing
from Models.Coordinates import Coordinates
from Models.CoffeeShop import CoffeeShop


class URLService:

    def __init__(self, url):
        self.url = url

    def get_coffee_shops(self):
        response = self._get_url_data()
        csv_data = self._parse_csv_response(response)
        coffee_shops = self._generate_coffee_shops_list(csv_data)
        return coffee_shops

    def _get_url_data(self):
        return requests.get(self.url, stream=True)

    def _parse_csv_response(self, response):
        return csv.reader(codecs.iterdecode(response.iter_lines(), 'utf-8'), delimiter=',')

    def _generate_coffee_shops_list(self, csv_data):
        coffee_shops = []
        for row in csv_data:
            shop_name = row[0]
            shop_coordinates = Coordinates(row[1], row[2])
            shop = CoffeeShop(shop_name, shop_coordinates)
            coffee_shops.append(shop)

        return coffee_shops

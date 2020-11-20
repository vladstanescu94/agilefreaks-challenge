import csv
import requests
import codecs

from contextlib import closing
from Models.Coordinates import Coordinates
from Models.CoffeeShop import CoffeeShop


class CSVService:

    def get_coffee_shops_from_url(self, url):
        response = self.get_csv_data(url)
        csv_data = self.parse_csv_response(response)
        coffee_shops = self._generate_coffee_shops_list(csv_data)
        return coffee_shops

    def get_csv_data(self, url):
        return requests.get(url, stream=True)

    def parse_csv_response(self, response):
        return csv.reader(codecs.iterdecode(response.iter_lines(), 'utf-8'), delimiter=',')

    def _generate_coffee_shops_list(self, csv_data):
        coffee_shops = []
        for row in csv_data:
            shop_name = row[0]
            shop_coordinates = Coordinates(row[1], row[2])
            shop = CoffeeShop(shop_name, shop_coordinates)
            coffee_shops.append(shop)

        return coffee_shops

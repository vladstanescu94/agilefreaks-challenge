import csv
import requests
import codecs

from contextlib import closing
from Models.Coordinates import Coordinates
from Models.CoffeeShop import CoffeeShop


class CSVService:

    def __init__(self, csv_url):
        self.csv_url = csv_url

    def get_coffee_shops(self):
        response = self.get_csv_data_from_url()
        csv_data = self.parse_csv_response(response)
        coffee_shops = self._generate_coffee_shops_list(csv_data)
        return coffee_shops

    def get_csv_data_from_url(self):
        return requests.get(self.csv_url, stream=True)

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

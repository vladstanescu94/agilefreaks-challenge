import csv
import requests
import codecs

from contextlib import closing
from Models.Coordinates import Coordinates
from Models.CoffeeShop import CoffeeShop
from Utils.custom_csv_error import CSVServiceHTTPError, CSVServiceInvalidData


class CSVService:

    def __init__(self, csv_url):
        self.csv_url = csv_url

    def get_coffee_shops(self):
        csv_data = self.get_csv_data_from_url()
        coffee_shops = self.generate_coffee_shops_list(csv_data)
        return coffee_shops

    def get_csv_data_from_url(self):
        response = requests.get(self.csv_url, stream=True)
        self.validate_http_response(response)
        return response

    def generate_coffee_shops_list(self, csv_data):
        reader = csv.reader(codecs.iterdecode(csv_data.iter_lines(), 'utf-8'), delimiter=',')
        coffee_shops = []

        for row in reader:
            if not self.has_valid_size(row):
                print("Invalid Row... Skipping Over")
                continue
            shop_name = row[0]
            shop_coordinates = Coordinates(row[1], row[2])
            shop = CoffeeShop(shop_name, shop_coordinates)
            coffee_shops.append(shop)

        self.validate_shops_list(coffee_shops)
        return coffee_shops

    def validate_http_response(self, response):
        if response.status_code != 200:
            raise CSVServiceHTTPError(f"HTTP Error - {response.status_code}, please check url:\n{self.csv_url}")

    def has_valid_size(self, row):
        return len(row) >= 3

    def validate_shops_list(self, shops):
        if len(shops) < 1:
            raise CSVServiceInvalidData(f"Error no data from CSV, please check CSV contents from url:\n{self.csv_url}")

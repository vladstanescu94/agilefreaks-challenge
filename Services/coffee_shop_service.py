from Models.coordinates import Coordinates
from Models.coffee_shop import CoffeeShop


class CoffeeShopService:

    def generate_coffee_shops(self, csv_data):
        coffee_shops = []
        for row in csv_data:
            try:
                shop_name = row[0]
                shop_coordinates = Coordinates(row[1], row[2])
                shop = CoffeeShop(shop_name, shop_coordinates)
                coffee_shops.append(shop)
            except:
                print(f"Invalid data ... Skipping over row {row} ")
                continue
        return coffee_shops

    def get_closest_shops_to_user(self, user_location, shops):
        closest_shops = map(lambda shop: (shop.name, shop.coordinates.compute_distance_to(user_location)), shops)
        unique_shops = self._remove_duplicate_shops(closest_shops)
        sorted_shops = sorted(unique_shops, key=lambda x: x[1])
        return sorted_shops[:3]

    def _remove_duplicate_shops(self, shop_list):
        return list(set([shop for shop in shop_list]))

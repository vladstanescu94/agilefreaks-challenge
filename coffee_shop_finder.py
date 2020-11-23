import sys
from Services.user_service import UserService
from Services.csv_service import CSVService
from Services.coffee_shop_service import CoffeeShopService
from Utils.custom_csv_error import CSVServiceError


def main():
    user_args = sys.argv[1:]
    user_service = UserService(args=user_args)
    csv_service = CSVService()

    try:
        user_data = user_service.get_user_data()
        csv_data = csv_service.get_csv_data(user_data.csv_url)
    except (IndexError, CSVServiceError) as error:
        print(error)
        sys.exit(1)

    coffee_shop_service = CoffeeShopService()
    coffee_shops = coffee_shop_service.generate_coffee_shops(csv_data=csv_data)
    closest_shops = coffee_shop_service.get_closest_shops_to_user(user_data.coordinates, coffee_shops)

    for shop in closest_shops:
        print(f"{shop[0]},{shop[1]}")


if __name__ == "__main__":
    main()

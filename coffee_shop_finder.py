import sys
from Services.UserService import UserService
from Services.CSVService import CSVService
from Utils.custom_csv_error import CSVServiceError


def main():
    user_args = sys.argv[1:]
    user_service = UserService(args=user_args)
    user_data = user_service.get_user_data()

    csv_service = CSVService(csv_url=user_data.csv_url)
    try:
        coffee_shops = csv_service.get_coffee_shops()
        closest_shops = get_closest_shops_to_user(user_data.coordinates, coffee_shops)
        for shop in closest_shops:
            print(f"{shop[0]},{shop[1]}")

    except CSVServiceError as error:
        print(error)
        sys.exit(1)


def get_closest_shops_to_user(user_location, shops):
    closest_shops = map(lambda shop: (shop.name, shop.coordinates.compute_distance_to(user_location)), shops)
    sorted_shops = sorted(closest_shops, key=lambda x: x[1])
    return sorted_shops[:3]


if __name__ == "__main__":
    main()

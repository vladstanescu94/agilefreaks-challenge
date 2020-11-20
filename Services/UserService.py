from Models.Coordinates import Coordinates
from Models.UserData import UserData


class UserService:
    def get_user_data_from_args(self, args):
        self.validate_user_args(args)
        user_coordinates = Coordinates(args[0], args[1])
        user_url = args[2]
        return UserData(user_coordinates, user_url)

    def validate_user_args(self, args):
        if len(args) < 3:
            raise IndexError(
                "Must provide 3 arguments as input: latitude logitude csv_url")

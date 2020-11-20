from Models.Coordinates import Coordinates
from Models.UserData import UserData


class UserService:
    def __init__(self, args):
        self.args = args

    def get_user_data(self):
        self.validate_user_args(self.args)
        user_coordinates = Coordinates(self.args[0], self.args[1])
        user_url = self.args[2]
        return UserData(user_coordinates, user_url)

    def validate_user_args(self, args):
        if len(args) < 3:
            raise IndexError(
                "Must provide 3 arguments as input: latitude logitude csv_url")

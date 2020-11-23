from Models.coordinates import Coordinates
from Models.user_data import UserData


class UserService:
    def __init__(self, args):
        self.args = args

    def get_user_data(self):
        self.validate_user_args()
        user_coordinates = Coordinates(self.args[0], self.args[1])
        user_url = self.args[2]
        return UserData(user_coordinates, user_url)

    def validate_user_args(self):
        if len(self.args) < 3:
            raise IndexError("Error - must provide 3 arguments as input: latitude logitude csv_url")

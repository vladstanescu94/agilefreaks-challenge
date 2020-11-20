from math import sqrt
from Utils.exceptions import InvalidCoordinates


class Coordinates:
    def __init__(self, latitude, longitude):
        try:
            self.latitude = float(latitude)
            self.longitude = float(longitude)
        except Exception as error:
            raise InvalidCoordinates(f"Invalid Coordinates Provided: {error}")

    def compute_distance_to(self, target_coordinates):
        return round(sqrt((self.latitude - target_coordinates.latitude)**2 + (self.longitude - target_coordinates.longitude)**2), 4)

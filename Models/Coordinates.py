from math import sqrt


class Coordinates:
    def __init__(self, latitude, longitude):
        try:
            self.latitude = float(latitude)
            self.longitude = float(longitude)
        except (ValueError, TypeError) as error:
            print(f"Invalid Coordinates Provided: {error}")

    def compute_distance_to(self, target_coordinates):
        return round(sqrt((self.latitude - target_coordinates.latitude)**2 + (self.longitude - target_coordinates.longitude)**2), 4)

from math import sqrt


class Coordinates:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def compute_distance_to(self, target_coordinates):
        return round(sqrt((self.latitude - target_coordinates.latitude)**2 + (self.longitude - target_coordinates.longitude)**2), 4)

#!/usr/bin/env python3

import math


class lat_long_distance:
    def __init__(self):
        self.__EARTH_RADIUS = 6371.0  # km

    def __haversin(self, radians_theta):
        return (math.sin(radians_theta / 2)) ** 2

    def getDistance(self, long1, lat1, long2, lat2):
        radians_long1 = math.radians(long1)
        radians_lat1 = math.radians(lat1)
        radians_long2 = math.radians(long2)
        radians_lat2 = math.radians(lat2)

        difference_long = abs(radians_long1 - radians_long2)
        difference_lat = abs(radians_lat1 - radians_lat2)

        h = self.__haversin(difference_lat) + math.cos(radians_lat1) * math.cos(radians_lat2) * self.__haversin(difference_long)
        distance = 2 * self.__EARTH_RADIUS * math.asin(math.sqrt(h))  # km

        return distance * 1000  # m

"""
Jakub Korsak
"""
import random

from numpy import sort

from car import Car
from config import Config
from road import Road


class Traffic:
    """
    A class representing the entity controlling interactions between cars
    """
    def __init__(self, params=None):
        if params is None:
            params = {}
        self.road = params["road"] if "road" in params else None
        self.road_size = params["road_size"] if "road_size" in params else Config.road_size
        self.noise = params["noise"] if "noise" in params else Config.noise

    def get_initial_traffic(self, amount):
        """
        Create the initial Traffic object containing randomly placed cars
        :param amount: the amount of cars to be created
        :return: self
        """
        positions = sort(random.sample(range(0, self.road_size), amount))
        self.road = Road([Car(position=int(position), velocity=0) for position in positions])
        return self

    def evaluate_distances(self) -> list:
        """

        :return: List of distances between neighboring cars (taking into account pbc)
        """
        if self.road is None:
            return []
        if len(self.road) == 1:
            return [None]
        dists = []
        for i, _ in enumerate(self.road):
            difference = self.road[i + 1].position - self.road[i].position
            if difference < 0:
                difference = self.road_size - self.road[i].position + self.road[i + 1].position
            dists.append(difference - 1)
        return dists

    def move_cars(self):
        """
        Move cars in Traffic following the rules:
        - if a car can accelerate, let it.
        - if it cannot, stop it
        - with some probability (given with self.noise) stop a car
        :return: self
        """
        dists = self.evaluate_distances()
        random_cars_indexes = random.sample(range(0, len(self.road) - 1),
                                            round(self.noise * len(self.road)))
        for i, _ in enumerate(self.road):
            if dists[i] > 0:
                if self.road[i].velocity < dists[i]:
                    self.road[i].accelerate(self.road_size)
                else:
                    self.road[i].velocity = dists[i] - 1
                    self.road[i].accelerate(self.road_size)
            elif dists[i] == 0:
                self.road[i].brake()
            if i in random_cars_indexes:
                self.road[i].brake()
        return self

    def get_cars_positions(self):
        """

        :return: List of positions of cars in Traffic
        """
        return [car.position for car in self.road]

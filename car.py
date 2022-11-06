"""
class Car
"""


class Car:
    """
    A class representing a car in a traffic jam
    """


    def __init__(self, position: int, velocity: int = 0, params=None):
        if params is None:
            params = {}
        self.position = position
        self.velocity = velocity
        self.road_size = params["road_size"] if "road_size" in params else None

    def accelerate(self, road_size):
        """
        Accelerate a car
        :param road_size: the size of the road
        :return: self
        """
        self.velocity += 1
        self._move(road_size)
        return self

    def brake(self):
        """
        Stop the car
        :return: self
        """
        self.velocity = 0
        return self

    def random_slowdown(self):
        """
        Randomly stop the car
        :return: self
        """
        self.brake()
        return self

    def _move(self, road_size):
        """
        Move a car while respecting the periodic boundary conditions
        :param road_size: needed in order to determine when cars go around the road
        """
        self.position += self.velocity
        if self.position >= road_size:
            self.position -= road_size
        elif self.position < 0:
            self.position += road_size

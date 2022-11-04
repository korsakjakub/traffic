from config import Config
import numpy as np


class Traffic:
    def __init__(self, params=None):
        if params is None:
            params = {}
        self.cars = None
        self.road_size = params["road_size"] if "road_size" in params else Config.road_size

    def get_initial_traffic(self, amount):
        positions = np.random.randint(self.road_size, size=(amount,))
        print(positions)
